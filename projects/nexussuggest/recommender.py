"""
NexusSuggest - Hybrid Recommender Engine.
"""
import numpy as np
from typing import List, Dict, Any
from .similarity import ContentRecommender, CollaborativeRecommender

class HybridRecommender:
    """
    Hybrid Recommendation Engine for NexusSuggest.
    Blends User-Based and Item-Based Collaborative Filtering scores with min-max normalization,
    and automatically falls back to content-based similarity for cold-start profiles.
    """
    def __init__(self):
        self.content = ContentRecommender()
        self.collaborative = CollaborativeRecommender()

    def fit(self):
        self.content.fit()
        self.collaborative.fit()

    def _wrap_metadata(self, item_id: str, score: float) -> Dict[str, Any]:
        if not hasattr(self, "_item_details"):
            self._item_details = self.content.df_items.set_index("item_id")[["title", "genre"]].to_dict(orient="index")
        details = self._item_details.get(item_id, {"title": "Unknown", "genre": "Unknown"})
        return {
            "item_id": item_id,
            "title": details["title"],
            "genre": details["genre"],
            "score": float(score)
        }

    def get_hybrid_recommendations(
        self,
        user_id: str,
        top_n: int = 10,
        alpha: float = 0.5,
        preferred_genre: str = "AI"
    ) -> List[Dict[str, Any]]:
        # Case 1: Active Existing User
        if user_id in self.collaborative.user_to_idx:
            u_idx = self.collaborative.user_to_idx[user_id]
            user_mean = self.collaborative.user_means[u_idx]
            sims = self.collaborative.user_similarity[u_idx]

            # 1. User-Based predictions
            k = 50
            sorted_user_indices = np.argsort(sims)[::-1]
            similar_users = [idx for idx in sorted_user_indices if idx != u_idx][:k]

            if similar_users:
                k_sims = sims[similar_users]
                k_ratings = self.collaborative.df_pivot.values[similar_users]
                k_means = self.collaborative.user_means[similar_users]

                k_ratings_centered = k_ratings - k_means[:, np.newaxis]
                k_rated_mask = ~np.isnan(k_ratings_centered)
                k_ratings_centered_zero = np.nan_to_num(k_ratings_centered)

                weighted_sum = np.dot(k_sims, k_ratings_centered_zero)
                abs_sims_weighted = np.abs(k_sims)[:, np.newaxis] * k_rated_mask
                sum_abs_sims = np.sum(abs_sims_weighted, axis=0)

                with np.errstate(divide="ignore", invalid="ignore"):
                    predicted_centered = np.where(sum_abs_sims > 0, weighted_sum / sum_abs_sims, np.nan)
                user_scores = user_mean + predicted_centered
            else:
                user_scores = np.full(len(self.collaborative.item_ids), np.nan)

            # 2. Item-Based predictions
            user_ratings = self.collaborative.df_pivot.values[u_idx]
            rated_indices = np.where(~np.isnan(user_ratings))[0]
            highly_rated_indices = [idx for idx in rated_indices if user_ratings[idx] >= 3.0] or list(rated_indices)

            if highly_rated_indices:
                ratings_highly_rated = user_ratings[highly_rated_indices]
                sims_slice = self.collaborative.item_similarity[:, highly_rated_indices]
                weighted_sum_item = np.dot(sims_slice, ratings_highly_rated)
                sum_abs_sims_item = np.sum(np.abs(sims_slice), axis=1)

                with np.errstate(divide="ignore", invalid="ignore"):
                    item_scores = np.where(sum_abs_sims_item > 0, weighted_sum_item / sum_abs_sims_item, np.nan)
            else:
                item_scores = np.full(len(self.collaborative.item_ids), np.nan)

            # 3. Min-Max Normalization
            user_min, user_max = np.nanmin(user_scores), np.nanmax(user_scores)
            user_denom = (user_max - user_min) or 1e-9
            user_scores_norm = (user_scores - user_min) / user_denom

            item_min, item_max = np.nanmin(item_scores), np.nanmax(item_scores)
            item_denom = (item_max - item_min) or 1e-9
            item_scores_norm = (item_scores - item_min) / item_denom

            # 4. Linear Fusion Blending
            combined_scores = alpha * user_scores_norm + (1 - alpha) * item_scores_norm
            combined_scores[rated_indices] = np.nan

            non_nan_indices = np.where(~np.isnan(combined_scores))[0]
            sorted_recs = sorted(non_nan_indices, key=lambda idx: combined_scores[idx], reverse=True)

            recommendations = []
            for idx in sorted_recs[:top_n]:
                item_id = self.collaborative.item_ids[idx]
                score = combined_scores[idx]
                recommendations.append(self._wrap_metadata(item_id, score))
            return recommendations

        # Case 2: Cold-Start Fallback
        else:
            df_items = self.content.df_items
            genre_items = df_items[df_items["genre"].str.lower() == preferred_genre.lower()]
            first_item_id = genre_items.iloc[0]["item_id"] if not genre_items.empty else df_items.iloc[0]["item_id"]

            content_recs = self.content.get_content_recommendations(first_item_id, top_n=top_n)
            return [
                {
                    "item_id": rec["item_id"],
                    "title": rec["title"],
                    "genre": rec["genre"],
                    "score": rec["similarity"]
                }
                for rec in content_recs
            ]

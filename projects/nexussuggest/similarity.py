"""
NexusSuggest - Content and Collaborative Similarity Algorithms (Cloud-Optimized & Low-Memory).
"""
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .utils import ITEMS_CSV, INTERACTIONS_CSV, ensure_dataset_exists

class ContentRecommender:
    """
    Content-Based Filtering Recommendation Engine.
    """
    def __init__(self, items_path: str = ITEMS_CSV):
        ensure_dataset_exists()
        self.items_path = items_path
        self.df_items = pd.read_csv(self.items_path)
        self.id_to_idx = pd.Series(self.df_items.index, index=self.df_items["item_id"]).to_dict()
        self.vectorizer = None
        self.tfidf_matrix = None

    def fit(self):
        combined_text = self.df_items["genre"].fillna("") + " " + self.df_items["description"].fillna("")
        self.vectorizer = TfidfVectorizer(stop_words="english", max_features=3000)
        self.tfidf_matrix = self.vectorizer.fit_transform(combined_text)

    def get_content_recommendations(self, item_id: str, top_n: int = 10):
        if self.tfidf_matrix is None:
            raise RuntimeError("Model must be fitted before querying.")
        if item_id not in self.id_to_idx:
            raise KeyError(f"Item ID '{item_id}' not found.")

        idx = self.id_to_idx[item_id]
        target_vec = self.tfidf_matrix[idx]
        sim_scores = cosine_similarity(target_vec, self.tfidf_matrix).flatten().astype(np.float32)
        sorted_indices = sim_scores.argsort()[::-1]

        recommendations = []
        for other_idx in sorted_indices:
            if other_idx == idx:
                continue
            item_row = self.df_items.iloc[other_idx]
            recommendations.append({
                "item_id": item_row["item_id"],
                "title": item_row["title"],
                "genre": item_row["genre"],
                "similarity": float(sim_scores[other_idx])
            })
            if len(recommendations) >= top_n:
                break
        return recommendations


class CollaborativeRecommender:
    """
    Memory-efficient Collaborative Filtering using on-demand vector similarity.
    Avoids precomputing dense (10000, 10000) matrices in RAM.
    """
    def __init__(self, interactions_path: str = INTERACTIONS_CSV, items_path: str = ITEMS_CSV):
        ensure_dataset_exists()
        self.df_interactions = pd.read_csv(interactions_path)
        self.df_items = pd.read_csv(items_path)

        self.user_ids = sorted(self.df_interactions["user_id"].unique())
        self.item_ids = sorted(self.df_items["item_id"].unique())

        self.user_to_idx = {uid: i for i, uid in enumerate(self.user_ids)}
        self.item_to_idx = {iid: i for i, iid in enumerate(self.item_ids)}

        self.df_pivot = None
        self.user_means = None
        self.matrix_centered = None
        self.user_norms = None

    def fit(self):
        raw_pivot = self.df_interactions.pivot(index="user_id", columns="item_id", values="rating")
        self.df_pivot = raw_pivot.reindex(index=self.user_ids, columns=self.item_ids)

        self.user_means = self.df_pivot.mean(axis=1).fillna(3.0).values.astype(np.float32)
        df_pivot_centered = self.df_pivot.sub(self.user_means, axis=0)
        self.matrix_centered = df_pivot_centered.fillna(0).values.astype(np.float32)
        self.user_norms = np.linalg.norm(self.matrix_centered, axis=1).astype(np.float32)

    def get_user_similarity_vector(self, u_idx: int) -> np.ndarray:
        """
        Computes cosine similarity for a single user on-demand.
        """
        u_vec = self.matrix_centered[u_idx]
        u_norm = self.user_norms[u_idx]
        if u_norm == 0:
            return np.zeros(len(self.user_ids), dtype=np.float32)
        denom = self.user_norms * u_norm + 1e-9
        return np.dot(self.matrix_centered, u_vec) / denom

    def get_item_similarity_for_indices(self, item_indices: list) -> np.ndarray:
        """
        Computes item-to-item similarity for target item indices on-demand.
        """
        target_items = self.matrix_centered[:, item_indices].T  # shape (k, users)
        all_items = self.matrix_centered.T  # shape (items, users)
        return cosine_similarity(all_items, target_items).astype(np.float32)

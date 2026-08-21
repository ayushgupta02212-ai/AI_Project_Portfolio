"""
NexusSuggest - Dataset Paths and Fallback Initialization Utilities.
"""
import os
import random
import numpy as np
import pandas as pd

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
ITEMS_CSV = os.path.join(DATA_DIR, "items.csv")
INTERACTIONS_CSV = os.path.join(DATA_DIR, "interactions.csv")

def ensure_dataset_exists():
    """
    Ensures items.csv and interactions.csv exist in the data directory.
    If missing, automatically generates the synthetic benchmark dataset.
    """
    if os.path.exists(ITEMS_CSV) and os.path.exists(INTERACTIONS_CSV):
        return

    os.makedirs(DATA_DIR, exist_ok=True)
    np.random.seed(42)
    random.seed(42)

    genres = ["AI", "DevOps", "Quantum Computing", "Web Development"]
    adjectives = ["Advanced", "Introductory", "Practical", "Enterprise", "Scalable", "High-Performance", "Modern", "Deep", "Automated", "Cloud-Native"]
    genre_concepts = {
        "AI": ["Machine Learning", "Neural Networks", "Deep Learning", "NLP", "Computer Vision", "LLMs", "Transformers"],
        "DevOps": ["Continuous Integration", "Infrastructure as Code", "Kubernetes", "Docker", "Site Reliability", "Microservices"],
        "Quantum Computing": ["Quantum Algorithms", "Superposition", "Qubit Simulation", "Quantum Gates", "Qiskit", "Quantum Cryptography"],
        "Web Development": ["React Framework", "State Management", "Server-Side Rendering", "GraphQL APIs", "Web Security"]
    }
    formats = ["Handbook", "Masterclass", "Essentials", "Deep Dive", "Cookbook", "Foundations", "Guide"]

    items_data = []
    item_count = 1
    for genre, concepts in genre_concepts.items():
        for concept in concepts:
            for adj in adjectives:
                for fmt in formats:
                    if item_count > 5000:
                        break
                    items_data.append({
                        "item_id": f"item_{item_count}",
                        "title": f"{adj} {concept} {fmt}",
                        "genre": genre,
                        "description": f"Comprehensive guide to {concept} exploring {adj.lower()} patterns in {genre}."
                    })
                    item_count += 1

    df_items = pd.DataFrame(items_data)
    df_items.to_csv(ITEMS_CSV, index=False)

    users = [f"user_{i+1}" for i in range(10000)]
    interactions = []
    item_ids = df_items["item_id"].tolist()

    for user_id in users:
        sampled_items = random.sample(item_ids, random.randint(12, 16))
        for item in sampled_items:
            rating = int(np.random.choice([1, 2, 3, 4, 5], p=[0.05, 0.1, 0.25, 0.35, 0.25]))
            interactions.append((user_id, item, rating))

    df_interactions = pd.DataFrame(interactions, columns=["user_id", "item_id", "rating"])
    df_interactions.to_csv(INTERACTIONS_CSV, index=False)

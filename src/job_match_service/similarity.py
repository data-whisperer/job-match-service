"""
Module for calculating similarities between text embeddings.
"""

from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityService:
    @staticmethod
    def calculate_similarity(embedding1: List[float], embedding2: List[float]) -> float:
        """Calculate cosine similarity between two embeddings."""
        return float(cosine_similarity(
            [embedding1],
            [embedding2]
        )[0][0])

    @staticmethod
    def calculate_similarities(
        query_embedding: List[float],
        embeddings: List[List[float]]
    ) -> List[float]:
        """Calculate similarities between a query embedding and a list of embeddings."""
        return cosine_similarity(
            [query_embedding],
            embeddings
        )[0].tolist() 
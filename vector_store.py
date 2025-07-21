"""
Vector store implementation for analogical reasoning and similarity search.
"""

import json
import numpy as np
from typing import List, Dict, Any, Optional
import logging
import os

# Try to import sentence_transformers with fallback
try:
    from sentence_transformers import SentenceTransformer
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SentenceTransformer = None
    SENTENCE_TRANSFORMERS_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimpleVectorStore:
    """Simple in-memory vector store for analogical reasoning."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.analogies = []
        self.vectors = []
        self.model = None
        self.model_name = model_name
        self._initialize_model()

    def _initialize_model(self):
        """Initialize the sentence transformer model."""
        try:
            if SENTENCE_TRANSFORMERS_AVAILABLE:
                self.model = SentenceTransformer(self.model_name)
                logger.info(f"Initialized SentenceTransformer model: {self.model_name}")
            else:
                self.model = None
                logger.warning("SentenceTransformer not available, using text-only storage")
        except Exception as e:
            logger.error(f"Error initializing model: {e}")
            self.model = None

    def add_analogy(self, trend: str, brand: str, analogy: str) -> bool:
        """Add an analogy to the vector store."""
        try:
            if not self.model:
                logger.warning("Model not available, storing without embeddings")
                self.analogies.append({
                    'trend': trend,
                    'brand': brand,
                    'analogy': analogy
                })
                return True

            # Create text for embedding
            text = f"Trend: {trend}, Brand: {brand}, Analogy: {analogy}"

            # Generate embedding
            embedding = self.model.encode(text)

            # Store analogy and vector
            analogy_data = {
                'trend': trend,
                'brand': brand, 
                'analogy': analogy,
                'text': text
            }

            self.analogies.append(analogy_data)
            self.vectors.append(embedding)

            logger.info(f"Added analogy for {brand} x {trend}")
            return True

        except Exception as e:
            logger.error(f"Error adding analogy: {e}")
            return False

    def find_similar_analogies(self, trend: str, brand: str, limit: int = 5) -> List[Dict]:
        """Find similar analogies based on vector similarity."""
        try:
            if not self.model or not self.vectors:
                return []

            # Create query text
            query_text = f"Trend: {trend}, Brand: {brand}"

            # Generate query embedding
            query_embedding = self.model.encode(query_text)

            # Calculate similarities
            similarities = []
            for i, vector in enumerate(self.vectors):
                similarity = np.dot(query_embedding, vector) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(vector)
                )
                similarities.append((similarity, i))

            # Sort by similarity and return top results
            similarities.sort(reverse=True, key=lambda x: x[0])

            results = []
            for similarity, index in similarities[:limit]:
                if similarity > 0.5:  # Minimum similarity threshold
                    analogy_data = self.analogies[index].copy()
                    analogy_data['similarity'] = float(similarity)
                    results.append(analogy_data)

            return results

        except Exception as e:
            logger.error(f"Error finding similar analogies: {e}")
            return []

    def get_stats(self) -> Dict[str, Any]:
        """Get vector store statistics."""
        return {
            'total_analogies': len(self.analogies),
            'vector_size': len(self.vectors[0]) if self.vectors else 0,
            'model_name': self.model_name,
            'model_available': self.model is not None
        }

    def save_to_file(self, filename: str = "vector_store.json") -> bool:
        """Save analogies to file (vectors not saved due to size)."""
        try:
            data = {
                'analogies': self.analogies,
                'model_name': self.model_name,
                'stats': self.get_stats()
            }

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2, default=str)

            logger.info(f"Saved vector store to {filename}")
            return True

        except Exception as e:
            logger.error(f"Error saving vector store: {e}")
            return False

    def load_from_file(self, filename: str = "vector_store.json") -> bool:
        """Load analogies from file."""
        try:
            if not os.path.exists(filename):
                return False

            with open(filename, 'r') as f:
                data = json.load(f)

            self.analogies = data.get('analogies', [])

            # Regenerate vectors for loaded analogies
            if self.model:
                self.vectors = []
                for analogy_data in self.analogies:
                    text = analogy_data.get('text', f"Trend: {analogy_data['trend']}, Brand: {analogy_data['brand']}")
                    embedding = self.model.encode(text)
                    self.vectors.append(embedding)

            logger.info(f"Loaded vector store from {filename}")
            return True

        except Exception as e:
            logger.error(f"Error loading vector store: {e}")
            return False

class QdrantVectorStore:
    """Qdrant vector store wrapper for production use."""

    def __init__(self):
        self.simple_store = SimpleVectorStore()
        logger.info("Initialized QdrantVectorStore with SimpleVectorStore backend")

    def add_analogy(self, trend: str, brand: str, analogy: str) -> bool:
        """Add analogy to vector store."""
        return self.simple_store.add_analogy(trend, brand, analogy)

    def find_similar_analogies(self, trend: str, brand: str, limit: int = 5) -> List[Dict]:
        """Find similar analogies."""
        return self.simple_store.find_similar_analogies(trend, brand, limit)

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics."""
        stats = self.simple_store.get_stats()
        stats['backend'] = 'SimpleVectorStore'
        return stats
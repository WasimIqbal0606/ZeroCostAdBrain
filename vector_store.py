"""
Vector store implementation for analogical reasoning and similarity search.
Uses Qdrant for production-grade vector storage and retrieval.
"""

import json
import os
import hashlib
from typing import List, Dict, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import requests
import logging

logger = logging.getLogger(__name__)

class QdrantVectorStore:
    """Qdrant-powered vector store for analogies and trends."""
    
    def __init__(self):
        self.client = None
        self.collection_name = "analogies"
        self.embedding_dim = 384  # Using sentence-transformers compatible size
        self.db = None
        self._setup_qdrant()
        self._ensure_collection()
        self._setup_database_integration()
    
    def _setup_database_integration(self):
        """Setup PostgreSQL database integration."""
        try:
            from database import DatabaseManager
            self.db = DatabaseManager()
        except Exception as e:
            logger.warning(f"Database integration not available: {e}")
            self.db = None
    
    def _setup_qdrant(self):
        """Setup Qdrant client - try in-memory first, fallback to local file."""
        try:
            # Try in-memory Qdrant for demo
            self.client = QdrantClient(":memory:")
            logger.info("Using in-memory Qdrant")
        except Exception as e:
            logger.warning(f"Could not setup Qdrant: {e}")
            self.client = None
    
    def _ensure_collection(self):
        """Ensure the analogies collection exists."""
        if not self.client:
            return
        
        try:
            collections = self.client.get_collections()
            collection_names = [c.name for c in collections.collections]
            
            if self.collection_name not in collection_names:
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=self.embedding_dim, distance=Distance.COSINE)
                )
                logger.info(f"Created collection: {self.collection_name}")
        except Exception as e:
            logger.error(f"Error ensuring collection: {e}")
    
    def _get_embedding(self, text: str) -> List[float]:
        """Get embedding for text using Hugging Face API."""
        try:
            # Use sentence-transformers via HF API
            api_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
            headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN', '')}"}
            
            response = requests.post(api_url, headers=headers, json={"inputs": text})
            
            if response.status_code == 200:
                embedding = response.json()
                if isinstance(embedding, list) and len(embedding) > 0:
                    # Handle nested list structure
                    if isinstance(embedding[0], list):
                        return embedding[0]
                    return embedding
            
            # Fallback: create simple hash-based vector
            import hashlib
            hash_obj = hashlib.md5(text.encode())
            hash_bytes = hash_obj.digest()
            # Convert to normalized vector of required dimension
            vector = []
            for i in range(self.embedding_dim):
                vector.append((hash_bytes[i % len(hash_bytes)] - 128) / 128.0)
            return vector
            
        except Exception as e:
            logger.error(f"Error getting embedding: {e}")
            # Fallback vector
            return [0.1] * self.embedding_dim
    
    def add_analogy(self, trend: str, brand: str, analogy: str) -> str:
        """Add an analogy to the vector store."""
        analogy_id = hashlib.md5(f"{trend}_{brand}_{analogy}".encode()).hexdigest()
        
        # Store in database first
        if self.db:
            embedding = self._get_embedding(f"{trend} {brand} {analogy}")
            db_id = self.db.save_analogy(trend, brand, analogy, embedding)
            if db_id:
                analogy_id = db_id
        
        # Store in Qdrant for vector search
        if not self.client:
            return analogy_id
        
        try:
            # Get embedding for the analogy text
            embedding = self._get_embedding(f"{trend} {brand} {analogy}")
            
            # Create point for Qdrant
            point = PointStruct(
                id=analogy_id,
                vector=embedding,
                payload={
                    "trend": trend,
                    "brand": brand,
                    "analogy": analogy,
                    "type": "analogy"
                }
            )
            
            self.client.upsert(
                collection_name=self.collection_name,
                points=[point]
            )
            
            logger.info(f"Added analogy to Qdrant: {analogy_id}")
            return analogy_id
            
        except Exception as e:
            logger.error(f"Error adding analogy: {e}")
            return analogy_id
    
    def find_similar_analogies(self, trend: str, brand: str, limit: int = 3) -> List[Dict]:
        """Find similar analogies for a given trend and brand."""
        if not self.client:
            return []
        
        try:
            # Get embedding for query
            query_embedding = self._get_embedding(f"{trend} {brand}")
            
            # Search in Qdrant
            search_result = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=limit,
                score_threshold=0.3  # Only return reasonably similar results
            )
            
            results = []
            for hit in search_result:
                if hit.payload:
                    result = dict(hit.payload)
                    result["similarity"] = float(hit.score)
                    results.append(result)
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching analogies: {e}")
            return []
    
    def get_stats(self) -> Dict:
        """Get statistics about the vector store."""
        if not self.client:
            return {"total_analogies": 0, "unique_trends": 0, "unique_brands": 0}
        
        try:
            collection_info = self.client.get_collection(self.collection_name)
            points_count = collection_info.points_count or 0
            
            # Get some points to analyze unique trends/brands
            scroll_result = self.client.scroll(
                collection_name=self.collection_name,
                limit=1000  # Get up to 1000 points for stats
            )
            
            trends = set()
            brands = set()
            
            for point in scroll_result[0]:
                if point.payload:
                    trends.add(point.payload.get("trend", ""))
                    brands.add(point.payload.get("brand", ""))
            
            return {
                "total_analogies": points_count,
                "unique_trends": len(trends),
                "unique_brands": len(brands)
            }
            
        except Exception as e:
            logger.error(f"Error getting stats: {e}")
            return {"total_analogies": 0, "unique_trends": 0, "unique_brands": 0}

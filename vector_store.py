"""
Vector store implementation for analogical reasoning and similarity search.
Uses in-memory storage for simplicity since this is a demo app.
"""

import json
import os
import hashlib
from typing import List, Dict, Tuple

class SimpleVectorStore:
    """Simple in-memory vector store for analogies and trends."""
    
    def __init__(self):
        self.analogies = {}
        self.metadata = {}
        self.data_file = "vector_data.json"
        self.load_data()
    
    def add_analogy(self, trend: str, brand: str, analogy: str) -> str:
        """Add an analogy to the vector store."""
        key = f"{trend}_{brand}_{hashlib.md5(analogy.encode()).hexdigest()[:8]}"
        
        # Store analogy and metadata
        self.analogies[key] = {
            "trend": trend,
            "brand": brand,
            "analogy": analogy,
            "type": "analogy"
        }
        
        self.save_data()
        return key
    
    def find_similar_analogies(self, trend: str, brand: str, limit: int = 3) -> List[Dict]:
        """Find similar analogies for a given trend and brand."""
        if not self.analogies:
            return []
        
        # Simple keyword-based similarity for demo purposes
        query_words = set((trend + " " + brand).lower().split())
        similarities = []
        
        for key, analogy_data in self.analogies.items():
            # Calculate simple word overlap similarity
            analogy_words = set((analogy_data["trend"] + " " + analogy_data["brand"] + " " + analogy_data["analogy"]).lower().split())
            overlap = len(query_words.intersection(analogy_words))
            total_words = len(query_words.union(analogy_words))
            similarity = overlap / total_words if total_words > 0 else 0
            similarities.append((similarity, key))
        
        # Sort by similarity and return top results
        similarities.sort(reverse=True)
        
        results = []
        for similarity, key in similarities[:limit]:
            if similarity > 0:  # Only return if there's some similarity
                result = self.analogies[key].copy()
                result["similarity"] = float(similarity)
                results.append(result)
        
        return results
    
    def save_data(self):
        """Save vector data to file."""
        try:
            data = {
                "analogies": self.analogies
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving vector data: {e}")
    
    def load_data(self):
        """Load vector data from file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.analogies = data.get("analogies", {})
        except Exception as e:
            print(f"Error loading vector data: {e}")
            self.analogies = {}
    
    def get_stats(self) -> Dict:
        """Get statistics about the vector store."""
        return {
            "total_analogies": len(self.analogies),
            "unique_trends": len(set(analogy.get("trend", "") for analogy in self.analogies.values())),
            "unique_brands": len(set(analogy.get("brand", "") for analogy in self.analogies.values()))
        }

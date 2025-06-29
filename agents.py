"""
AI agent implementations for the multi-agent advertising brain app.
Each agent specializes in a specific aspect of campaign creation.
"""

import os
import json
import requests
from typing import Dict, List, Any
from google import genai
from google.genai import types
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIAgent:
    """Base class for all AI agents."""
    
    def __init__(self, name: str):
        self.name = name
        self.gemini_client = None
        self.setup_clients()
    
    def setup_clients(self):
        """Setup AI model clients."""
        try:
            gemini_key = os.getenv("GEMINI_API_KEY")
            if gemini_key:
                self.gemini_client = genai.Client(api_key=gemini_key)
        except Exception as e:
            logger.error(f"Error setting up Gemini client: {e}")
    
    def call_huggingface_api(self, prompt: str, model: str = "mistralai/Mistral-7B-Instruct-v0.1") -> str:
        """Call Hugging Face Inference API."""
        try:
            hf_token = os.getenv("HUGGINGFACE_API_TOKEN", "hf_placeholder")
            
            headers = {
                "Authorization": f"Bearer {hf_token}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 500,
                    "temperature": 0.7,
                    "top_p": 0.9
                }
            }
            
            response = requests.post(
                f"https://api-inference.huggingface.co/models/{model}",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get("generated_text", "").replace(prompt, "").strip()
                return str(result)
            else:
                logger.error(f"HuggingFace API error: {response.status_code} - {response.text}")
                return f"API Error: {response.status_code}"
                
        except Exception as e:
            logger.error(f"Error calling HuggingFace API: {e}")
            return f"Error: {str(e)}"
    
    def call_gemini_api(self, prompt: str) -> str:
        """Call Gemini API."""
        try:
            if not self.gemini_client:
                return "Gemini client not available"
            
            response = self.gemini_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            return response.text or "No response from Gemini"
            
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}")
            return f"Error: {str(e)}"

class TrendHarvester(AIAgent):
    """Agent responsible for identifying emerging micro-trends."""
    
    def __init__(self):
        super().__init__("TrendHarvester")
    
    def harvest_trends(self, query: str) -> Dict[str, Any]:
        """Harvest trends for a given topic."""
        from prompts import TREND_PROMPT
        
        prompt = TREND_PROMPT.format(query=query)
        
        # Try Gemini first, fallback to HuggingFace
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        return {
            "agent": self.name,
            "query": query,
            "trends": response,
            "status": "completed"
        }

class AnalogicalReasoner(AIAgent):
    """Agent responsible for creating brand-trend analogies."""
    
    def __init__(self, vector_store):
        super().__init__("AnalogicalReasoner")
        self.vector_store = vector_store
    
    def create_analogy(self, trend: str, brand: str) -> Dict[str, Any]:
        """Create an analogy between a trend and brand."""
        from prompts import ANALOGY_PROMPT
        
        # Check for similar analogies first
        similar = self.vector_store.find_similar_analogies(trend, brand, limit=2)
        
        prompt = ANALOGY_PROMPT.format(trend=trend, brand=brand)
        
        # Try Gemini first, fallback to HuggingFace
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        # Store the new analogy
        if "Error:" not in response:
            self.vector_store.add_analogy(trend, brand, response)
        
        return {
            "agent": self.name,
            "trend": trend,
            "brand": brand,
            "analogy": response,
            "similar_analogies": similar,
            "status": "completed"
        }

class CreativeSynthesizer(AIAgent):
    """Agent responsible for generating ad headlines and copy."""
    
    def __init__(self):
        super().__init__("CreativeSynthesizer")
    
    def synthesize_creative(self, analogy: str) -> Dict[str, Any]:
        """Generate creative content based on analogy."""
        from prompts import CREATIVE_PROMPT
        
        prompt = CREATIVE_PROMPT.format(analogy=analogy)
        
        # Try Gemini first, fallback to HuggingFace
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        return {
            "agent": self.name,
            "analogy": analogy,
            "creative_content": response,
            "status": "completed"
        }

class BudgetOptimizer(AIAgent):
    """Agent responsible for budget allocation optimization."""
    
    def __init__(self):
        super().__init__("BudgetOptimizer")
    
    def optimize_budget(self, metrics: Dict = None) -> Dict[str, Any]:
        """Optimize budget allocation across channels."""
        from prompts import BUDGET_PROMPT
        
        # Use sample metrics if none provided
        if not metrics:
            metrics = {
                "google_ctr": 3.2,
                "meta_ctr": 2.8,
                "programmatic_ctr": 1.5,
                "email_open_rate": 22.5,
                "total_budget": 10000
            }
        
        prompt = BUDGET_PROMPT
        
        # Try Gemini first, fallback to HuggingFace
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        return {
            "agent": self.name,
            "current_metrics": metrics,
            "optimization_plan": response,
            "status": "completed"
        }

class PersonalizationAgent(AIAgent):
    """Agent responsible for personalized user journey creation."""
    
    def __init__(self):
        super().__init__("PersonalizationAgent")
    
    def create_personalization(self, profile: Dict) -> Dict[str, Any]:
        """Create personalized user journey."""
        from prompts import PERSONALIZATION_PROMPT
        
        profile_json = json.dumps(profile, indent=2)
        prompt = PERSONALIZATION_PROMPT.format(profile_json=profile_json)
        
        # Try Gemini first, fallback to HuggingFace
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        return {
            "agent": self.name,
            "user_profile": profile,
            "personalization_plan": response,
            "status": "completed"
        }

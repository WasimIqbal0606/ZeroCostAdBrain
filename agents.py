
"""
AI agent implementations for the multi-agent advertising brain app.
Each agent specializes in a specific aspect of campaign creation.
"""

import os
import json
import requests
from typing import Dict, Any
import logging

# Constants
class ErrorMessages:
    PREFIX = "Error:"
    NOT_AVAILABLE = "not available"
    GEMINI_ERROR = "Gemini API error"
    MISTRAL_ERROR = "Mistral API error"
    CONFIG_ERROR = "Configuration error"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import Gemini, but handle if not available
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
    if os.getenv("GEMINI_API_KEY"):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        logger.info("Gemini API configured successfully")
    else:
        logger.warning("Gemini API key not found")
        GENAI_AVAILABLE = False
except ImportError:
    genai = None
    GENAI_AVAILABLE = False
    logger.warning("Google Generative AI package not available")

class AIAgent:
    """Base class for all AI agents."""
    
    def __init__(self, name: str):
        self.name = name
        self.gemini_model = None
        self.setup_clients()
    
    def setup_clients(self):
        """Setup AI model clients."""
        try:
            if GENAI_AVAILABLE:
                if hasattr(genai, 'GenerativeModel'):
                    self.gemini_model = genai.GenerativeModel('gemini-pro')
                    logger.info(f"Initialized Gemini model for {self.name}")
                else:
                    logger.warning("GenerativeModel not available in google.generativeai")
            else:
                logger.info("Gemini AI not available")
        except (AttributeError, ValueError) as e:
            logger.error(f"{ErrorMessages.CONFIG_ERROR} in {self.name}: {e}")
            self.gemini_model = None
    
    def call_mistral_api(self, prompt: str, model: str = "mistral-small-latest") -> str:
        """Call La Plateforme Mistral API."""
        try:
            mistral_token = os.getenv("MISTRAL_API_KEY")
            if not mistral_token:
                return "Mistral API key not available"
            
            headers = {
                "Authorization": f"Bearer {mistral_token}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            response = requests.post(
                "https://api.mistral.ai/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    return result["choices"][0]["message"]["content"]
                return str(result)
            else:
                logger.error(f"Mistral API error: {response.status_code} - {response.text}")
                return f"API Error: {response.status_code}"
                
        except Exception as e:
            logger.error(f"Error calling Mistral API: {e}")
            return f"Error: {str(e)}"

    def call_huggingface_api(self, prompt: str, model: str = "mistralai/Mistral-7B-Instruct-v0.1") -> str:
        """Call Hugging Face Inference API."""
        try:
            hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
            if not hf_token:
                return "HuggingFace API key not available"
            
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
        """Call the Gemini API with the given prompt."""
        try:
            if not self.gemini_model:
                return f"Sample {self.name} output: AI analysis would appear here with proper API key"

            response = self.gemini_model.generate_content(prompt)
            if hasattr(response, 'text'):
                return response.text
            return "No response generated"
        except (AttributeError, ValueError, RuntimeError) as e:
            logger.error(f"{ErrorMessages.GEMINI_ERROR}: {e}")
            return f"{ErrorMessages.PREFIX} {str(e)}"

class TrendHarvester(AIAgent):
    """Agent responsible for identifying emerging micro-trends."""
    
    def __init__(self):
        super().__init__("TrendHarvester")
    
    def harvest_trends(self, query: str) -> Dict[str, Any]:
        """Harvest trends for a given topic."""
        
        prompt = f"""
        You are a TrendHarvester AI. Analyze the topic '{query}' and identify trending patterns.
        
        Provide insights on:
        1. Current market trends
        2. Emerging opportunities
        3. Cultural relevance
        4. Audience engagement patterns
        
        Return a detailed analysis of trends for this topic.
        """
        
        # Try Gemini first, then Mistral, fallback to HuggingFace
        response = self.call_gemini_api(prompt)
        if "Error:" in response or "not available" in response:
            response = self.call_mistral_api(prompt)
        if "Error:" in response or "not available" in response:
            response = self.call_huggingface_api(prompt)
        
        return {
            "agent": self.name,
            "query": query,
            "trends": response,
            "status": "completed"
        }

class AnalogicalReasoner(AIAgent):
    """Agent responsible for creating brand-trend analogies."""
    
    def __init__(self, vector_store=None):
        super().__init__("AnalogicalReasoner")
        self.vector_store = vector_store
    
    def create_analogy(self, trend: str, brand: str) -> Dict[str, Any]:
        """Create an analogy between a trend and brand."""
        
        prompt = f"""
        You are an AnalogicalReasoner AI. Create a compelling analogy between:
        Trend: {trend}
        Brand: {brand}
        
        Provide a creative connection that shows how the brand aligns with this trend.
        Make it memorable and persuasive for advertising purposes.
        """
        
        # Try Gemini first, fallback to other models
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_mistral_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        # Store the analogy if vector store is available
        if self.vector_store and ErrorMessages.PREFIX not in response:
            try:
                self.vector_store.add_analogy(trend, brand, response)
            except (AttributeError, ValueError, RuntimeError) as e:
                logger.warning(f"Failed to store analogy in vector store: {e}")  # Log but continue
        
        return {
            "agent": self.name,
            "trend": trend,
            "brand": brand,
            "analogy": response,
            "status": "completed"
        }

class CreativeSynthesizer(AIAgent):
    """Agent responsible for generating ad headlines and copy."""
    
    def __init__(self):
        super().__init__("CreativeSynthesizer")
    
    def synthesize_creative(self, analogy: str) -> Dict[str, Any]:
        """Generate creative content based on analogy."""
        
        prompt = f"""
        You are a CreativeSynthesizer AI. Based on this analogy:
        {analogy}
        
        Create:
        1. 3 compelling ad headlines
        2. 2 short social media posts
        3. 1 elevator pitch
        
        Make them engaging and action-oriented.
        """
        
        # Try Gemini first, fallback to other models
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_mistral_api(prompt)
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
    
    def optimize_budget(self) -> Dict[str, Any]:
        """Optimize budget allocation across channels."""
        
        prompt = """
        You are a BudgetOptimizer AI. Recommend optimal budget allocation across:
        - Social Media Advertising (Facebook, Instagram, Twitter)
        - Search Engine Marketing (Google Ads, Bing Ads)
        - Content Marketing
        - Email Marketing
        - Influencer Partnerships
        
        Provide percentages and reasoning for each channel.
        """
        
        # Try Gemini first, fallback to other models
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_mistral_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        return {
            "agent": self.name,
            "optimization_plan": response,
            "status": "completed"
        }

class PersonalizationAgent(AIAgent):
    """Agent responsible for personalized user journey creation."""
    
    def __init__(self):
        super().__init__("PersonalizationAgent")
    
    def create_personalization(self, profile: Dict) -> Dict[str, Any]:
        """Create personalized user journey."""
        
        profile_json = json.dumps(profile, indent=2)
        prompt = f"""
        You are a PersonalizationAgent AI. Based on this user profile:
        {profile_json}
        
        Create a personalized marketing journey including:
        1. Recommended touchpoints
        2. Content preferences
        3. Optimal timing
        4. Channel priorities
        
        Tailor the approach to this specific audience.
        """
        
        # Try Gemini first, fallback to other models
        response = self.call_gemini_api(prompt)
        if "Error:" in response:
            response = self.call_mistral_api(prompt)
        if "Error:" in response:
            response = self.call_huggingface_api(prompt)
        
        return {
            "agent": self.name,
            "user_profile": profile,
            "personalization_plan": response,
            "status": "completed"
        }

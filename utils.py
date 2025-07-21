
"""
Utility functions for the Neural AdBrain platform.
Includes campaign management, data processing, and helper functions.
"""

import json
import csv
import os
import uuid
from typing import Dict, List, Any, Optional
from datetime import datetime
import pandas as pd

class CampaignManager:
    """Manages campaign data storage and retrieval."""
    
    def __init__(self, storage_file: str = "campaigns.json"):
        self.storage_file = storage_file
        self.campaigns = self._load_campaigns()
    
    def _load_campaigns(self) -> Dict:
        """Load campaigns from storage file."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading campaigns: {e}")
            return {}
    
    def save_campaigns(self) -> bool:
        """Save campaigns to storage file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.campaigns, f, indent=2, default=str)
            return True
        except Exception as e:
            print(f"Error saving campaigns: {e}")
            return False
    
    def save_campaign(self, campaign_data: Dict) -> str:
        """Save a new campaign and return its ID."""
        campaign_id = str(uuid.uuid4())
        campaign_data['id'] = campaign_id
        campaign_data['created_at'] = datetime.now().isoformat()
        
        self.campaigns[campaign_id] = campaign_data
        self.save_campaigns()
        
        return campaign_id
    
    def get_campaign(self, campaign_id: str) -> Optional[Dict]:
        """Get a specific campaign by ID."""
        return self.campaigns.get(campaign_id)
    
    def list_campaigns(self) -> List[Dict]:
        """List all campaigns."""
        return list(self.campaigns.values())
    
    def delete_campaign(self, campaign_id: str) -> bool:
        """Delete a campaign by ID."""
        if campaign_id in self.campaigns:
            del self.campaigns[campaign_id]
            self.save_campaigns()
            return True
        return False

def export_campaign_to_csv(campaign_data: Dict, filename: Optional[str] = None) -> str:
    """Export campaign data to CSV file."""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"campaign_export_{timestamp}.csv"
    
    try:
        # Flatten campaign data for CSV export
        flattened_data = []
        
        # Basic campaign info
        basic_info = {
            'campaign_id': campaign_data.get('id', 'Unknown'),
            'topic': campaign_data.get('topic', 'Unknown'),
            'brand': campaign_data.get('brand', 'Unknown'),
            'budget': campaign_data.get('budget', 0),
            'created_at': campaign_data.get('created_at', 'Unknown')
        }
        
        # Agent results
        results = campaign_data.get('results', {})
        for agent_name, agent_result in results.items():
            row = basic_info.copy()
            row['agent'] = agent_name
            row['result'] = str(agent_result)
            flattened_data.append(row)
        
        # Create DataFrame and export
        df = pd.DataFrame(flattened_data)
        df.to_csv(filename, index=False)
        
        return filename
        
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        return ""

def create_sample_user_profile() -> Dict[str, Any]:
    """Create a sample user profile for testing."""
    return {
        "demographics": {
            "age_range": "25-34",
            "income": "$50k-$75k",
            "education": "Bachelor's degree",
            "location": "Urban"
        },
        "interests": [
            "Technology",
            "Sustainability", 
            "Health & Wellness",
            "Professional Development"
        ],
        "behavior": {
            "shopping_preference": "Online research, in-store purchase",
            "social_media_usage": "High",
            "brand_loyalty": "Medium",
            "early_adopter": True
        },
        "preferences": {
            "content_format": ["Video", "Infographics", "Articles"],
            "communication_style": "Professional but approachable",
            "contact_frequency": "Weekly"
        }
    }

def format_agent_response(response: str, agent_name: str) -> str:
    """Format agent response for display."""
    if not response:
        return f"No response from {agent_name}"
    
    # Add agent branding
    formatted = f"**{agent_name} Analysis:**\n\n"
    formatted += response
    
    return formatted

def create_budget_chart_data(optimization_plan: str) -> Dict[str, float]:
    """Extract budget allocation data from optimization plan."""
    # Default budget allocation if parsing fails
    default_allocation = {
        "Social Media": 35.0,
        "Search Ads": 25.0,
        "Content Marketing": 20.0,
        "Email Marketing": 12.0,
        "Influencer Marketing": 8.0
    }
    
    try:
        # Try to parse percentages from the optimization plan
        # This is a simplified parser - in production, use more robust parsing
        allocation = {}
        lines = optimization_plan.split('\n')
        
        for line in lines:
            if '%' in line:
                # Extract channel name and percentage
                parts = line.split(':')
                if len(parts) >= 2:
                    channel = parts[0].strip()
                    percentage_part = parts[1].strip()
                    
                    # Extract number before %
                    for char in percentage_part:
                        if char.isdigit() or char == '.':
                            continue
                        else:
                            percentage_str = percentage_part[:percentage_part.index(char)]
                            break
                    else:
                        percentage_str = percentage_part.replace('%', '')
                    
                    try:
                        percentage = float(percentage_str)
                        allocation[channel] = percentage
                    except ValueError:
                        continue
        
        # Return parsed allocation if valid, otherwise default
        if allocation and sum(allocation.values()) > 0:
            return allocation
        else:
            return default_allocation
            
    except Exception as e:
        print(f"Error parsing budget allocation: {e}")
        return default_allocation

def validate_api_keys() -> Dict[str, bool]:
    """Validate that required API keys are available."""
    required_keys = {
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
        "MISTRAL_API_KEY": os.getenv("MISTRAL_API_KEY"),
        "HUGGINGFACE_API_TOKEN": os.getenv("HUGGINGFACE_API_TOKEN")
    }
    
    return {key: bool(value) for key, value in required_keys.items()}

def clean_text_for_analysis(text: str) -> str:
    """Clean text for AI analysis."""
    if not text:
        return ""
    
    # Remove extra whitespace
    cleaned = ' '.join(text.split())
    
    # Limit length for API calls
    max_length = 2000
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length] + "..."
    
    return cleaned

def calculate_engagement_score(metrics: Dict) -> float:
    """Calculate overall engagement score from metrics."""
    try:
        likes = metrics.get('likes', 0)
        shares = metrics.get('shares', 0)
        comments = metrics.get('comments', 0)
        views = metrics.get('views', 1)  # Avoid division by zero
        
        # Calculate engagement rate
        total_engagement = likes + shares + comments
        engagement_rate = (total_engagement / views) * 100
        
        # Normalize to 0-10 scale
        normalized_score = min(engagement_rate / 10, 10.0)
        
        return round(normalized_score, 2)
        
    except Exception as e:
        print(f"Error calculating engagement score: {e}")
        return 5.0  # Default neutral score

def generate_campaign_summary(campaign_data: Dict) -> str:
    """Generate a text summary of campaign results."""
    try:
        topic = campaign_data.get('topic', 'Unknown')
        brand = campaign_data.get('brand', 'Unknown')
        budget = campaign_data.get('budget', 0)
        
        results = campaign_data.get('results', {})
        agent_count = len(results)
        
        summary = f"""
Campaign Summary:
================
Brand: {brand}
Topic: {topic}
Budget: ${budget:,}
Agents Executed: {agent_count}
Created: {campaign_data.get('created_at', 'Unknown')}

Results Overview:
- Trend Analysis: {'✓' if 'trend_harvester' in results else '✗'}
- Brand Analogies: {'✓' if 'analogical_reasoner' in results else '✗'}
- Creative Content: {'✓' if 'creative_synthesizer' in results else '✗'}
- Budget Optimization: {'✓' if 'budget_optimizer' in results else '✗'}
- Personalization: {'✓' if 'personalization_agent' in results else '✗'}
        """
        
        return summary.strip()
        
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Error generating campaign summary"

def format_currency(amount: float) -> str:
    """Format currency values for display."""
    if amount >= 1000000:
        return f"${amount/1000000:.1f}M"
    elif amount >= 1000:
        return f"${amount/1000:.1f}K"
    else:
        return f"${amount:.0f}"

def calculate_roi_prediction(budget: float, metrics: Dict) -> float:
    """Calculate ROI prediction based on budget and metrics."""
    try:
        # Simple ROI calculation based on industry averages
        base_roi = 150  # 150% baseline ROI
        
        # Adjust based on budget efficiency
        if budget > 50000:
            budget_multiplier = 1.2
        elif budget > 10000:
            budget_multiplier = 1.1
        else:
            budget_multiplier = 1.0
        
        # Adjust based on engagement metrics
        engagement_score = calculate_engagement_score(metrics)
        engagement_multiplier = 1 + (engagement_score / 50)  # Max 20% boost
        
        predicted_roi = base_roi * budget_multiplier * engagement_multiplier
        
        return round(predicted_roi, 1)
        
    except Exception as e:
        print(f"Error calculating ROI prediction: {e}")
        return 150.0  # Default baseline

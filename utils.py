"""
Utility functions for the multi-agent advertising brain app.
Includes data management, export functionality, and helper functions.
"""

import json
import os
import csv
import pandas as pd
from datetime import datetime
from typing import Dict, List, Any
import streamlit as st
from database import DatabaseManager

class CampaignManager:
    """Manages campaign data storage and retrieval with PostgreSQL."""
    
    def __init__(self):
        self.db = DatabaseManager()
        # Keep legacy file support as fallback
        self.campaigns_file = "campaigns.json"
    
    def save_campaign(self, campaign_data: Dict) -> str:
        """Save a new campaign to PostgreSQL database."""
        # Add timestamp and ID if not present
        if 'id' not in campaign_data:
            campaign_data['id'] = f"campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        if 'created_at' not in campaign_data:
            campaign_data['created_at'] = datetime.now().isoformat()
        
        # Save to database
        campaign_id = self.db.save_campaign(campaign_data)
        
        # Fallback to file if database fails
        if not campaign_id:
            return self._save_campaign_to_file(campaign_data)
        
        return campaign_id
    
    def get_campaign(self, campaign_id: str) -> Dict:
        """Get a specific campaign from database."""
        campaign = self.db.get_campaign(campaign_id)
        if campaign:
            return campaign
        
        # Fallback to file
        return self._get_campaign_from_file(campaign_id)
    
    def list_campaigns(self) -> List[Dict]:
        """List all campaigns from database."""
        campaigns = self.db.list_campaigns()
        if campaigns:
            return campaigns
        
        # Fallback to file
        return self._list_campaigns_from_file()
    
    def delete_campaign(self, campaign_id: str) -> bool:
        """Delete a campaign from database."""
        success = self.db.delete_campaign(campaign_id)
        if success:
            return True
        
        # Fallback to file
        return self._delete_campaign_from_file(campaign_id)
    
    def _save_campaign_to_file(self, campaign_data: Dict) -> str:
        """Fallback file storage."""
        try:
            campaigns = self._load_campaigns_from_file()
            campaign_id = campaign_data['id']
            campaigns[campaign_id] = campaign_data
            
            with open(self.campaigns_file, 'w') as f:
                json.dump(campaigns, f, indent=2, default=str)
            
            return campaign_id
        except Exception as e:
            st.error(f"Error saving to file: {e}")
            return ""
    
    def _load_campaigns_from_file(self) -> Dict:
        """Load campaigns from file."""
        try:
            if os.path.exists(self.campaigns_file):
                with open(self.campaigns_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            st.error(f"Error loading campaigns: {e}")
        return {}
    
    def _get_campaign_from_file(self, campaign_id: str) -> Dict:
        """Get campaign from file."""
        campaigns = self._load_campaigns_from_file()
        return campaigns.get(campaign_id, {})
    
    def _list_campaigns_from_file(self) -> List[Dict]:
        """List campaigns from file."""
        campaigns = self._load_campaigns_from_file()
        return list(campaigns.values())
    
    def _delete_campaign_from_file(self, campaign_id: str) -> bool:
        """Delete campaign from file."""
        try:
            campaigns = self._load_campaigns_from_file()
            if campaign_id in campaigns:
                del campaigns[campaign_id]
                with open(self.campaigns_file, 'w') as f:
                    json.dump(campaigns, f, indent=2, default=str)
                return True
        except Exception as e:
            st.error(f"Error deleting from file: {e}")
        return False

def export_campaign_to_csv(campaign_data: Dict) -> str:
    """Export campaign data to CSV format."""
    try:
        # Flatten the campaign data for CSV export
        flattened_data = []
        
        # Basic campaign info
        basic_info = {
            'Campaign ID': campaign_data.get('id', ''),
            'Topic': campaign_data.get('topic', ''),
            'Brand': campaign_data.get('brand', ''),
            'Created At': campaign_data.get('created_at', '')
        }
        
        # Add agent results
        results = campaign_data.get('results', {})
        for agent_name, agent_data in results.items():
            if isinstance(agent_data, dict):
                for key, value in agent_data.items():
                    if isinstance(value, (str, int, float)):
                        basic_info[f"{agent_name}_{key}"] = value
        
        flattened_data.append(basic_info)
        
        # Convert to DataFrame and then CSV
        df = pd.DataFrame(flattened_data)
        csv_filename = f"campaign_{campaign_data.get('id', 'export')}.csv"
        df.to_csv(csv_filename, index=False)
        
        return csv_filename
        
    except Exception as e:
        st.error(f"Error exporting to CSV: {e}")
        return ""

def create_sample_user_profile() -> Dict:
    """Create a sample user profile for testing."""
    return {
        "demographics": {
            "age_range": "25-34",
            "gender": "Non-binary",
            "income": "$50,000-$75,000",
            "location": "Urban area"
        },
        "interests": [
            "Sustainable living",
            "Technology",
            "Fitness",
            "Travel"
        ],
        "behavior": {
            "online_shopping_frequency": "Weekly",
            "social_media_usage": "High",
            "preferred_content_type": "Video",
            "device_preference": "Mobile"
        },
        "purchase_history": {
            "last_purchase": "Eco-friendly water bottle",
            "average_order_value": "$45",
            "favorite_brands": ["Patagonia", "Apple", "Nike"]
        }
    }

def format_agent_response(response: str, agent_name: str) -> str:
    """Format agent response for better display."""
    if not response or "Error:" in response:
        return f"❌ {agent_name} encountered an error: {response}"
    
    # Add agent-specific formatting
    if agent_name == "TrendHarvester":
        return f"🔍 **Trend Analysis:**\n{response}"
    elif agent_name == "AnalogicalReasoner":
        return f"🧠 **Brand Analogy:**\n{response}"
    elif agent_name == "CreativeSynthesizer":
        return f"✨ **Creative Content:**\n{response}"
    elif agent_name == "BudgetOptimizer":
        return f"💰 **Budget Optimization:**\n{response}"
    elif agent_name == "PersonalizationAgent":
        return f"👤 **Personalization Plan:**\n{response}"
    
    return response

def create_budget_chart_data(budget_response: str) -> Dict:
    """Extract budget allocation data for chart display."""
    # Default allocation
    default_data = {
        "Google Ads": 40,
        "Meta/Facebook": 30,
        "Programmatic": 20,
        "Email": 10
    }
    
    try:
        # Try to extract percentages from the response
        import re
        
        # Look for percentage patterns
        google_match = re.search(r'Google[^:]*:?\s*(\d+)%', budget_response, re.IGNORECASE)
        meta_match = re.search(r'(?:Meta|Facebook)[^:]*:?\s*(\d+)%', budget_response, re.IGNORECASE)
        prog_match = re.search(r'Programmatic[^:]*:?\s*(\d+)%', budget_response, re.IGNORECASE)
        email_match = re.search(r'Email[^:]*:?\s*(\d+)%', budget_response, re.IGNORECASE)
        
        if google_match or meta_match or prog_match or email_match:
            extracted_data = {}
            if google_match:
                extracted_data["Google Ads"] = int(google_match.group(1))
            if meta_match:
                extracted_data["Meta/Facebook"] = int(meta_match.group(1))
            if prog_match:
                extracted_data["Programmatic"] = int(prog_match.group(1))
            if email_match:
                extracted_data["Email"] = int(email_match.group(1))
            
            # Fill in missing values with defaults
            for key in default_data:
                if key not in extracted_data:
                    extracted_data[key] = default_data[key]
            
            return extracted_data
    
    except Exception as e:
        st.warning(f"Could not parse budget data: {e}")
    
    return default_data

def validate_api_keys() -> Dict[str, bool]:
    """Validate that required API keys are available."""
    return {
        "GEMINI_API_KEY": bool(os.getenv("GEMINI_API_KEY")),
        "MISTRAL_API_KEY": bool(os.getenv("MISTRAL_API_KEY")),
        "HUGGINGFACE_API_TOKEN": bool(os.getenv("HUGGINGFACE_API_TOKEN"))
    }

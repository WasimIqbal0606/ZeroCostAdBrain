"""
Database management for the Neural AdBrain platform.
Handles campaign storage and retrieval with PostgreSQL.
"""

import os
import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Try to import psycopg2, but handle if not available
try:
    import psycopg2
    from psycopg2.extras import RealDictCursor, Json
    POSTGRES_AVAILABLE = True
except ImportError:
    logger.warning("PostgreSQL not available, using file-based storage")
    POSTGRES_AVAILABLE = False

class DatabaseManager:
    """Database manager with PostgreSQL and file-based fallback."""

    def __init__(self):
        self.use_postgres = POSTGRES_AVAILABLE and self._check_postgres_connection()
        self.file_storage = "campaigns_db.json"

        if self.use_postgres:
            self._initialize_postgres()
        else:
            logger.info("Using file-based storage")

    def _check_postgres_connection(self) -> bool:
        """Check if PostgreSQL is available and accessible."""
        try:
            database_url = os.environ.get('DATABASE_URL')
            if not database_url:
                return False

            conn = psycopg2.connect(database_url)
            conn.close()
            return True

        except Exception as e:
            logger.warning(f"PostgreSQL not accessible: {e}")
            return False

    def _initialize_postgres(self):
        """Initialize PostgreSQL tables."""
        try:
            database_url = os.environ.get('DATABASE_URL')
            conn = psycopg2.connect(database_url)
            cursor = conn.cursor()

            # Create campaigns table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS campaigns (
                    id VARCHAR(255) PRIMARY KEY,
                    topic VARCHAR(255) NOT NULL,
                    brand VARCHAR(255) NOT NULL,
                    budget DECIMAL(10, 2),
                    market_region VARCHAR(100),
                    user_profile JSONB,
                    results JSONB,
                    execution_metadata JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conn.commit()
            cursor.close()
            conn.close()

            logger.info("PostgreSQL tables initialized")

        except Exception as e:
            logger.error(f"Error initializing PostgreSQL: {e}")
            self.use_postgres = False

    def save_campaign(self, campaign_data: Dict) -> str:
        """Save campaign data."""
        campaign_id = str(uuid.uuid4())
        campaign_data['id'] = campaign_id
        campaign_data['created_at'] = datetime.now().isoformat()

        if self.use_postgres:
            return self._save_campaign_postgres(campaign_data)
        else:
            return self._save_campaign_file(campaign_data)

    def _save_campaign_postgres(self, campaign_data: Dict) -> str:
        """Save campaign to PostgreSQL."""
        try:
            database_url = os.environ.get('DATABASE_URL')
            conn = psycopg2.connect(database_url)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO campaigns (
                    id, topic, brand, budget, market_region, 
                    user_profile, results, execution_metadata
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                campaign_data['id'],
                campaign_data.get('topic', ''),
                campaign_data.get('brand', ''),
                campaign_data.get('budget', 0),
                campaign_data.get('market_region', ''),
                Json(campaign_data.get('user_profile', {})),
                Json(campaign_data.get('results', {})),
                Json(campaign_data.get('execution_metadata', {}))
            ))

            conn.commit()
            cursor.close()
            conn.close()

            logger.info(f"Campaign saved to PostgreSQL: {campaign_data['id']}")
            return campaign_data['id']

        except Exception as e:
            logger.error(f"Error saving to PostgreSQL: {e}")
            # Fallback to file storage
            return self._save_campaign_file(campaign_data)

    def _save_campaign_file(self, campaign_data: Dict) -> str:
        """Save campaign to file."""
        try:
            # Load existing campaigns
            campaigns = {}
            if os.path.exists(self.file_storage):
                with open(self.file_storage, 'r') as f:
                    campaigns = json.load(f)

            # Add new campaign
            campaigns[campaign_data['id']] = campaign_data

            # Save back to file
            with open(self.file_storage, 'w') as f:
                json.dump(campaigns, f, indent=2, default=str)

            logger.info(f"Campaign saved to file: {campaign_data['id']}")
            return campaign_data['id']

        except Exception as e:
            logger.error(f"Error saving to file: {e}")
            return ""

    def get_campaign(self, campaign_id: str) -> Optional[Dict]:
        """Get campaign by ID."""
        if self.use_postgres:
            return self._get_campaign_postgres(campaign_id)
        else:
            return self._get_campaign_file(campaign_id)

    def _get_campaign_postgres(self, campaign_id: str) -> Optional[Dict]:
        """Get campaign from PostgreSQL."""
        try:
            database_url = os.environ.get('DATABASE_URL')
            conn = psycopg2.connect(database_url)
            cursor = conn.cursor(cursor_factory=RealDictCursor)

            cursor.execute("SELECT * FROM campaigns WHERE id = %s", (campaign_id,))
            result = cursor.fetchone()

            cursor.close()
            conn.close()

            return dict(result) if result else None

        except Exception as e:
            logger.error(f"Error getting campaign from PostgreSQL: {e}")
            return self._get_campaign_file(campaign_id)

    def _get_campaign_file(self, campaign_id: str) -> Optional[Dict]:
        """Get campaign from file."""
        try:
            if os.path.exists(self.file_storage):
                with open(self.file_storage, 'r') as f:
                    campaigns = json.load(f)
                return campaigns.get(campaign_id)
            return None

        except Exception as e:
            logger.error(f"Error getting campaign from file: {e}")
            return None

    def list_campaigns(self, limit: int = 50) -> List[Dict]:
        """List all campaigns."""
        if self.use_postgres:
            return self._list_campaigns_postgres(limit)
        else:
            return self._list_campaigns_file(limit)

    def _list_campaigns_postgres(self, limit: int) -> List[Dict]:
        """List campaigns from PostgreSQL."""
        try:
            database_url = os.environ.get('DATABASE_URL')
            conn = psycopg2.connect(database_url)
            cursor = conn.cursor(cursor_factory=RealDictCursor)

            cursor.execute(
                "SELECT * FROM campaigns ORDER BY created_at DESC LIMIT %s", 
                (limit,)
            )
            results = cursor.fetchall()

            cursor.close()
            conn.close()

            return [dict(result) for result in results]

        except Exception as e:
            logger.error(f"Error listing campaigns from PostgreSQL: {e}")
            return self._list_campaigns_file(limit)

    def _list_campaigns_file(self, limit: int) -> List[Dict]:
        """List campaigns from file."""
        try:
            if os.path.exists(self.file_storage):
                with open(self.file_storage, 'r') as f:
                    campaigns = json.load(f)

                # Sort by created_at and limit
                campaign_list = list(campaigns.values())
                campaign_list.sort(
                    key=lambda x: x.get('created_at', ''), 
                    reverse=True
                )

                return campaign_list[:limit]

            return []

        except Exception as e:
            logger.error(f"Error listing campaigns from file: {e}")
            return []

    def delete_campaign(self, campaign_id: str) -> bool:
        """Delete campaign by ID."""
        if self.use_postgres:
            return self._delete_campaign_postgres(campaign_id)
        else:
            return self._delete_campaign_file(campaign_id)

    def _delete_campaign_postgres(self, campaign_id: str) -> bool:
        """Delete campaign from PostgreSQL."""
        try:
            database_url = os.environ.get('DATABASE_URL')
            conn = psycopg2.connect(database_url)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM campaigns WHERE id = %s", (campaign_id,))
            deleted = cursor.rowcount > 0

            conn.commit()
            cursor.close()
            conn.close()

            return deleted

        except Exception as e:
            logger.error(f"Error deleting campaign from PostgreSQL: {e}")
            return self._delete_campaign_file(campaign_id)

    def _delete_campaign_file(self, campaign_id: str) -> bool:
        """Delete campaign from file."""
        try:
            if os.path.exists(self.file_storage):
                with open(self.file_storage, 'r') as f:
                    campaigns = json.load(f)

                if campaign_id in campaigns:
                    del campaigns[campaign_id]

                    with open(self.file_storage, 'w') as f:
                        json.dump(campaigns, f, indent=2, default=str)

                    return True

            return False

        except Exception as e:
            logger.error(f"Error deleting campaign from file: {e}")
            return False
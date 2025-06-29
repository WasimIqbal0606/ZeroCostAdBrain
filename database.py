"""
PostgreSQL database integration for Neural AdBrain platform.
Enterprise-grade data persistence with SQLAlchemy ORM.
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from sqlalchemy import create_engine, Column, String, Text, DateTime, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

logger = logging.getLogger(__name__)

Base = declarative_base()

class Campaign(Base):
    """Campaign data model."""
    __tablename__ = 'campaigns'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    topic = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    budget = Column(Float)
    market_region = Column(String)
    trend_depth = Column(String)
    creativity_level = Column(String)
    include_live_data = Column(Boolean, default=False)
    user_profile = Column(JSONB)
    results = Column(JSONB)
    execution_metadata = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String, default='active')

class WorkflowExecution(Base):
    """Workflow execution tracking."""
    __tablename__ = 'workflow_executions'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    campaign_id = Column(String)
    workflow_id = Column(String)
    execution_data = Column(JSONB)
    status = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    execution_time_seconds = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Analogy(Base):
    """Vector analogies storage."""
    __tablename__ = 'analogies'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    trend = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    analogy = Column(Text, nullable=False)
    embedding_vector = Column(JSONB)  # Store as JSON array
    similarity_score = Column(Float)
    campaign_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class LiveDataSnapshot(Base):
    """Live market data snapshots."""
    __tablename__ = 'live_data_snapshots'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    topic = Column(String, nullable=False)
    data_source = Column(String, nullable=False)  # reddit, github, news, crypto
    raw_data = Column(JSONB)
    trend_signals = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)

class DatabaseManager:
    """PostgreSQL database manager for Neural AdBrain platform."""
    
    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        self._initialize_database()
    
    def _initialize_database(self):
        """Initialize database connection and create tables."""
        try:
            database_url = os.getenv('DATABASE_URL')
            if not database_url:
                logger.error("DATABASE_URL not found in environment variables")
                return
            
            self.engine = create_engine(
                database_url,
                pool_size=10,
                max_overflow=20,
                pool_pre_ping=True,
                echo=False  # Set to True for SQL debugging
            )
            
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            
            # Create all tables
            Base.metadata.create_all(bind=self.engine)
            logger.info("Database initialized successfully")
            
        except Exception as e:
            logger.error(f"Database initialization error: {e}")
            self.engine = None
            self.SessionLocal = None
    
    def get_session(self) -> Optional[Session]:
        """Get database session."""
        if not self.SessionLocal:
            return None
        return self.SessionLocal()
    
    def save_campaign(self, campaign_data: Dict) -> str:
        """Save campaign to database."""
        if not self.SessionLocal:
            logger.error("Database not available")
            return ""
        
        session = self.get_session()
        try:
            campaign = Campaign(
                id=campaign_data.get('id', str(uuid.uuid4())),
                topic=campaign_data.get('topic', ''),
                brand=campaign_data.get('brand', ''),
                budget=campaign_data.get('budget', 0),
                market_region=campaign_data.get('market_region', ''),
                trend_depth=campaign_data.get('trend_depth', ''),
                creativity_level=campaign_data.get('creativity_level', ''),
                include_live_data=campaign_data.get('include_live_data', False),
                user_profile=campaign_data.get('user_profile', {}),
                results=campaign_data.get('results', {}),
                execution_metadata=campaign_data.get('execution_metadata', {})
            )
            
            session.add(campaign)
            session.commit()
            
            logger.info(f"Campaign saved: {campaign.id}")
            return campaign.id
            
        except Exception as e:
            session.rollback()
            logger.error(f"Error saving campaign: {e}")
            return ""
        finally:
            session.close()
    
    def get_campaign(self, campaign_id: str) -> Optional[Dict]:
        """Get campaign by ID."""
        if not self.SessionLocal:
            return None
        
        session = self.get_session()
        try:
            campaign = session.query(Campaign).filter(Campaign.id == campaign_id).first()
            if campaign:
                return {
                    'id': campaign.id,
                    'topic': campaign.topic,
                    'brand': campaign.brand,
                    'budget': campaign.budget,
                    'market_region': campaign.market_region,
                    'trend_depth': campaign.trend_depth,
                    'creativity_level': campaign.creativity_level,
                    'include_live_data': campaign.include_live_data,
                    'user_profile': campaign.user_profile,
                    'results': campaign.results,
                    'execution_metadata': campaign.execution_metadata,
                    'created_at': campaign.created_at.isoformat() if campaign.created_at else None,
                    'updated_at': campaign.updated_at.isoformat() if campaign.updated_at else None,
                    'status': campaign.status
                }
            return None
            
        except Exception as e:
            logger.error(f"Error getting campaign: {e}")
            return None
        finally:
            session.close()
    
    def list_campaigns(self, limit: int = 50) -> List[Dict]:
        """List all campaigns."""
        if not self.SessionLocal:
            return []
        
        session = self.get_session()
        try:
            campaigns = session.query(Campaign).order_by(Campaign.created_at.desc()).limit(limit).all()
            
            result = []
            for campaign in campaigns:
                result.append({
                    'id': campaign.id,
                    'topic': campaign.topic,
                    'brand': campaign.brand,
                    'budget': campaign.budget,
                    'market_region': campaign.market_region,
                    'created_at': campaign.created_at.isoformat() if campaign.created_at else None,
                    'status': campaign.status
                })
            
            return result
            
        except Exception as e:
            logger.error(f"Error listing campaigns: {e}")
            return []
        finally:
            session.close()
    
    def delete_campaign(self, campaign_id: str) -> bool:
        """Delete campaign by ID."""
        if not self.SessionLocal:
            return False
        
        session = self.get_session()
        try:
            campaign = session.query(Campaign).filter(Campaign.id == campaign_id).first()
            if campaign:
                session.delete(campaign)
                session.commit()
                logger.info(f"Campaign deleted: {campaign_id}")
                return True
            return False
            
        except Exception as e:
            session.rollback()
            logger.error(f"Error deleting campaign: {e}")
            return False
        finally:
            session.close()
    
    def save_analogy(self, trend: str, brand: str, analogy: str, embedding_vector: List[float] = None, campaign_id: str = None) -> str:
        """Save analogy to database."""
        if not self.SessionLocal:
            return ""
        
        session = self.get_session()
        try:
            analogy_record = Analogy(
                trend=trend,
                brand=brand,
                analogy=analogy,
                embedding_vector=embedding_vector or [],
                campaign_id=campaign_id
            )
            
            session.add(analogy_record)
            session.commit()
            
            logger.info(f"Analogy saved: {analogy_record.id}")
            return analogy_record.id
            
        except Exception as e:
            session.rollback()
            logger.error(f"Error saving analogy: {e}")
            return ""
        finally:
            session.close()
    
    def find_similar_analogies(self, trend: str, brand: str, limit: int = 3) -> List[Dict]:
        """Find similar analogies using database search."""
        if not self.SessionLocal:
            return []
        
        session = self.get_session()
        try:
            # Simple text-based similarity for now
            analogies = session.query(Analogy).filter(
                Analogy.trend.ilike(f'%{trend}%') | 
                Analogy.brand.ilike(f'%{brand}%')
            ).limit(limit).all()
            
            result = []
            for analogy in analogies:
                result.append({
                    'id': analogy.id,
                    'trend': analogy.trend,
                    'brand': analogy.brand,
                    'analogy': analogy.analogy,
                    'similarity': analogy.similarity_score or 0.8,  # Default similarity
                    'created_at': analogy.created_at.isoformat() if analogy.created_at else None
                })
            
            return result
            
        except Exception as e:
            logger.error(f"Error finding similar analogies: {e}")
            return []
        finally:
            session.close()
    
    def save_workflow_execution(self, execution_data: Dict) -> str:
        """Save workflow execution record."""
        if not self.SessionLocal:
            return ""
        
        session = self.get_session()
        try:
            execution = WorkflowExecution(
                campaign_id=execution_data.get('campaign_id'),
                workflow_id=execution_data.get('workflow_id'),
                execution_data=execution_data.get('execution_data', {}),
                status=execution_data.get('status', 'completed'),
                start_time=datetime.fromisoformat(execution_data.get('start_time', datetime.now().isoformat())),
                end_time=datetime.fromisoformat(execution_data.get('end_time', datetime.now().isoformat())),
                execution_time_seconds=execution_data.get('execution_time_seconds', 0)
            )
            
            session.add(execution)
            session.commit()
            
            logger.info(f"Workflow execution saved: {execution.id}")
            return execution.id
            
        except Exception as e:
            session.rollback()
            logger.error(f"Error saving workflow execution: {e}")
            return ""
        finally:
            session.close()
    
    def save_live_data_snapshot(self, topic: str, data_source: str, raw_data: Dict, trend_signals: Dict = None) -> str:
        """Save live data snapshot."""
        if not self.SessionLocal:
            return ""
        
        session = self.get_session()
        try:
            snapshot = LiveDataSnapshot(
                topic=topic,
                data_source=data_source,
                raw_data=raw_data,
                trend_signals=trend_signals or {}
            )
            
            session.add(snapshot)
            session.commit()
            
            logger.info(f"Live data snapshot saved: {snapshot.id}")
            return snapshot.id
            
        except Exception as e:
            session.rollback()
            logger.error(f"Error saving live data snapshot: {e}")
            return ""
        finally:
            session.close()
    
    def get_database_stats(self) -> Dict:
        """Get database statistics."""
        if not self.SessionLocal:
            return {'error': 'Database not available'}
        
        session = self.get_session()
        try:
            stats = {
                'total_campaigns': session.query(Campaign).count(),
                'total_analogies': session.query(Analogy).count(),
                'total_workflow_executions': session.query(WorkflowExecution).count(),
                'total_live_data_snapshots': session.query(LiveDataSnapshot).count(),
                'recent_campaigns': session.query(Campaign).filter(
                    Campaign.created_at > datetime.now().replace(hour=0, minute=0, second=0)
                ).count()
            }
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting database stats: {e}")
            return {'error': str(e)}
        finally:
            session.close()
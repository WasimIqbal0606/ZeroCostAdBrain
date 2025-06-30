# Neural AdBrain Platform Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [AI Agent System](#ai-agent-system)
4. [API Integration](#api-integration)
5. [Database Schema](#database-schema)
6. [User Interface](#user-interface)
7. [Workflow Execution](#workflow-execution)
8. [Analytics & Reporting](#analytics--reporting)
9. [Installation & Setup](#installation--setup)
10. [Configuration](#configuration)
11. [Troubleshooting](#troubleshooting)

## System Overview

Neural AdBrain is an enterprise-grade advertising intelligence platform that leverages multiple specialized AI agents to create, optimize, and analyze marketing campaigns. The platform combines real-time market data, neural network processing, and advanced AI models to deliver comprehensive campaign solutions.

### Key Features
- **6 Specialized AI Agents**: MemeHarvester, NarrativeAligner, CopyCrafter, HookOptimizer, SequencePlanner, AnalyticsInterpreter
- **Real-time Data Integration**: Live social media trends, market sentiment, cryptocurrency indicators
- **Multi-modal Analytics**: Campaign performance tracking, budget optimization, viral potential scoring
- **Zero-cost Architecture**: Free API integrations for core functionality
- **Enterprise Storage**: PostgreSQL with vector similarity search

### Technology Stack
- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python 3.x with specialized agent modules
- **AI Models**: Google Gemini 2.5 Flash, Mistral AI, Hugging Face transformers
- **Database**: PostgreSQL with JSONB support
- **Vector Store**: Qdrant in-memory database
- **Real-time APIs**: Reddit JSON feeds, CoinDesk crypto API, RSS news feeds

## Architecture

### High-Level System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Interface │    │  Agent Executor │    │  Data Sources   │
│   (Streamlit)   │───▶│  (LangGraph)    │───▶│  (APIs/Feeds)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Session State  │    │  Vector Store   │    │   PostgreSQL    │
│   Management    │    │   (Qdrant)      │    │   Database      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Breakdown

#### 1. Frontend Layer (app.py)
- **Neural Command Center**: Main navigation hub with module selection
- **Campaign Studio**: Form-based campaign parameter input
- **AI Agents**: Agent execution interface with real-time progress tracking
- **Analytics Center**: Comprehensive results display and performance metrics
- **Enterprise Hub**: Partnership and business intelligence sections

#### 2. Agent Layer (specialized_agents.py)
- **MemeHarvester**: Analyzes trending phrases and viral content patterns
- **NarrativeAligner**: Creates compelling brand story hooks aligned with trends
- **CopyCrafter**: Generates headlines, ad copy, and video scripts
- **HookOptimizer**: Ranks content by viral potential and engagement probability
- **SequencePlanner**: Designs email marketing sequences and automation triggers
- **AnalyticsInterpreter**: Provides performance insights and optimization recommendations

#### 3. Data Layer
- **PostgreSQL**: Campaign persistence, execution metadata, user profiles
- **Qdrant Vector Store**: Analogical reasoning, semantic similarity search
- **Session State**: Real-time workflow data, temporary results storage

## AI Agent System

### Agent Architecture

Each AI agent inherits from the base `AIAgent` class and implements specialized functionality:

```python
class AIAgent:
    def __init__(self, name: str):
        self.name = name
        self.setup_clients()
    
    def setup_clients(self):
        """Initialize AI model clients (Gemini, Mistral, HuggingFace)"""
    
    def call_gemini_api(self, prompt: str) -> str:
        """Primary AI model interaction"""
```

### Specialized Agent Details

#### 1. MemeHarvester
**Purpose**: Identifies trending phrases and viral content patterns
**Input**: Social media data dumps, trending topics
**Output**: Ranked list of viral phrases, meme potential scores
**Prompt Strategy**: "List the top 5 trending phrases or memes from this text dump"

#### 2. NarrativeAligner
**Purpose**: Maps brand values to compelling story hooks
**Input**: Brand information, trending insights from MemeHarvester
**Output**: Brand-aligned narratives, story hooks, alignment scores
**Prompt Strategy**: "Map these brand values to a short, catchy story hook"

#### 3. CopyCrafter
**Purpose**: Generates ready-to-use advertising copy
**Input**: Story hooks from NarrativeAligner
**Output**: Headlines, 30-second video scripts, multi-platform content
**Prompt Strategy**: "Write three ad headlines and two 30-sec video scripts using this hook"

#### 4. HookOptimizer
**Purpose**: Analyzes viral potential and engagement probability
**Input**: Generated content from CopyCrafter
**Output**: Shareability rankings, engagement scores, A/B test recommendations
**Prompt Strategy**: "Rank these hooks by likely share-ability and engagement"

#### 5. SequencePlanner
**Purpose**: Creates comprehensive email marketing sequences
**Input**: Optimized content from HookOptimizer
**Output**: 5-step email campaigns, behavioral triggers, automation workflows
**Prompt Strategy**: "Draft a 5-step email drip that builds on this narrative"

#### 6. AnalyticsInterpreter
**Purpose**: Provides actionable performance insights
**Input**: Campaign statistics, performance metrics
**Output**: Optimization recommendations, benchmarking analysis
**Prompt Strategy**: "Here are your campaign stats; give me three bullet tips to improve next time"

## API Integration

### Primary AI Services

#### Google Gemini AI
- **Model**: gemini-2.5-flash
- **Usage**: Primary natural language processing
- **Authentication**: GEMINI_API_KEY environment variable
- **Rate Limits**: 10 remote calls per session with AFC enabled

#### Mistral AI
- **Model**: mistral-small-latest
- **Usage**: Secondary language model for specialized tasks
- **Authentication**: MISTRAL_API_KEY environment variable
- **Endpoint**: La Plateforme Mistral API

#### Hugging Face
- **Models**: sentence-transformers, various specialized models
- **Usage**: Text embeddings, semantic similarity
- **Authentication**: HUGGINGFACE_API_TOKEN environment variable

### Real-time Data Sources

#### Reddit API Integration
```python
# Free Reddit JSON feeds
url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=5"
headers = {'User-Agent': 'NeuraAdBrain/1.0'}
```
**Subreddits**: marketing, advertising, entrepreneur, business
**Data**: Post titles, engagement scores, comment counts

#### Cryptocurrency Market Data
```python
# CoinDesk API for market sentiment
crypto_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
```
**Usage**: Tech market sentiment indicator via Bitcoin price movements
**Update Frequency**: Real-time API calls

#### News RSS Feeds
**Sources**: TechCrunch, Wired, VentureBeat, industry-specific feeds
**Processing**: Trafilatura for content extraction
**Integration**: Trend analysis and market intelligence

## Database Schema

### PostgreSQL Tables

#### campaigns
```sql
CREATE TABLE campaigns (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    topic VARCHAR NOT NULL,
    brand VARCHAR NOT NULL,
    budget FLOAT,
    market_region VARCHAR,
    trend_depth VARCHAR,
    creativity_level VARCHAR,
    include_live_data BOOLEAN DEFAULT FALSE,
    user_profile JSONB,
    results JSONB,
    execution_metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR DEFAULT 'active'
);
```

#### workflow_executions
```sql
CREATE TABLE workflow_executions (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    campaign_id VARCHAR,
    workflow_id VARCHAR,
    execution_data JSONB,
    status VARCHAR,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    execution_time_seconds FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### analogies
```sql
CREATE TABLE analogies (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    trend VARCHAR NOT NULL,
    brand VARCHAR NOT NULL,
    analogy TEXT NOT NULL,
    embedding_vector JSONB,
    similarity_score FLOAT,
    campaign_id VARCHAR,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### live_data_snapshots
```sql
CREATE TABLE live_data_snapshots (
    id VARCHAR PRIMARY KEY DEFAULT uuid_generate_v4(),
    topic VARCHAR NOT NULL,
    data_source VARCHAR NOT NULL,
    raw_data JSONB,
    trend_signals JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Vector Store Schema (Qdrant)

#### analogies collection
```python
{
    "id": "unique_identifier",
    "payload": {
        "trend": "trending_topic",
        "brand": "brand_name", 
        "analogy": "generated_analogy_text",
        "similarity_score": 0.85,
        "campaign_id": "uuid"
    },
    "vector": [0.1, 0.2, ..., 0.n]  # 384-dimensional embedding
}
```

## User Interface

### Navigation Structure

#### Main Navigation
1. **Neural Command Center**: Dashboard overview with live metrics
2. **Campaign Studio**: Campaign creation and parameter configuration
3. **AI Agents**: Agent execution interface with progress tracking
4. **Analytics**: Comprehensive results analysis and performance metrics
5. **Enterprise Hub**: Business intelligence and partnership features

### Page Specifications

#### Campaign Studio
**Components**:
- Topic and brand input fields
- Budget allocation sliders
- Market region selection
- Advanced options (creativity level, trend depth)
- Live data integration toggles

**Validation**:
- Required field validation
- Budget range constraints
- Region format verification

#### AI Agents Execution
**Components**:
- Agent status cards with real-time progress
- Execution progress bar
- Live logging display
- Results preview metrics
- Success confirmation with analytics navigation

**Features**:
- Visual agent status indicators (running, completed, error)
- Real-time execution time tracking
- Agent-specific progress messages
- Automatic results storage to session state

#### Analytics Center
**Components**:
- Agent Results Tabs (Trend Analysis, Creative Assets, Budget, Email Sequences)
- Real-time Market Intelligence dashboard
- Performance metrics with live data integration
- Interactive visualizations using Plotly
- Export functionality for campaign data

**Data Sources**:
- Session state campaign results
- Live Reddit trending topics
- Cryptocurrency market sentiment
- Real-time performance fluctuations

## Workflow Execution

### Agent Execution Pipeline

```mermaid
graph TD
    A[Campaign Parameters] --> B[Data Collection]
    B --> C[MemeHarvester]
    C --> D[NarrativeAligner]
    D --> E[CopyCrafter]
    E --> F[HookOptimizer]
    F --> G[SequencePlanner]
    G --> H[AnalyticsInterpreter]
    H --> I[Budget Calculation]
    I --> J[Results Compilation]
    J --> K[Session State Storage]
```

### Execution Flow Details

#### 1. Initialization Phase
- Campaign parameter validation
- Agent client setup (Gemini, Mistral, HuggingFace)
- Database connection establishment
- Vector store initialization

#### 2. Data Collection Phase
- Free API data gathering (Reddit, news, crypto)
- Social media trend analysis
- Market sentiment collection
- Real-time data integration

#### 3. Agent Sequential Execution
Each agent executes in sequence, building upon previous results:
- **Input**: Previous agent outputs + live data
- **Processing**: AI model interaction with specialized prompts
- **Output**: Structured results stored for next agent
- **Monitoring**: Real-time progress tracking and error handling

#### 4. Results Compilation
- Aggregate all agent outputs into comprehensive results object
- Calculate performance metrics and viral potential scores
- Generate budget allocation recommendations
- Store results in session state and database

#### 5. Analytics Display
- Map agent results to analytics interface
- Generate real-time visualizations
- Provide actionable insights and recommendations
- Enable data export and campaign management

### Error Handling Strategy

#### Graceful Degradation
- API failure fallbacks to cached data
- Agent execution continues with available data
- Comprehensive error logging and user notification
- Fallback result generation for incomplete workflows

#### Recovery Mechanisms
- Automatic retry logic for transient failures
- Alternative AI model selection (Gemini → Mistral → HuggingFace)
- Session state preservation across errors
- User-friendly error messages with resolution steps

## Analytics & Reporting

### Key Performance Indicators

#### Viral Potential Metrics
- **Viral Score**: Aggregated shareability rating (0-10)
- **Engagement Probability**: Statistical likelihood of user interaction
- **Trend Alignment**: How well content matches current trends
- **Brand Resonance**: Alignment between content and brand values

#### Budget Optimization Metrics
- **Efficiency Score**: ROI optimization rating (0-10)
- **Channel Allocation**: Percentage distribution across platforms
- **Performance Factors**: Real-time adjustment parameters
- **Cost Per Engagement**: Projected engagement cost analysis

#### Campaign Performance Tracking
- **Social Media Reach**: Projected audience size and engagement
- **Conversion Funnel**: Email sequence performance predictions
- **A/B Testing Recommendations**: Content variation suggestions
- **Market Sentiment Impact**: External factor influence analysis

### Real-time Dashboard Features

#### Live Market Intelligence
- **Reddit Trending Topics**: Real-time social media discussion analysis
- **Cryptocurrency Sentiment**: Tech market mood indicator
- **News Feed Integration**: Industry trend monitoring
- **Global Market Signals**: Cross-platform sentiment analysis

#### Interactive Visualizations
- **Performance Trend Charts**: Time-series campaign metrics
- **Budget Allocation Pie Charts**: Visual spending distribution
- **Viral Potential Heatmaps**: Content performance predictions
- **ROI Projection Graphs**: Expected return calculations

## Installation & Setup

### System Requirements
- Python 3.8+
- PostgreSQL 12+
- Minimum 4GB RAM
- 10GB available disk space
- Internet connection for API access

### Installation Steps

#### 1. Environment Setup
```bash
# Clone repository
git clone [repository_url]
cd neural-adbrain

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

#### 2. Database Configuration
```bash
# Install PostgreSQL (if not installed)
# Create database
createdb neural_adbrain

# Set environment variable
export DATABASE_URL="postgresql://username:password@localhost/neural_adbrain"
```

#### 3. API Key Configuration
```bash
# Required API keys
export GEMINI_API_KEY="your_gemini_api_key"
export MISTRAL_API_KEY="your_mistral_api_key"

# Optional API keys
export HUGGINGFACE_API_TOKEN="your_huggingface_token"
export NEWS_API_KEY="your_news_api_key"
```

#### 4. Application Launch
```bash
# Run Streamlit application
streamlit run app.py --server.port 5000
```

### Dependencies

#### Core Dependencies
```
streamlit>=1.28.0
google-genai>=0.2.0
langchain>=0.1.0
langgraph>=0.0.40
pandas>=1.5.0
plotly>=5.15.0
psycopg2-binary>=2.9.0
qdrant-client>=1.6.0
sqlalchemy>=2.0.0
```

#### AI/ML Dependencies
```
requests>=2.31.0
trafilatura>=1.6.0
numpy>=1.24.0
langchain-community>=0.0.20
langchain-core>=0.1.0
```

## Configuration

### Environment Variables

#### Required Configuration
```bash
# Database
DATABASE_URL="postgresql://user:pass@localhost/neural_adbrain"

# AI Services
GEMINI_API_KEY="your_gemini_key"
MISTRAL_API_KEY="your_mistral_key"

# Database connection details (auto-set by Replit)
PGDATABASE="neural_adbrain"
PGHOST="localhost"
PGPORT="5432"
PGUSER="username"
PGPASSWORD="password"
```

#### Optional Configuration
```bash
# Enhanced features
HUGGINGFACE_API_TOKEN="your_hf_token"
NEWS_API_KEY="your_news_api_key"
OPENWEATHER_API_KEY="your_weather_key"

# Application settings
STREAMLIT_SERVER_PORT="5000"
STREAMLIT_SERVER_ADDRESS="0.0.0.0"
```

### Streamlit Configuration

#### .streamlit/config.toml
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

### AI Model Configuration

#### Model Selection Priority
1. **Primary**: Google Gemini 2.5 Flash (fastest, most reliable)
2. **Secondary**: Mistral Small Latest (fallback for complex tasks)
3. **Tertiary**: Hugging Face models (specialized embedding tasks)

#### Prompt Engineering Settings
- **Temperature**: 0.7 (balanced creativity and consistency)
- **Max Tokens**: 2000 (comprehensive responses)
- **Top P**: 0.9 (high quality text generation)
- **Frequency Penalty**: 0.1 (avoid repetition)

## Troubleshooting

### Common Issues

#### 1. Database Connection Errors
**Symptoms**: PostgreSQL connection failures, table creation errors
**Solutions**:
```bash
# Check database status
pg_isready -h localhost -p 5432

# Verify environment variables
echo $DATABASE_URL

# Reset database connection
python -c "from database import DatabaseManager; db = DatabaseManager()"
```

#### 2. API Key Authentication Failures
**Symptoms**: API response errors, authentication failures
**Solutions**:
```bash
# Verify API keys are set
echo $GEMINI_API_KEY | head -c 20

# Test API connectivity
curl -H "Authorization: Bearer $GEMINI_API_KEY" \
     https://generativelanguage.googleapis.com/v1beta/models
```

#### 3. Session State Persistence Issues
**Symptoms**: Analytics showing no campaign results despite successful execution
**Solutions**:
- Use the debug information in Analytics section
- Check session state keys in debug output
- Try the test data injection button
- Restart the Streamlit application

#### 4. Agent Execution Timeouts
**Symptoms**: Long response times, incomplete workflows
**Solutions**:
- Check internet connectivity
- Verify API rate limits not exceeded
- Review error logs in workflow console
- Use fallback result generation

### Performance Optimization

#### Database Optimization
```sql
-- Index for faster campaign queries
CREATE INDEX idx_campaigns_created_at ON campaigns(created_at);
CREATE INDEX idx_campaigns_status ON campaigns(status);

-- Analyze query performance
EXPLAIN ANALYZE SELECT * FROM campaigns WHERE status = 'active';
```

#### Memory Management
```python
# Vector store optimization
import gc
gc.collect()  # Force garbage collection

# Limit vector store size
max_vectors = 10000
```

#### API Rate Limit Management
- Implement exponential backoff for failed requests
- Cache frequently requested data
- Use batch processing for multiple API calls
- Monitor usage quotas and implement warnings

### Monitoring and Logging

#### Application Logs
- Workflow execution logs in console output
- Agent-specific progress messages
- API call success/failure tracking
- Database operation monitoring

#### Performance Metrics
- Agent execution times
- API response latencies
- Database query performance
- Memory usage tracking

#### Error Tracking
- Comprehensive exception logging
- User-friendly error messages
- Automatic error recovery attempts
- Performance degradation alerts

---

## Support and Maintenance

### Regular Maintenance Tasks
1. **Database Cleanup**: Remove old campaign data and optimize tables
2. **API Key Rotation**: Update authentication credentials regularly
3. **Vector Store Optimization**: Reindex embeddings for better performance
4. **Dependency Updates**: Keep libraries and models current
5. **Performance Monitoring**: Track and optimize system metrics

### Support Channels
- **Technical Issues**: Check troubleshooting section first
- **Feature Requests**: Submit via project repository
- **Performance Problems**: Monitor system resources and logs
- **API Integration**: Verify credentials and test connectivity

### Version History
- **v1.0**: Initial release with 6-agent architecture
- **v1.1**: Real-time data integration and PostgreSQL support
- **v1.2**: Enhanced analytics dashboard and debugging tools
- **v1.3**: Professional UI overhaul and session state optimization

This documentation provides comprehensive coverage of the Neural AdBrain platform architecture, implementation details, and operational guidance for successful deployment and maintenance.
# Multi-Agent Advertising Brain App

## Overview

This is a comprehensive advertising campaign creation and optimization platform powered by multiple specialized AI agents. The application provides a zero-cost solution for marketers to create, analyze, and optimize advertising campaigns using various AI models and techniques. Built with Streamlit for the frontend and Python for the backend logic, it leverages multiple AI services including Gemini AI and Hugging Face models to provide intelligent recommendations across different aspects of campaign management.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web application
- **Layout**: Wide layout with expandable sidebar
- **State Management**: Streamlit session state for maintaining application state across user interactions
- **User Interface**: Interactive dashboard with real-time data visualization using Plotly

### Backend Architecture
- **Language**: Python 3.x
- **Design Pattern**: Multi-agent system with specialized AI agents
- **Agent System**: Five specialized agents handling different aspects of campaign creation:
  - TrendHarvester: Identifies emerging market trends
  - AnalogicalReasoner: Creates brand-relevant analogies from trends
  - CreativeSynthesizer: Generates ad copy and headlines
  - BudgetOptimizer: Optimizes budget allocation across channels
  - PersonalizationAgent: Creates personalized user journeys

### Data Storage Solutions
- **Vector Store**: Qdrant in-memory vector database for production-grade similarity search
- **Campaign Data**: JSON file-based storage for campaign persistence
- **Embeddings**: Hugging Face API with sentence-transformers for semantic similarity
- **Live Data Integration**: Real-time data from Reddit, GitHub, news APIs, and crypto trends

## Key Components

### AI Agents (`agents.py`)
Each agent inherits from a base `AIAgent` class and specializes in specific campaign aspects:
- **Base Agent**: Handles common AI client setup and API calls
- **Specialized Agents**: Implement domain-specific logic using structured prompts
- **API Integration**: Supports both Gemini AI and Hugging Face Inference API

### Vector Store (`vector_store.py`)
- **Purpose**: Stores and retrieves analogies and trends for similarity matching
- **Technology**: SentenceTransformer for embeddings, NumPy for vector operations
- **Persistence**: JSON-based data storage for vector metadata

### Prompt Management (`prompts.py`)
- **Centralized Prompts**: All AI agent prompts defined in a single module
- **Structured Templates**: Formatted prompts with clear output specifications
- **Consistency**: Ensures uniform communication patterns across agents

### Utility Functions (`utils.py`)
- **Campaign Management**: CRUD operations for campaign data
- **Data Export**: CSV export functionality for campaign results
- **Helper Functions**: Data validation, formatting, and chart generation

## Data Flow

1. **User Input**: Campaign requirements entered through Streamlit interface
2. **Agent Orchestration**: Main app coordinates agent execution in sequence
3. **Trend Analysis**: TrendHarvester identifies relevant market trends
4. **Analogy Creation**: AnalogicalReasoner creates brand-specific analogies
5. **Creative Generation**: CreativeSynthesizer produces ad copy and headlines
6. **Budget Optimization**: BudgetOptimizer allocates budget across channels
7. **Personalization**: PersonalizationAgent creates targeted user journeys
8. **Data Persistence**: Results stored in JSON files and vector store
9. **Visualization**: Results displayed through interactive dashboard

## External Dependencies

### AI Services
- **Gemini AI**: Primary AI model for natural language processing
- **Mistral AI**: La Plateforme Mistral API for high-quality language model inference
- **Hugging Face**: Inference API with multiple model support
- **Qdrant**: Vector database for semantic similarity and analogical reasoning

### Python Libraries
- **Streamlit**: Web application framework
- **Plotly**: Interactive data visualization
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing for vector operations
- **Requests**: HTTP client for API calls

### Environment Variables
- `GEMINI_API_KEY`: Authentication for Google Gemini AI
- `MISTRAL_API_KEY`: Authentication for La Plateforme Mistral AI
- `HUGGINGFACE_API_TOKEN`: Authentication for Hugging Face API
- `NEWS_API_KEY`: Optional for enhanced news data (NewsAPI)
- `OPENWEATHER_API_KEY`: Optional for weather context data

## Deployment Strategy

### Local Development
- **Setup**: Clone repository and install dependencies from requirements
- **Configuration**: Set environment variables for API keys
- **Execution**: Run via `streamlit run app.py`

### Zero-Cost Architecture
- **Design Principle**: Minimize external service costs
- **Fallback Strategy**: Multiple AI service options to ensure availability
- **Local Processing**: Vector embeddings computed locally to reduce API calls

### Scalability Considerations
- **File-based Storage**: Suitable for demo/prototype scale
- **Memory Management**: In-memory vector store for fast similarity search
- **Future Enhancements**: Can be extended with proper database integration

## Specialized 6-Agent Architecture with Free Data APIs

### Implementation (June 29, 2025)

The Neural AdBrain platform now features **6 specialized AI agents with comprehensive free data integration** for zero-cost campaign creation and optimization:

#### Specialized Agent Modules
1. **MemeHarvester**: "List the top 5 trending phrases or memes from this text dump"
   - Analyzes Twitter/Reddit data for viral content patterns
   - Identifies cultural moments and engagement trends
   - Scores meme potential and virality factors

2. **NarrativeAligner**: "Map these brand values to a short, catchy story hook"
   - Creates compelling brand narratives from trending data
   - Aligns brand values with cultural zeitgeist
   - Generates multiple story hook variations

3. **CopyCrafter**: "Write three ad headlines and two 30-sec video scripts using this hook"
   - Produces ready-to-use advertising copy
   - Creates multi-platform content variations
   - Optimizes for different audience segments

4. **HookOptimizer**: "Rank these hooks by likely share-ability and engagement"
   - Analyzes viral potential across platforms
   - Provides A/B testing recommendations
   - Calculates engagement probability scores

5. **SequencePlanner**: "Draft a 5-step email drip that builds on this narrative"
   - Creates comprehensive email marketing sequences
   - Implements behavioral triggers and automation
   - Optimizes conversion funnel progression

6. **AnalyticsInterpreter**: "Here are your campaign stats; give me three bullet tips to improve next time"
   - Provides actionable performance insights
   - Benchmarks against industry standards
   - Recommends specific optimization strategies

#### Free Data Integration Sources
- **Twitter Alternative APIs**: Nitter instances for social media trends
- **Reddit Public JSON**: Real-time community discussions and engagement
- **Free RSS News Feeds**: Industry insights from TechCrunch, Wired, VentureBeat
- **Creative Commons Resources**: Free stock photos, icons, and design assets
- **Marketing Resource APIs**: Industry trends, competitive analysis, keyword data

#### Technical Implementation
- **Sequential Workflow**: Agents execute in optimized order for maximum insight building
- **Data Fusion**: Combines multiple free data sources for comprehensive market intelligence
- **Real-time Processing**: Live social media and news data integration
- **Zero-Cost Architecture**: No paid API dependencies for core functionality
- **Enterprise Storage**: PostgreSQL persistence with vector similarity search

## Changelog

```
Changelog:
- June 29, 2025. Initial setup with Streamlit and basic multi-agent architecture
- June 29, 2025. Enhanced with Qdrant vector store for production-grade similarity search
- June 29, 2025. Integrated La Plateforme Mistral AI API for improved language model capabilities
- June 29, 2025. Added live data integration (Reddit, GitHub, news, crypto trends) for real-time market intelligence
- June 29, 2025. Implemented comprehensive trend signal analysis with multi-source data fusion
- June 29, 2025. BREAKTHROUGH: Revolutionary LangGraph architecture with autonomous multi-agent orchestration
- June 29, 2025. Transformed UI to elegant orange gradient design with smooth 4-step user experience flow
- June 29, 2025. Enhanced results display with comprehensive insights across 5 revolutionary domains
- June 30, 2025. EXTRAORDINARY VISUAL TRANSFORMATION: Implemented mind-blowing 12-color animated gradient background
- June 30, 2025. Added glassmorphism effects, neon glowing buttons, and floating animations throughout the UI
- June 30, 2025. Fixed all CSS rendering issues in AI Intelligence page during campaign execution
- June 30, 2025. Resolved f-string syntax errors in components.py for seamless operation
- June 30, 2025. PROFESSIONAL UI OVERHAUL: Transformed to React-style components with JavaScript interactivity
- June 30, 2025. Fixed text visibility issues with professional white backgrounds and dark text for optimal readability
- June 30, 2025. Added hover animations, click effects, and progress indicators to all UI components
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```
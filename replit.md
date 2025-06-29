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
- **Vector Store**: In-memory vector storage using sentence transformers for similarity search
- **Campaign Data**: JSON file-based storage for campaign persistence
- **Embeddings**: SentenceTransformer model (all-MiniLM-L6-v2) for semantic similarity

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
- **Hugging Face**: Fallback inference API using Mistral-7B model
- **SentenceTransformers**: Local embeddings for similarity search

### Python Libraries
- **Streamlit**: Web application framework
- **Plotly**: Interactive data visualization
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing for vector operations
- **Requests**: HTTP client for API calls

### Environment Variables
- `GEMINI_API_KEY`: Authentication for Google Gemini AI
- `HUGGINGFACE_API_TOKEN`: Authentication for Hugging Face API

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

## Changelog

```
Changelog:
- June 29, 2025. Initial setup
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```
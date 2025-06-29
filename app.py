"""
Multi-Agent Advertising Brain App
A zero-cost solution for comprehensive campaign creation and optimization.
"""

import streamlit as st
import json
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# Import our custom modules
from agents import TrendHarvester, AnalogicalReasoner, CreativeSynthesizer, BudgetOptimizer, PersonalizationAgent
from vector_store import SimpleVectorStore
from utils import CampaignManager, export_campaign_to_csv, create_sample_user_profile, format_agent_response, create_budget_chart_data, validate_api_keys

# Page configuration
st.set_page_config(
    page_title="Multi-Agent Advertising Brain",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = SimpleVectorStore()

if 'campaign_manager' not in st.session_state:
    st.session_state.campaign_manager = CampaignManager()

if 'current_campaign' not in st.session_state:
    st.session_state.current_campaign = None

if 'agents_initialized' not in st.session_state:
    st.session_state.agents_initialized = False

def initialize_agents():
    """Initialize all AI agents."""
    if not st.session_state.agents_initialized:
        try:
            st.session_state.trend_harvester = TrendHarvester()
            st.session_state.analogical_reasoner = AnalogicalReasoner(st.session_state.vector_store)
            st.session_state.creative_synthesizer = CreativeSynthesizer()
            st.session_state.budget_optimizer = BudgetOptimizer()
            st.session_state.personalization_agent = PersonalizationAgent()
            st.session_state.agents_initialized = True
            return True
        except Exception as e:
            st.error(f"Error initializing agents: {e}")
            return False
    return True

def main():
    """Main application function."""
    
    # Header
    st.title("🧠 Multi-Agent Advertising Brain")
    st.markdown("**Zero-cost, next-level campaign creation and optimization using AI agents**")
    
    # Check API keys
    api_status = validate_api_keys()
    
    if not any(api_status.values()):
        st.error("⚠️ No API keys found. Please set GEMINI_API_KEY and/or HUGGINGFACE_API_TOKEN environment variables.")
        st.info("The app will use fallback responses for demonstration purposes.")
    else:
        if api_status["GEMINI_API_KEY"]:
            st.success("✅ Gemini API key found")
        if api_status["HUGGINGFACE_API_TOKEN"]:
            st.success("✅ Hugging Face API key found")
    
    # Initialize agents
    if not initialize_agents():
        st.stop()
    
    # Sidebar navigation
    with st.sidebar:
        st.header("Navigation")
        page = st.selectbox(
            "Choose a page:",
            ["🏠 Campaign Creator", "📊 Dashboard", "📁 Campaign History", "⚙️ Settings"]
        )
        
        # Vector store stats
        st.subheader("Vector Store Stats")
        stats = st.session_state.vector_store.get_stats()
        st.metric("Total Analogies", stats["total_analogies"])
        st.metric("Unique Trends", stats["unique_trends"])
        st.metric("Unique Brands", stats["unique_brands"])
    
    # Main content based on selected page
    if page == "🏠 Campaign Creator":
        campaign_creator_page()
    elif page == "📊 Dashboard":
        dashboard_page()
    elif page == "📁 Campaign History":
        campaign_history_page()
    elif page == "⚙️ Settings":
        settings_page()

def campaign_creator_page():
    """Campaign creation page."""
    
    st.header("Create New Campaign")
    
    # Campaign input form
    with st.form("campaign_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            topic = st.text_input(
                "Campaign Topic",
                placeholder="e.g., Sustainable Fashion, AI Technology, Fitness Apps",
                help="Enter the main topic or theme for your advertising campaign"
            )
            
            brand = st.text_input(
                "Brand Name",
                placeholder="e.g., Nike, Apple, Local Coffee Shop",
                help="Enter the brand name you're creating the campaign for"
            )
        
        with col2:
            # User profile selection
            profile_option = st.selectbox(
                "Target Audience Profile",
                ["Sample Profile", "Custom Profile"]
            )
            
            if profile_option == "Custom Profile":
                custom_profile = st.text_area(
                    "Custom User Profile (JSON)",
                    placeholder='{"demographics": {"age": "25-34"}, "interests": ["tech", "sports"]}',
                    help="Enter a custom user profile in JSON format"
                )
            else:
                custom_profile = None
        
        # Advanced options
        with st.expander("Advanced Options"):
            include_budget = st.checkbox("Include Budget Optimization", value=True)
            include_personalization = st.checkbox("Include Personalization", value=True)
            
        submit_campaign = st.form_submit_button(
            "🚀 Run Campaign Analysis",
            type="primary",
            use_container_width=True
        )
    
    # Process campaign when submitted
    if submit_campaign:
        if not topic or not brand:
            st.error("Please provide both a campaign topic and brand name.")
            return
        
        # Prepare user profile
        if profile_option == "Custom Profile" and custom_profile:
            try:
                user_profile = json.loads(custom_profile)
            except json.JSONDecodeError:
                st.error("Invalid JSON format in custom profile. Using sample profile instead.")
                user_profile = create_sample_user_profile()
        else:
            user_profile = create_sample_user_profile()
        
        # Run the multi-agent workflow
        run_campaign_workflow(topic, brand, user_profile, include_budget, include_personalization)

def run_campaign_workflow(topic, brand, user_profile, include_budget, include_personalization):
    """Execute the multi-agent campaign workflow."""
    
    st.header("🔄 Campaign Analysis in Progress")
    
    # Progress tracking
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Results container
    results = {}
    
    # Step 1: Trend Harvesting
    status_text.text("🔍 Harvesting trends...")
    progress_bar.progress(20)
    
    with st.spinner("TrendHarvester is analyzing emerging micro-trends..."):
        trend_result = st.session_state.trend_harvester.harvest_trends(topic)
        results['trend_harvester'] = trend_result
    
    # Display trend results
    with st.expander("📈 Trend Analysis Results", expanded=True):
        st.markdown(format_agent_response(trend_result['trends'], 'TrendHarvester'))
    
    # Step 2: Analogical Reasoning
    status_text.text("🧠 Creating brand analogies...")
    progress_bar.progress(40)
    
    # Extract first trend for analogy (simplified)
    trend_lines = trend_result['trends'].split('\n')
    first_trend = None
    for line in trend_lines:
        if line.strip().startswith('•'):
            first_trend = line.split('(')[0].replace('•', '').strip()
            break
    
    if not first_trend:
        first_trend = topic  # Fallback to topic
    
    with st.spinner("AnalogicalReasoner is creating brand-trend analogies..."):
        analogy_result = st.session_state.analogical_reasoner.create_analogy(first_trend, brand)
        results['analogical_reasoner'] = analogy_result
    
    # Display analogy results
    with st.expander("🧠 Brand Analogy Results", expanded=True):
        st.markdown(format_agent_response(analogy_result['analogy'], 'AnalogicalReasoner'))
        
        if analogy_result.get('similar_analogies'):
            st.subheader("Similar Analogies Found")
            for similar in analogy_result['similar_analogies']:
                st.write(f"**{similar['trend']} × {similar['brand']}** (Similarity: {similar['similarity']:.2f})")
                st.write(similar['analogy'])
    
    # Step 3: Creative Synthesis
    status_text.text("✨ Generating creative content...")
    progress_bar.progress(60)
    
    with st.spinner("CreativeSynthesizer is crafting ad content..."):
        creative_result = st.session_state.creative_synthesizer.synthesize_creative(analogy_result['analogy'])
        results['creative_synthesizer'] = creative_result
    
    # Display creative results
    with st.expander("✨ Creative Content Results", expanded=True):
        st.markdown(format_agent_response(creative_result['creative_content'], 'CreativeSynthesizer'))
    
    # Step 4: Budget Optimization (optional)
    if include_budget:
        status_text.text("💰 Optimizing budget allocation...")
        progress_bar.progress(80)
        
        with st.spinner("BudgetOptimizer is analyzing spend allocation..."):
            budget_result = st.session_state.budget_optimizer.optimize_budget()
            results['budget_optimizer'] = budget_result
        
        # Display budget results
        with st.expander("💰 Budget Optimization Results", expanded=True):
            st.markdown(format_agent_response(budget_result['optimization_plan'], 'BudgetOptimizer'))
            
            # Create budget chart
            budget_data = create_budget_chart_data(budget_result['optimization_plan'])
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Recommended Budget Allocation")
                fig = px.pie(
                    values=list(budget_data.values()),
                    names=list(budget_data.keys()),
                    title="Channel Budget Distribution"
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Budget Breakdown")
                budget_df = pd.DataFrame(
                    list(budget_data.items()),
                    columns=['Channel', 'Percentage']
                )
                st.dataframe(budget_df, use_container_width=True)
    
    # Step 5: Personalization (optional)
    if include_personalization:
        status_text.text("👤 Creating personalization plan...")
        progress_bar.progress(90)
        
        with st.spinner("PersonalizationAgent is crafting user journey..."):
            personalization_result = st.session_state.personalization_agent.create_personalization(user_profile)
            results['personalization_agent'] = personalization_result
        
        # Display personalization results
        with st.expander("👤 Personalization Plan Results", expanded=True):
            st.markdown(format_agent_response(personalization_result['personalization_plan'], 'PersonalizationAgent'))
            
            st.subheader("Target User Profile")
            st.json(user_profile)
    
    # Complete
    status_text.text("✅ Campaign analysis complete!")
    progress_bar.progress(100)
    
    # Save campaign
    campaign_data = {
        'topic': topic,
        'brand': brand,
        'user_profile': user_profile,
        'results': results,
        'include_budget': include_budget,
        'include_personalization': include_personalization
    }
    
    campaign_id = st.session_state.campaign_manager.save_campaign(campaign_data)
    st.session_state.current_campaign = campaign_id
    
    st.success(f"✅ Campaign saved with ID: {campaign_id}")
    
    # Export options
    st.subheader("📤 Export Options")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Export to CSV", use_container_width=True):
            csv_file = export_campaign_to_csv(campaign_data)
            if csv_file:
                st.success(f"Exported to {csv_file}")
    
    with col2:
        if st.button("📋 Copy Campaign Data", use_container_width=True):
            st.code(json.dumps(campaign_data, indent=2, default=str))

def dashboard_page():
    """Campaign dashboard page."""
    
    st.header("📊 Campaign Dashboard")
    
    if not st.session_state.current_campaign:
        st.info("No active campaign. Please create a campaign first.")
        return
    
    # Load current campaign
    campaign = st.session_state.campaign_manager.get_campaign(st.session_state.current_campaign)
    
    if not campaign:
        st.error("Current campaign not found.")
        return
    
    # Campaign overview
    st.subheader("Campaign Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Campaign ID", campaign.get('id', 'Unknown'))
    with col2:
        st.metric("Topic", campaign.get('topic', 'Unknown'))
    with col3:
        st.metric("Brand", campaign.get('brand', 'Unknown'))
    with col4:
        st.metric("Created", campaign.get('created_at', 'Unknown')[:10])
    
    # Results summary
    results = campaign.get('results', {})
    
    # Agent status
    st.subheader("Agent Execution Status")
    agent_status = []
    
    for agent_name in ['trend_harvester', 'analogical_reasoner', 'creative_synthesizer', 'budget_optimizer', 'personalization_agent']:
        if agent_name in results:
            agent_status.append({
                'Agent': agent_name.replace('_', ' ').title(),
                'Status': '✅ Completed',
                'Output Length': len(str(results[agent_name])),
            })
        else:
            agent_status.append({
                'Agent': agent_name.replace('_', ' ').title(),
                'Status': '❌ Not Run',
                'Output Length': 0,
            })
    
    status_df = pd.DataFrame(agent_status)
    st.dataframe(status_df, use_container_width=True)
    
    # Detailed results
    st.subheader("Detailed Results")
    
    for agent_name, result in results.items():
        with st.expander(f"{agent_name.replace('_', ' ').title()} Results"):
            st.json(result)

def campaign_history_page():
    """Campaign history page."""
    
    st.header("📁 Campaign History")
    
    campaigns = st.session_state.campaign_manager.list_campaigns()
    
    if not campaigns:
        st.info("No campaigns found. Create your first campaign!")
        return
    
    # Campaign list
    for campaign in campaigns:
        with st.expander(f"Campaign: {campaign.get('topic', 'Unknown')} × {campaign.get('brand', 'Unknown')}"):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write(f"**ID:** {campaign.get('id', 'Unknown')}")
                st.write(f"**Created:** {campaign.get('created_at', 'Unknown')}")
                st.write(f"**Agents Run:** {len(campaign.get('results', {}))}")
            
            with col2:
                if st.button("Load Campaign", key=f"load_{campaign.get('id')}"):
                    st.session_state.current_campaign = campaign.get('id')
                    st.success("Campaign loaded!")
                    st.rerun()
            
            with col3:
                if st.button("Delete", key=f"delete_{campaign.get('id')}", type="secondary"):
                    if st.session_state.campaign_manager.delete_campaign(campaign.get('id')):
                        st.success("Campaign deleted!")
                        st.rerun()

def settings_page():
    """Settings and configuration page."""
    
    st.header("⚙️ Settings")
    
    # API Configuration
    st.subheader("API Configuration")
    
    api_status = validate_api_keys()
    
    for api_name, status in api_status.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{api_name}:**")
        with col2:
            if status:
                st.success("✅ Available")
            else:
                st.error("❌ Missing")
    
    st.info("API keys are loaded from environment variables. Please set them before running the application.")
    
    # Vector Store Management
    st.subheader("Vector Store Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Clear Vector Store"):
            st.session_state.vector_store = SimpleVectorStore()
            st.success("Vector store cleared!")
    
    with col2:
        stats = st.session_state.vector_store.get_stats()
        st.write(f"Current analogies: {stats['total_analogies']}")
    
    # Campaign Data Management
    st.subheader("Campaign Data Management")
    
    campaigns = st.session_state.campaign_manager.list_campaigns()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Clear All Campaigns", type="secondary"):
            st.session_state.campaign_manager.campaigns = {}
            st.session_state.campaign_manager.save_campaigns()
            st.success("All campaigns cleared!")
    
    with col2:
        st.write(f"Total campaigns: {len(campaigns)}")
    
    # System Information
    st.subheader("System Information")
    
    system_info = {
        "Python Version": "3.x",
        "Streamlit Version": st.__version__,
        "Vector Store Type": "In-Memory",
        "Storage Type": "File-based"
    }
    
    for key, value in system_info.items():
        st.write(f"**{key}:** {value}")

if __name__ == "__main__":
    main()

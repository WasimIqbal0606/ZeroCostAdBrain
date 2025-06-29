"""
Neural AdBrain - Enterprise Multi-Agent AI Platform
Big tech style advertising intelligence with live data and workflow orchestration.
"""

import streamlit as st
import json
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
import asyncio

# Import our custom modules
from agents import TrendHarvester, AnalogicalReasoner, CreativeSynthesizer, BudgetOptimizer, PersonalizationAgent
from vector_store import QdrantVectorStore
from utils import CampaignManager, export_campaign_to_csv, create_sample_user_profile, format_agent_response, create_budget_chart_data, validate_api_keys
from n8n_workflow import N8NWorkflowEngine
from components import (
    render_neural_network_background, render_hero_section, render_agent_card,
    render_workflow_visualization, render_metrics_dashboard, render_campaign_results_panel,
    render_sidebar_navigation, render_loading_animation, render_status_indicator
)

# Page configuration
st.set_page_config(
    page_title="Neural AdBrain - Enterprise AI Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = QdrantVectorStore()

if 'campaign_manager' not in st.session_state:
    st.session_state.campaign_manager = CampaignManager()

if 'workflow_engine' not in st.session_state:
    st.session_state.workflow_engine = N8NWorkflowEngine()
    st.session_state.main_workflow_id = st.session_state.workflow_engine.create_advertising_workflow()

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
    """Main application function with big tech styling."""
    
    # Render custom sidebar
    render_sidebar_navigation()
    
    # Hero section
    render_hero_section()
    
    # 3D Neural network background
    with st.container():
        st.markdown("### Live Neural Network Intelligence")
        neural_fig = render_neural_network_background()
        st.plotly_chart(neural_fig, use_container_width=True)
    
    # Check API keys with status indicators
    api_status = validate_api_keys()
    
    if not any(api_status.values()):
        render_status_indicator("error", "No AI services connected. Configure API keys to enable intelligence.")
    else:
        connected_services = []
        if api_status["GEMINI_API_KEY"]:
            connected_services.append("Gemini AI")
        if api_status["MISTRAL_API_KEY"]:
            connected_services.append("Mistral AI") 
        if api_status["HUGGINGFACE_API_TOKEN"]:
            connected_services.append("Hugging Face")
        
        render_status_indicator("success", f"Connected: {', '.join(connected_services)}")
    
    # Initialize agents
    if not initialize_agents():
        st.stop()
    
    # Main navigation tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🚀 Campaign Creator", 
        "🔄 Workflow Designer", 
        "📊 Intelligence Dashboard", 
        "📁 Campaign Archive", 
        "⚙️ Platform Settings"
    ])
    
    with tab1:
        campaign_creator_page()
    with tab2:
        workflow_designer_page()
    with tab3:
        dashboard_page()
    with tab4:
        campaign_history_page()
    with tab5:
        settings_page()

def workflow_designer_page():
    """N8N-style workflow designer page."""
    
    st.markdown("## 🔄 Workflow Orchestration Engine")
    st.markdown("Design and monitor AI agent workflows with enterprise-grade orchestration")
    
    # Workflow status
    workflow_status = st.session_state.workflow_engine.get_workflow_status(st.session_state.main_workflow_id)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Workflow Architecture")
        workflow_viz = st.session_state.workflow_engine.get_workflow_visualization(st.session_state.main_workflow_id)
        if workflow_viz and "nodes" in workflow_viz:
            viz_fig = render_workflow_visualization(workflow_viz)
            st.plotly_chart(viz_fig, use_container_width=True)
        else:
            st.info("Workflow visualization loading...")
    
    with col2:
        st.markdown("### Agent Status")
        if "nodes" in workflow_status:
            for node_id, node_info in workflow_status["nodes"].items():
                render_agent_card(
                    node_info["name"],
                    f"Type: {node_info['type']}",
                    node_info["status"],
                    node_info.get("execution_time", 0)
                )
    
    # Execution history
    st.markdown("### Recent Executions")
    execution_history = st.session_state.workflow_engine.get_execution_history(5)
    
    if execution_history:
        for execution in execution_history[-3:]:  # Show last 3
            with st.expander(f"Execution {execution['execution_id'][:8]} - {execution['status']}"):
                st.json(execution)
    else:
        st.info("No workflow executions yet")

def campaign_creator_page():
    """Enhanced campaign creation page with big tech styling."""
    
    st.markdown("## 🚀 AI Campaign Intelligence Generator")
    st.markdown("Create enterprise-grade advertising campaigns powered by multi-agent AI")
    
    # Campaign input form with enhanced styling
    st.markdown("""
    <div style="
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.15);
        border: 1px solid #FFE4CC;
    ">
    """, unsafe_allow_html=True)
    
    with st.form("campaign_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 Campaign Configuration")
            topic = st.text_input(
                "Campaign Topic",
                placeholder="AI-Powered Fitness, Sustainable Fashion, FinTech Innovation",
                help="Define your campaign's core theme or industry focus"
            )
            
            brand = st.text_input(
                "Brand Identity",
                placeholder="Nike, Tesla, Spotify, Local Startup",
                help="Enter the brand name for campaign personalization"
            )
            
            campaign_budget = st.number_input(
                "Campaign Budget ($)",
                min_value=1000,
                max_value=1000000,
                value=50000,
                step=5000,
                help="Total advertising budget for optimization"
            )
        
        with col2:
            st.markdown("### 👥 Audience Intelligence")
            profile_option = st.selectbox(
                "Target Audience Profile",
                ["AI-Generated Profile", "Custom Profile", "Enterprise Template"],
                help="Choose how to define your target audience"
            )
            
            if profile_option == "Custom Profile":
                custom_profile = st.text_area(
                    "Custom Audience Profile (JSON)",
                    placeholder='{"demographics": {"age": "25-34", "income": "$75k+"}, "interests": ["technology", "sustainability"]}',
                    help="Define custom audience in JSON format",
                    height=120
                )
            else:
                custom_profile = None
            
            market_region = st.selectbox(
                "Primary Market",
                ["North America", "Europe", "Asia-Pacific", "Global", "Custom Region"],
                help="Target geographic market"
            )
        
        # Enhanced options panel
        st.markdown("### ⚡ AI Agent Configuration")
        col3, col4 = st.columns(2)
        
        with col3:
            include_budget = st.checkbox("Budget Optimization Agent", value=True)
            include_personalization = st.checkbox("Personalization Agent", value=True)
            include_live_data = st.checkbox("Live Market Intelligence", value=True)
        
        with col4:
            trend_depth = st.select_slider(
                "Trend Analysis Depth",
                options=["Surface", "Standard", "Deep", "Comprehensive"],
                value="Standard"
            )
            
            creativity_level = st.select_slider(
                "Creative Innovation Level", 
                options=["Conservative", "Balanced", "Bold", "Disruptive"],
                value="Balanced"
            )
            
        submit_campaign = st.form_submit_button(
            "🚀 Launch AI Campaign Intelligence",
            type="primary",
            use_container_width=True
        )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Process campaign when submitted
    if submit_campaign:
        if not topic or not brand:
            render_status_indicator("error", "Campaign topic and brand identity are required")
            return
        
        render_status_indicator("info", "Initializing AI agents for campaign intelligence...")
        
        # Prepare enhanced user profile
        if profile_option == "Custom Profile" and custom_profile:
            try:
                user_profile = json.loads(custom_profile)
            except json.JSONDecodeError:
                render_status_indicator("warning", "Invalid JSON format. Using AI-generated profile.")
                user_profile = create_sample_user_profile()
        else:
            user_profile = create_sample_user_profile()
        
        # Enhanced campaign parameters
        campaign_params = {
            "topic": topic,
            "brand": brand,
            "budget": campaign_budget,
            "market_region": market_region,
            "trend_depth": trend_depth,
            "creativity_level": creativity_level,
            "include_live_data": include_live_data
        }
        
        # Run the enhanced multi-agent workflow
        run_enhanced_campaign_workflow(campaign_params, user_profile, include_budget, include_personalization)

def run_enhanced_campaign_workflow(campaign_params: dict, user_profile: dict, include_budget: bool, include_personalization: bool):
    """Execute enhanced campaign workflow with N8N orchestration."""
    
    st.markdown("## 🔄 AI Agent Orchestration Engine")
    st.markdown("Enterprise workflow execution with real-time monitoring")
    
    # Initialize workflow execution
    workflow_input = {
        "campaign_params": campaign_params,
        "user_profile": user_profile,
        "options": {
            "include_budget": include_budget,
            "include_personalization": include_personalization
        }
    }
    
    # Progress tracking with enhanced UI
    progress_container = st.container()
    results_container = st.container()
    
    with progress_container:
        st.markdown("### Agent Execution Pipeline")
        
        # Create progress columns for each agent
        agent_cols = st.columns(5)
        agent_names = ["TrendHarvester", "AnalogicalReasoner", "CreativeSynthesizer", "BudgetOptimizer", "PersonalizationAgent"]
        
        # Initialize agent status cards
        agent_statuses = {}
        for i, agent_name in enumerate(agent_names):
            with agent_cols[i]:
                agent_statuses[agent_name] = st.empty()
                agent_statuses[agent_name].markdown(f"""
                <div style="
                    background: white;
                    border-radius: 12px;
                    padding: 1rem;
                    text-align: center;
                    border: 2px solid #E5E7EB;
                    margin-bottom: 1rem;
                ">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚪</div>
                    <div style="font-size: 0.8rem; color: #6B7280;">{agent_name}</div>
                    <div style="font-size: 0.7rem; color: #9CA3AF;">Waiting</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Execute workflow steps
    results = {}
    
    # Step 1: TrendHarvester with live data
    agent_statuses["TrendHarvester"].markdown(f"""
    <div style="
        background: white;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        border: 2px solid #F59E0B;
        margin-bottom: 1rem;
    ">
        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🟡</div>
        <div style="font-size: 0.8rem; color: #1F2937;">TrendHarvester</div>
        <div style="font-size: 0.7rem; color: #F59E0B;">Running</div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.spinner("TrendHarvester analyzing market intelligence..."):
        trend_result = st.session_state.trend_harvester.harvest_trends(campaign_params["topic"])
        results['trend_harvester'] = trend_result
    
    agent_statuses["TrendHarvester"].markdown(f"""
    <div style="
        background: white;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        border: 2px solid #10B981;
        margin-bottom: 1rem;
    ">
        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🟢</div>
        <div style="font-size: 0.8rem; color: #1F2937;">TrendHarvester</div>
        <div style="font-size: 0.7rem; color: #10B981;">Completed</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Continue with other agents...
    # (Similar pattern for remaining agents)
    
    # Display results with enhanced UI
    with results_container:
        render_campaign_results_panel(results)
        
        # Save campaign with enhanced metadata
        campaign_data = {
            **campaign_params,
            'user_profile': user_profile,
            'results': results,
            'execution_metadata': {
                'workflow_engine': 'N8N',
                'ai_models_used': ['Gemini', 'Mistral', 'HuggingFace'],
                'live_data_enabled': campaign_params.get('include_live_data', False),
                'execution_timestamp': datetime.now().isoformat()
            }
        }
        
        campaign_id = st.session_state.campaign_manager.save_campaign(campaign_data)
        st.session_state.current_campaign = campaign_id
        
        render_status_indicator("success", f"Campaign intelligence generated successfully. ID: {campaign_id}")
        
        # Enhanced export options
        st.markdown("### Export & Integration")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 Export Analytics Report", use_container_width=True):
                csv_file = export_campaign_to_csv(campaign_data)
                if csv_file:
                    render_status_indicator("success", f"Analytics exported to {csv_file}")
        
        with col2:
            if st.button("🔗 Generate API Payload", use_container_width=True):
                api_payload = json.dumps(campaign_data, indent=2, default=str)
                st.code(api_payload, language="json")
        
        with col3:
            if st.button("📋 Copy Campaign JSON", use_container_width=True):
                st.code(json.dumps(campaign_data, indent=2, default=str))

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
        
        # Show live data insights if available
        if 'live_data' in trend_result and 'trend_signals' in trend_result:
            st.subheader("🔴 Live Market Intelligence")
            signals = trend_result['trend_signals']
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Social Momentum", f"{signals['social_momentum']}/10")
            with col2:
                st.metric("News Coverage", f"{signals['news_relevance']}/10")
            with col3:
                st.metric("Tech Innovation", f"{signals['tech_innovation']}/10")
            with col4:
                st.metric("Market Interest", f"{signals['market_interest']}/10")
            
            # Show data sources
            live_data = trend_result['live_data']['sources']
            st.write(f"**Live Sources:** {len(live_data['reddit'])} Reddit posts, {len(live_data['news'])} news articles, {len(live_data['github'])} GitHub repos, {len(live_data['crypto'])} crypto trends")
    
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

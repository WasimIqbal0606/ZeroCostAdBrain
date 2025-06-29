"""
Modern UI components for the Neural AdBrain platform.
Implements elegant orange gradient design with clean typography and smooth animations.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import math
from typing import Dict, List, Any
import json

def render_hero_section():
    """Render modern orange gradient hero section."""
    
    # Custom CSS for the hero section
    st.markdown("""
    <style>
    .hero-container {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        padding: 4rem 2rem;
        border-radius: 0;
        margin: -1rem -1rem 2rem -1rem;
        color: white;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 300;
        line-height: 1.2;
        margin: 0 0 1.5rem 0;
        color: white;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 300;
        line-height: 1.6;
        margin: 1.5rem 0;
        color: rgba(255,255,255,0.9);
        max-width: 600px;
    }
    .hero-button {
        background: rgba(255,255,255,0.2);
        border: 2px solid white;
        color: white;
        padding: 1rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 500;
        border-radius: 50px;
        cursor: pointer;
        backdrop-filter: blur(10px);
        margin-top: 2rem;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
    }
    .hero-button:hover {
        background: rgba(255,255,255,0.3);
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create network visualization
    fig = create_network_visualization()
    
    # Hero section layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">Engineering the AI-Powered<br>Advertising Brain for<br>Modern Campaigns</h1>
            <p class="hero-subtitle">Transform your marketing with our neural advertising platform, creating intelligent campaigns through advanced AI orchestration and real-time market intelligence.</p>
            <div class="hero-button">Get Started →</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def create_network_visualization():
    """Create elegant 3D network visualization."""
    
    # Generate sophisticated network structure
    nodes_x, nodes_y, nodes_z = [], [], []
    edges_x, edges_y, edges_z = [], [], []
    
    # Create nodes in elegant 3D pattern
    for i in range(25):
        theta = 2 * math.pi * i / 25
        phi = math.pi * (i % 6) / 5
        r = 1 + 0.4 * math.sin(i * 0.5)
        
        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)
        
        nodes_x.append(x)
        nodes_y.append(y)
        nodes_z.append(z)
    
    # Create elegant connections
    for i in range(len(nodes_x)):
        for j in range(i + 1, len(nodes_x)):
            dist = ((nodes_x[i] - nodes_x[j])**2 + 
                   (nodes_y[i] - nodes_y[j])**2 + 
                   (nodes_z[i] - nodes_z[j])**2)**0.5
            if dist < 1.2 and np.random.random() > 0.65:
                edges_x.extend([nodes_x[i], nodes_x[j], None])
                edges_y.extend([nodes_y[i], nodes_y[j], None])
                edges_z.extend([nodes_z[i], nodes_z[j], None])
    
    fig = go.Figure()
    
    # Add connections with gradient effect
    fig.add_trace(go.Scatter3d(
        x=edges_x, y=edges_y, z=edges_z,
        mode='lines',
        line=dict(color='rgba(255,255,255,0.4)', width=3),
        showlegend=False,
        hoverinfo='none'
    ))
    
    # Add nodes with glow effect
    fig.add_trace(go.Scatter3d(
        x=nodes_x, y=nodes_y, z=nodes_z,
        mode='markers',
        marker=dict(
            size=10,
            color='white',
            opacity=0.9,
            line=dict(color='rgba(255,255,255,0.6)', width=2)
        ),
        showlegend=False,
        hoverinfo='none'
    ))
    
    # Clean minimal layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='rgba(0,0,0,0)',
            camera=dict(eye=dict(x=1.8, y=1.8, z=1.8))
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=450,
        showlegend=False
    )
    
    return fig

def render_agent_card(agent_name: str, description: str, status: str, execution_time: float = 0):
    """Render elegant agent status card."""
    
    status_colors = {
        "idle": "#94A3B8",
        "running": "#F59E0B", 
        "completed": "#10B981",
        "error": "#EF4444"
    }
    
    status_icons = {
        "idle": "⚪",
        "running": "🟡",
        "completed": "✅", 
        "error": "❌"
    }
    
    color = status_colors.get(status, "#94A3B8")
    icon = status_icons.get(status, "⚪")
    
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.95);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    ">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <h3 style="
                margin: 0;
                color: #1F2937;
                font-size: 1.3rem;
                font-weight: 600;
            ">{icon} {agent_name}</h3>
            <span style="
                background: {color};
                color: white;
                padding: 0.4rem 1rem;
                border-radius: 25px;
                font-size: 0.85rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            ">{status}</span>
        </div>
        <p style="
            margin: 1rem 0 0 0;
            color: #6B7280;
            font-size: 1rem;
            line-height: 1.5;
        ">{description}</p>
        {f'<p style="margin: 1rem 0 0 0; color: #9CA3AF; font-size: 0.9rem; font-weight: 500;">⏱️ {execution_time:.1f}s</p>' if execution_time > 0 else ''}
    </div>
    """, unsafe_allow_html=True)

def render_metrics_dashboard(metrics: Dict):
    """Render elegant metrics dashboard."""
    
    st.markdown("### 📊 Performance Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    metrics_data = [
        ("Social Buzz", metrics.get("social_engagement", 0), "📱"),
        ("News Coverage", metrics.get("news_relevance", 0), "📰"),
        ("Tech Innovation", metrics.get("tech_innovation", 0), "💡"),
        ("Market Interest", metrics.get("market_interest", 0), "💰")
    ]
    
    for i, (label, value, icon) in enumerate(metrics_data):
        with [col1, col2, col3, col4][i]:
            render_metric_card(label, value, icon)

def render_metric_card(label: str, value: float, icon: str):
    """Render individual metric card."""
    
    # Determine color based on value
    if value >= 8:
        color = "#10B981"  # Green
        gradient = "linear-gradient(135deg, #10B981 0%, #34D399 100%)"
    elif value >= 5:
        color = "#F59E0B"  # Orange
        gradient = "linear-gradient(135deg, #F59E0B 0%, #FBBF24 100%)"
    else:
        color = "#EF4444"  # Red
        gradient = "linear-gradient(135deg, #EF4444 0%, #F87171 100%)"
    
    st.markdown(f"""
    <div style="
        background: {gradient};
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        color: white;
        margin: 0.5rem 0;
    ">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">{icon}</div>
        <div style="
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        ">{value}/10</div>
        <div style="
            font-size: 1rem;
            font-weight: 500;
            opacity: 0.9;
        ">{label}</div>
    </div>
    """, unsafe_allow_html=True)

def render_campaign_results_panel(results: Dict):
    """Render campaign results in elegant panel."""
    
    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 20px 60px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Campaign Intelligence Results")
    
    # Elegant tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Trends", "🧠 Analogies", "✨ Creative", "💰 Budget"])
    
    with tab1:
        if "trend_harvester" in results:
            trend_data = results["trend_harvester"]
            st.markdown("**Emerging Market Trends:**")
            st.write(trend_data.get("trends", "No trend data available"))
            
            if "trend_signals" in trend_data:
                render_metrics_dashboard(trend_data["trend_signals"])
    
    with tab2:
        if "analogical_reasoner" in results:
            analogy_data = results["analogical_reasoner"]
            st.markdown("**Brand-Trend Analogies:**")
            st.write(analogy_data.get("analogy", "No analogy data available"))
    
    with tab3:
        if "creative_synthesizer" in results:
            creative_data = results["creative_synthesizer"]
            st.markdown("**Generated Creative Content:**")
            st.write(creative_data.get("creative", "No creative content available"))
    
    with tab4:
        if "budget_optimizer" in results:
            budget_data = results["budget_optimizer"]
            st.markdown("**Budget Allocation:**")
            st.write(budget_data.get("allocation", "No budget data available"))
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_sidebar_navigation():
    """Render elegant sidebar navigation."""
    
    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 2rem 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    ">
        <h2 style="
            color: white;
            font-size: 1.8rem;
            font-weight: 600;
            text-align: center;
            margin: 0 0 1rem 0;
        ">🧠 Neural AdBrain</h2>
        <p style="
            color: rgba(255,255,255,0.8);
            margin: 0;
            font-size: 1rem;
            text-align: center;
            font-weight: 300;
        ">AI Campaign Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

def render_loading_animation():
    """Render elegant loading animation."""
    
    st.markdown("""
    <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 3rem;
    ">
        <div style="
            width: 60px;
            height: 60px;
            border: 4px solid rgba(255,255,255,0.3);
            border-top: 4px solid white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        "></div>
    </div>
    
    <style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)

def render_status_indicator(status: str, message: str = ""):
    """Render status indicator with message."""
    
    status_config = {
        "success": {"color": "#10B981", "icon": "✅", "bg": "rgba(16, 185, 129, 0.1)"},
        "warning": {"color": "#F59E0B", "icon": "⚠️", "bg": "rgba(245, 158, 11, 0.1)"},
        "error": {"color": "#EF4444", "icon": "❌", "bg": "rgba(239, 68, 68, 0.1)"},
        "info": {"color": "#3B82F6", "icon": "ℹ️", "bg": "rgba(59, 130, 246, 0.1)"}
    }
    
    config = status_config.get(status, status_config["info"])
    
    st.markdown(f"""
    <div style="
        background: {config['bg']};
        border: 2px solid {config['color']};
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        display: flex;
        align-items: center;
        backdrop-filter: blur(10px);
    ">
        <span style="
            font-size: 1.5rem;
            margin-right: 1rem;
        ">{config['icon']}</span>
        <span style="
            color: white;
            font-weight: 500;
            font-size: 1.1rem;
        ">{message}</span>
    </div>
    """, unsafe_allow_html=True)

def render_workflow_visualization(workflow_data: Dict):
    """Render elegant workflow visualization."""
    
    if not workflow_data or "nodes" not in workflow_data:
        st.info("No workflow data available")
        return
    
    # Create workflow graph visualization
    fig = go.Figure()
    
    nodes = workflow_data["nodes"]
    edges = workflow_data.get("edges", [])
    
    # Node styling
    node_colors = {
        "trigger": "#10B981",
        "agent": "#3B82F6", 
        "storage": "#8B5CF6",
        "output": "#F59E0B"
    }
    
    # Add workflow nodes and connections
    for i, node in enumerate(nodes):
        x_pos = i * 2
        y_pos = 0
        
        fig.add_trace(go.Scatter(
            x=[x_pos], y=[y_pos],
            mode='markers+text',
            marker=dict(
                size=30,
                color=node_colors.get(node.get("type", "agent"), "#6B7280"),
                line=dict(color='white', width=2)
            ),
            text=node.get("name", f"Node {i}"),
            textposition="bottom center",
            showlegend=False
        ))
    
    # Add connections
    for edge in edges:
        source_idx = edge.get("source", 0)
        target_idx = edge.get("target", 1)
        
        if source_idx < len(nodes) and target_idx < len(nodes):
            fig.add_trace(go.Scatter(
                x=[source_idx * 2, target_idx * 2],
                y=[0, 0],
                mode='lines',
                line=dict(color='rgba(255,255,255,0.5)', width=3),
                showlegend=False
            ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        margin=dict(l=0, r=0, t=0, b=0),
        height=200
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
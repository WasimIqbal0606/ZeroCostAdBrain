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
    """Render next-level cyberpunk advertising neural brain hero section."""
    
    # Advanced cyberpunk CSS for the hero section
    st.markdown("""
    <style>
    .cyber-hero-container {
        background: linear-gradient(135deg, #0D1B2A 0%, #1B263B 20%, #415A77 40%, #FF006E 70%, #FB5607 100%);
        padding: 4rem 2rem;
        border-radius: 0;
        margin: -1rem -1rem 2rem -1rem;
        color: white;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 0 50px rgba(255, 0, 110, 0.4),
            inset 0 1px 0 rgba(255,255,255,0.1);
        border-bottom: 2px solid rgba(255, 0, 110, 0.5);
    }
    .cyber-hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 80%, rgba(255, 0, 110, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(251, 86, 7, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(59, 130, 246, 0.1) 0%, transparent 50%);
        animation: cyberPulse 4s ease-in-out infinite alternate;
    }
    .cyber-title {
        font-size: 4rem;
        font-weight: 900;
        line-height: 1.1;
        margin: 0 0 1.5rem 0;
        background: linear-gradient(45deg, #FFFFFF, #FF006E, #FB5607, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(255, 0, 110, 0.8);
        letter-spacing: -2px;
        position: relative;
        z-index: 2;
    }
    .cyber-subtitle {
        font-size: 1.4rem;
        font-weight: 600;
        line-height: 1.6;
        margin: 1.5rem 0;
        color: rgba(255,255,255,0.95);
        max-width: 650px;
        text-shadow: 0 0 20px rgba(255, 0, 110, 0.6);
        position: relative;
        z-index: 2;
    }
    .cyber-button {
        background: linear-gradient(45deg, #FF006E, #FB5607);
        border: 2px solid rgba(255, 0, 110, 0.8);
        color: white;
        padding: 1.2rem 3rem;
        font-size: 1.2rem;
        font-weight: 700;
        border-radius: 50px;
        cursor: pointer;
        backdrop-filter: blur(15px);
        margin-top: 2rem;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        box-shadow: 0 0 30px rgba(255, 0, 110, 0.4);
        position: relative;
        z-index: 2;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .cyber-button:hover {
        background: linear-gradient(45deg, #FB5607, #FF006E);
        transform: translateY(-3px);
        box-shadow: 0 10px 40px rgba(255, 0, 110, 0.6);
    }
    @keyframes cyberPulse {
        0% { opacity: 0.6; transform: scale(1); }
        100% { opacity: 1; transform: scale(1.02); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create advertising neural network visualization
    fig = create_advertising_neural_network()
    
    # Hero section layout
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="cyber-hero-container">
            <h1 class="cyber-title">Neural AdBrain<br>Cybernetic Marketing<br>Intelligence</h1>
            <p class="cyber-subtitle">Revolutionary AI consciousness that harvests viral memes, crafts persuasive narratives, and optimizes campaigns through quantum-enhanced neural networks—transforming advertising into pure digital art.</p>
            <div class="cyber-button">Activate Neural Matrix →</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def create_advertising_neural_network():
    """Create cyberpunk advertising neural network visualization."""
    
    # Generate advertising-specific network structure
    nodes_x, nodes_y, nodes_z = [], [], []
    edges_x, edges_y, edges_z = [], [], []
    node_colors = []
    node_sizes = []
    node_names = []
    
    # Define advertising brain components
    ad_components = [
        {"name": "MemeHarvester", "color": "#FF006E", "size": 25, "pos": (0, 0, 1)},
        {"name": "NarrativeAligner", "color": "#FB5607", "size": 22, "pos": (0.8, 0, 0.6)},
        {"name": "CopyCrafter", "color": "#3B82F6", "size": 20, "pos": (-0.8, 0, 0.6)},
        {"name": "HookOptimizer", "color": "#10B981", "size": 18, "pos": (0.4, 0.7, 0)},
        {"name": "SequencePlanner", "color": "#8B5CF6", "size": 16, "pos": (-0.4, 0.7, 0)},
        {"name": "AnalyticsInterpreter", "color": "#F59E0B", "size": 15, "pos": (0, -0.8, 0)},
    ]
    
    # Add social data sources (input layer)
    social_sources = [
        {"name": "Twitter", "color": "#1DA1F2", "size": 12, "pos": (1.2, 0.4, -0.5)},
        {"name": "Reddit", "color": "#FF4500", "size": 12, "pos": (1.2, -0.4, -0.5)},
        {"name": "News", "color": "#4B5563", "size": 10, "pos": (0, 1.2, -0.5)},
        {"name": "Trends", "color": "#06B6D4", "size": 10, "pos": (-1.2, 0, -0.5)},
    ]
    
    # Add output channels
    output_channels = [
        {"name": "Facebook", "color": "#1877F2", "size": 14, "pos": (0.8, -1, 0.8)},
        {"name": "Instagram", "color": "#E4405F", "size": 14, "pos": (-0.8, -1, 0.8)},
        {"name": "LinkedIn", "color": "#0A66C2", "size": 12, "pos": (0, -1.4, 0.4)},
        {"name": "Email", "color": "#34D399", "size": 10, "pos": (1.4, -0.6, 0.2)},
    ]
    
    all_nodes = ad_components + social_sources + output_channels
    
    # Create nodes
    for node in all_nodes:
        x, y, z = node["pos"]
        nodes_x.append(x)
        nodes_y.append(y)
        nodes_z.append(z)
        node_colors.append(node["color"])
        node_sizes.append(node["size"])
        node_names.append(node["name"])
    
    # Create connections (neural pathways)
    connections = [
        # Social sources to processing agents
        (6, 0), (7, 0), (8, 1), (9, 2),  # Sources to agents
        (6, 2), (7, 1), (8, 3), (9, 4),  # Cross connections
        # Agent interconnections
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5),  # Sequential flow
        (0, 3), (1, 4), (2, 5),  # Skip connections
        (0, 5), (1, 3),  # Feedback loops
        # Agents to output channels
        (3, 10), (4, 11), (5, 12), (2, 13),  # To outputs
        (0, 10), (1, 11),  # Direct connections
    ]
    
    for start, end in connections:
        edges_x.extend([nodes_x[start], nodes_x[end], None])
        edges_y.extend([nodes_y[start], nodes_y[end], None])
        edges_z.extend([nodes_z[start], nodes_z[end], None])
    
    # Create 3D scatter plot for nodes
    node_trace = go.Scatter3d(
        x=nodes_x, y=nodes_y, z=nodes_z,
        mode='markers+text',
        marker=dict(
            size=node_sizes,
            color=node_colors,
            opacity=0.9,
            line=dict(width=2, color='rgba(255,255,255,0.8)')
        ),
        text=node_names,
        textposition="middle center",
        textfont=dict(size=8, color="white"),
        hovertemplate='<b>%{text}</b><br>' +
                      'Neural Node: %{text}<br>' +
                      '<extra></extra>',
        name="Neural Nodes"
    )
    
    # Create 3D line plot for edges (neural pathways)
    edge_trace = go.Scatter3d(
        x=edges_x, y=edges_y, z=edges_z,
        mode='lines',
        line=dict(color='rgba(255, 0, 110, 0.6)', width=3),
        hoverinfo='none',
        name="Neural Pathways"
    )
    
    # Create the figure
    fig = go.Figure(data=[edge_trace, node_trace])
    
    # Update layout for cyberpunk aesthetic
    fig.update_layout(
        title="",
        showlegend=False,
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            bgcolor='rgba(13, 27, 42, 0.8)',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=400,
        font=dict(color="white")
    )
    
    return fig

def render_agent_card(agent_name: str, description: str, status: str, execution_time: float = 0):
    """Render next-level cyberpunk agent status card."""
    
    # Cyberpunk status colors and icons
    status_config = {
        'waiting': {'color': '#415A77', 'icon': '◯', 'bg': 'rgba(65, 90, 119, 0.15)', 'glow': 'rgba(65, 90, 119, 0.4)'},
        'running': {'color': '#FF006E', 'icon': '◐', 'bg': 'rgba(255, 0, 110, 0.15)', 'glow': 'rgba(255, 0, 110, 0.6)'},
        'completed': {'color': '#00F5FF', 'icon': '●', 'bg': 'rgba(0, 245, 255, 0.15)', 'glow': 'rgba(0, 245, 255, 0.6)'},
        'error': {'color': '#FB5607', 'icon': '⚡', 'bg': 'rgba(251, 86, 7, 0.15)', 'glow': 'rgba(251, 86, 7, 0.6)'}
    }
    
    config = status_config.get(status, status_config['waiting'])
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(13, 27, 42, 0.8), {config['bg']});
        border: 1px solid {config['color']}80;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.8rem 0;
        backdrop-filter: blur(20px);
        box-shadow: 
            0 8px 32px rgba(0,0,0,0.3),
            0 0 0 1px {config['glow']},
            inset 0 1px 0 rgba(255,255,255,0.1);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 50% 50%, {config['glow']} 0%, transparent 70%);
            opacity: 0.1;
            animation: pulse 2s ease-in-out infinite alternate;
        "></div>
        
        <div style="display: flex; align-items: center; gap: 1.5rem; position: relative; z-index: 2;">
            <div style="
                font-size: 2rem;
                color: {config['color']};
                width: 50px;
                height: 50px;
                display: flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, {config['bg']}, rgba(0,0,0,0.3));
                border-radius: 50%;
                border: 2px solid {config['color']};
                box-shadow: 0 0 20px {config['glow']};
                text-shadow: 0 0 10px {config['color']};
            ">{config['icon']}</div>
            <div style="flex: 1;">
                <div style="
                    font-size: 1.3rem;
                    font-weight: 700;
                    color: {config['color']};
                    margin-bottom: 0.5rem;
                    text-shadow: 0 0 10px {config['glow']};
                    letter-spacing: 0.5px;
                ">{agent_name}</div>
                <div style="
                    font-size: 1rem;
                    color: rgba(255,255,255,0.9);
                    line-height: 1.5;
                    text-shadow: 0 1px 2px rgba(0,0,0,0.5);
                ">{description}</div>
                {f'<div style="font-size: 0.9rem; color: {config["color"]}; margin-top: 0.5rem; font-weight: 600;">Neural processing: {execution_time:.1f}s</div>' if status == 'completed' else ''}
            </div>
        </div>
    </div>
    
    <style>
        @keyframes pulse {{
            0% {{ opacity: 0.1; transform: scale(1); }}
            100% {{ opacity: 0.3; transform: scale(1.05); }}
        }}
    </style>
    """, unsafe_allow_html=True)

def render_metrics_dashboard(metrics: Dict):
    """Render cyberpunk metrics dashboard."""
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_metric_card("Viral Potential", metrics.get('viral_score', 85), "🔥")
    with col2:
        render_metric_card("Neural Accuracy", metrics.get('accuracy', 94), "🎯")
    with col3:
        render_metric_card("Trend Velocity", metrics.get('trend_velocity', 78), "⚡")
    with col4:
        render_metric_card("ROI Prediction", metrics.get('roi_prediction', 156), "💎")

def render_metric_card(label: str, value: float, icon: str):
    """Render cyberpunk metric card."""
    
    # Determine color based on value ranges
    if value >= 90:
        color = "#00F5FF"
        glow = "rgba(0, 245, 255, 0.6)"
    elif value >= 70:
        color = "#FF006E"
        glow = "rgba(255, 0, 110, 0.6)"
    else:
        color = "#FB5607"
        glow = "rgba(251, 86, 7, 0.6)"
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(13, 27, 42, 0.9), rgba(27, 38, 59, 0.8));
        border: 2px solid {color}80;
        border-radius: 20px;
        padding: 2rem 1.5rem;
        text-align: center;
        backdrop-filter: blur(25px);
        box-shadow: 
            0 10px 40px rgba(0,0,0,0.4),
            0 0 0 1px {glow},
            inset 0 2px 0 rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
        transform: translateY(0);
        transition: all 0.4s ease;
    ">
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 50% 20%, {glow} 0%, transparent 60%);
            opacity: 0.15;
        "></div>
        
        <div style="position: relative; z-index: 2;">
            <div style="
                font-size: 3rem;
                margin-bottom: 1rem;
                text-shadow: 0 0 15px {color};
            ">{icon}</div>
            <div style="
                font-size: 2.5rem;
                font-weight: 900;
                color: {color};
                margin-bottom: 0.5rem;
                text-shadow: 0 0 20px {glow};
                letter-spacing: -1px;
            ">{value}{'%' if value < 10 else ''}</div>
            <div style="
                font-size: 1rem;
                color: rgba(255,255,255,0.8);
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 1px;
                text-shadow: 0 1px 2px rgba(0,0,0,0.5);
            ">{label}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_campaign_results_panel(results: Dict):
    """Render cyberpunk campaign results panel."""
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(13, 27, 42, 0.95), rgba(27, 38, 59, 0.9));
        border: 2px solid rgba(255, 0, 110, 0.6);
        border-radius: 24px;
        padding: 2.5rem;
        margin: 2rem 0;
        backdrop-filter: blur(30px);
        box-shadow: 
            0 15px 50px rgba(0,0,0,0.5),
            0 0 0 1px rgba(255, 0, 110, 0.3),
            inset 0 2px 0 rgba(255,255,255,0.1);
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 80%, rgba(255, 0, 110, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(0, 245, 255, 0.1) 0%, transparent 50%);
            animation: resultsPulse 3s ease-in-out infinite alternate;
        "></div>
        
        <div style="position: relative; z-index: 2;">
            <h3 style="
                color: #00F5FF;
                font-size: 2.2rem;
                font-weight: 900;
                margin-bottom: 2rem;
                text-align: center;
                text-shadow: 0 0 25px rgba(0, 245, 255, 0.8);
                letter-spacing: 1px;
            ">Neural Campaign Results</h3>
        </div>
    </div>
    
    <style>
        @keyframes resultsPulse {
            0% { opacity: 0.8; transform: scale(1); }
            100% { opacity: 1; transform: scale(1.02); }
        }
    </style>
    """, unsafe_allow_html=True)

def render_sidebar_navigation():
    """Render cyberpunk sidebar navigation."""
    
    st.sidebar.markdown("""
    <style>
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, rgba(13, 27, 42, 0.95), rgba(27, 38, 59, 0.9));
            border-right: 2px solid rgba(255, 0, 110, 0.4);
        }
        .sidebar .sidebar-content .block-container {
            padding-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

def render_loading_animation():
    """Render cyberpunk loading animation."""
    
    st.markdown("""
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 3rem;
        background: linear-gradient(135deg, rgba(13, 27, 42, 0.8), rgba(27, 38, 59, 0.6));
        border-radius: 20px;
        margin: 2rem 0;
        border: 1px solid rgba(255, 0, 110, 0.3);
    ">
        <div style="
            width: 60px;
            height: 60px;
            border: 4px solid rgba(255, 0, 110, 0.3);
            border-top: 4px solid #FF006E;
            border-radius: 50%;
            animation: cyberSpin 1s linear infinite;
        "></div>
    </div>
    
    <style>
        @keyframes cyberSpin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
    """, unsafe_allow_html=True)

def render_status_indicator(status: str, message: str = ""):
    """Render cyberpunk status indicator."""
    
    colors = {
        'success': '#00F5FF',
        'warning': '#FF006E', 
        'error': '#FB5607',
        'info': '#3B82F6'
    }
    
    color = colors.get(status, '#00F5FF')
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(13, 27, 42, 0.9), rgba(27, 38, 59, 0.8));
        border: 2px solid {color}80;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3), 0 0 0 1px {color}40;
    ">
        <div style="
            color: {color};
            font-weight: 700;
            font-size: 1.1rem;
            text-shadow: 0 0 10px {color}80;
        ">{status.upper()}: {message}</div>
    </div>
    """, unsafe_allow_html=True)
    
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
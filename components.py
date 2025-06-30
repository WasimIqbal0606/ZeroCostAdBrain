"""
Next-level cyberpunk UI components for the Neural AdBrain platform.
Implements cutting-edge design with advertising-focused neural network visualization.
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
    /* Input fields with glow */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        backdrop-filter: blur(10px) !important;
    }

    /* Ensure proper form labeling */
    .stTextInput > label,
    .stSelectbox > label,
    .stTextArea > label {
        color: white !important;
        font-weight: 600 !important;
    }

    /* Button gradient animation */
    .gradient-button {
        text-decoration: none;
        padding: 15px 30px;
        text-align: center;
        letter-spacing: 1px;
        transition: 0.3s;
    }

    /* Add a glow effect on hover */
    .gradient-button:hover {
        box-shadow: 0 0 20px rgba(100, 255, 218, 0.6);
    }

    /* Keyframes for background gradient shift */
    @keyframes gradientShift {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    /* Apply the gradient animation */
    .animated-gradient {
        animation: gradientShift 8s ease infinite;
        background: linear-gradient(270deg, #00bcd4, #4caf50, #009688);
        background-size: 200% 200%;
    }

    /* Button-specific gradient animation */
    @keyframes buttonGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glow effect animation */
    @keyframes textGlow {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }

    /* Floating animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
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
    """Render professional React-style agent status card with better visibility."""

    # Professional status colors and icons with better contrast
    status_config = {
        'waiting': {'color': '#6366F1', 'icon': '○', 'bg': 'rgba(99, 102, 241, 0.1)', 'border': '#6366F1'},
        'running': {'color': '#F59E0B', 'icon': '●', 'bg': 'rgba(245, 158, 11, 0.1)', 'border': '#F59E0B'},
        'completed': {'color': '#10B981', 'icon': '✓', 'bg': 'rgba(16, 185, 129, 0.1)', 'border': '#10B981'},
        'error': {'color': '#EF4444', 'icon': '✗', 'bg': 'rgba(239, 68, 68, 0.1)', 'border': '#EF4444'},
        'idle': {'color': '#6B7280', 'icon': '○', 'bg': 'rgba(107, 114, 128, 0.1)', 'border': '#6B7280'}
    }

    config = status_config.get(status, status_config['waiting'])

    # Professional React-style component with JavaScript interactivity
    component_id = f"agent-card-{hash(agent_name)}"
    
    html_content = f"""
    <div id="{component_id}" class="agent-card" style="
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid {config['border']};
        border-radius: 12px;
        padding: 20px;
        margin: 16px 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    ">
        <!-- Status indicator stripe -->
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: {config['color']};
        "></div>
        
        <!-- Main content -->
        <div style="
            display: flex;
            align-items: center;
            gap: 16px;
            margin-left: 8px;
        ">
            <!-- Status icon -->
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                width: 48px;
                height: 48px;
                border-radius: 50%;
                background: {config['bg']};
                border: 2px solid {config['color']};
                font-size: 20px;
                font-weight: bold;
                color: {config['color']};
            ">{config['icon']}</div>
            
            <!-- Agent info -->
            <div style="flex: 1;">
                <div style="
                    font-size: 18px;
                    font-weight: 600;
                    color: #1F2937;
                    margin-bottom: 4px;
                    letter-spacing: -0.025em;
                ">{agent_name}</div>
                <div style="
                    font-size: 14px;
                    color: #6B7280;
                    line-height: 1.5;
                ">{description}</div>
                {f'<div style="font-size: 12px; color: {config["color"]}; margin-top: 8px; font-weight: 500;">Completed in {execution_time:.1f}s</div>' if status == 'completed' else ''}
            </div>
            
            <!-- Status badge -->
            <div style="
                padding: 6px 12px;
                border-radius: 20px;
                background: {config['color']};
                color: white;
                font-size: 12px;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            ">{status}</div>
        </div>
    </div>
    
    <script>
        (function() {{
            const card = document.getElementById('{component_id}');
            if (card) {{
                // Add hover effects
                card.addEventListener('mouseenter', function() {{
                    this.style.transform = 'translateY(-2px)';
                    this.style.boxShadow = '0 8px 30px rgba(0, 0, 0, 0.15)';
                }});
                
                card.addEventListener('mouseleave', function() {{
                    this.style.transform = 'translateY(0)';
                    this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
                }});
                
                // Add click animation
                card.addEventListener('click', function() {{
                    this.style.transform = 'scale(0.98)';
                    setTimeout(() => {{
                        this.style.transform = 'translateY(-2px)';
                    }}, 100);
                }});
                
                // Add status-specific animations
                if ('{status}' === 'running') {{
                    const icon = card.querySelector('div:nth-child(2) > div:first-child');
                    if (icon) {{
                        icon.style.animation = 'pulse 2s infinite';
                    }}
                }}
            }}
        }})();
    </script>
    
    <style>
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        
        .agent-card:hover {{
            border-color: {config['color']} !important;
        }}
    </style>
    """
    
    st.markdown(html_content, unsafe_allow_html=True)

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
    """Render professional React-style metric card with better visibility."""

    # Professional color scheme based on value ranges
    if value >= 90:
        color = "#10B981"  # Green
        bg_color = "rgba(16, 185, 129, 0.1)"
    elif value >= 70:
        color = "#3B82F6"  # Blue
        bg_color = "rgba(59, 130, 246, 0.1)"
    elif value >= 50:
        color = "#F59E0B"  # Amber
        bg_color = "rgba(245, 158, 11, 0.1)"
    else:
        color = "#EF4444"  # Red
        bg_color = "rgba(239, 68, 68, 0.1)"

    card_id = f"metric-card-{hash(label)}"
    
    st.markdown(f"""
    <div id="{card_id}" class="metric-card" style="
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid {color};
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
        min-height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    ">
        <!-- Background accent -->
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, {color}, {color}80);
        "></div>
        
        <!-- Icon -->
        <div style="
            font-size: 32px;
            margin-bottom: 12px;
            filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        ">{icon}</div>
        
        <!-- Value -->
        <div style="
            font-size: 36px;
            font-weight: 700;
            color: {color};
            margin-bottom: 8px;
            line-height: 1;
            letter-spacing: -0.025em;
        ">{value:.1f}{'%' if value <= 100 else ''}</div>
        
        <!-- Label -->
        <div style="
            font-size: 14px;
            color: #6B7280;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            line-height: 1.2;
            ">{label}</div>
        
        <!-- Progress indicator -->
        <div style="
            position: absolute;
            bottom: 0;
            left: 0;
            width: {min(value, 100)}%;
            height: 3px;
            background: {color};
            transition: width 1.5s ease-out;
        "></div>
    </div>
    
    <script>
        (function() {{
            const card = document.getElementById('{card_id}');
            if (card) {{
                // Add hover effects
                card.addEventListener('mouseenter', function() {{
                    this.style.transform = 'translateY(-4px) scale(1.02)';
                    this.style.boxShadow = '0 12px 40px rgba(0, 0, 0, 0.15)';
                    this.style.borderColor = '{color}';
                }});
                
                card.addEventListener('mouseleave', function() {{
                    this.style.transform = 'translateY(0) scale(1)';
                    this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
                }});
                
                // Add click animation
                card.addEventListener('click', function() {{
                    this.style.transform = 'translateY(-2px) scale(0.98)';
                    setTimeout(() => {{
                        this.style.transform = 'translateY(-4px) scale(1.02)';
                    }}, 150);
                }});
            }}
        }})();
    </script>
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

def render_workflow_visualization(workflow_data: Dict):
    """Render cyberpunk workflow visualization."""

    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(13, 27, 42, 0.9), rgba(27, 38, 59, 0.8));
        border: 2px solid rgba(0, 245, 255, 0.6);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        backdrop-filter: blur(25px);
        box-shadow: 
            0 12px 40px rgba(0,0,0,0.4),
            0 0 0 1px rgba(0, 245, 255, 0.3),
            inset 0 2px 0 rgba(255,255,255,0.1);
    ">
        <h3 style="
            color: #00F5FF;
            font-size: 1.8rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            text-align: center;
            text-shadow: 0 0 20px rgba(0, 245, 255, 0.8);
        ">Neural Workflow Execution</h3>
    </div>
    """, unsafe_allow_html=True)

# The following function was not in the original code, but it is needed based on the instructions.
def render_campaign_form():
    """Renders a form for creating a campaign."""
    # Campaign form with elegant styling
    col1, col2 = st.columns([2, 1])

    with col1:
        # Main campaign inputs
        topic = st.text_input(
            "Campaign Topic/Product",
            placeholder="e.g., Sustainable Fashion, AI Productivity Tools, Electric Vehicles",
            help="The main product or service you want to advertise",
            key="campaign_topic_input"
        )

        brand = st.text_input(
            "Brand Name",
            placeholder="e.g., EcoWear, TechFlow, GreenDrive",
            help="Your brand or company name",
            key="brand_name_input"
        )
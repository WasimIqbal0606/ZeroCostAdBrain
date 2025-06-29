"""
Next.js-style UI components for the multi-agent advertising brain app.
Implements modern big tech company design patterns with 3D neural network visuals.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from typing import Dict, List, Any
import json

def render_neural_network_background():
    """Render 3D neural network background visualization."""
    
    # Create 3D neural network nodes
    np.random.seed(42)
    n_layers = 5
    nodes_per_layer = [8, 12, 16, 12, 6]
    
    x, y, z = [], [], []
    node_colors = []
    
    for layer_idx, n_nodes in enumerate(nodes_per_layer):
        layer_x = layer_idx * 2
        for node_idx in range(n_nodes):
            x.append(layer_x)
            y.append((node_idx - n_nodes/2) * 0.8)
            z.append(np.random.uniform(-1, 1))
            node_colors.append(layer_idx)
    
    # Create connections
    edge_x, edge_y, edge_z = [], [], []
    start_idx = 0
    
    for layer_idx in range(len(nodes_per_layer) - 1):
        current_layer_size = nodes_per_layer[layer_idx]
        next_layer_size = nodes_per_layer[layer_idx + 1]
        
        for i in range(current_layer_size):
            for j in range(next_layer_size):
                if np.random.random() > 0.3:  # Sparse connections
                    current_idx = start_idx + i
                    next_idx = start_idx + current_layer_size + j
                    
                    edge_x.extend([x[current_idx], x[next_idx], None])
                    edge_y.extend([y[current_idx], y[next_idx], None])
                    edge_z.extend([z[current_idx], z[next_idx], None])
        
        start_idx += current_layer_size
    
    # Create 3D plot
    fig = go.Figure()
    
    # Add edges
    fig.add_trace(go.Scatter3d(
        x=edge_x, y=edge_y, z=edge_z,
        mode='lines',
        line=dict(color='rgba(255, 107, 53, 0.3)', width=2),
        showlegend=False,
        hoverinfo='none'
    ))
    
    # Add nodes
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=8,
            color=node_colors,
            colorscale='Oranges',
            opacity=0.8,
            line=dict(color='white', width=2)
        ),
        showlegend=False,
        hoverinfo='none'
    ))
    
    # Update layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(showgrid=False, showticklabels=False, title=''),
            yaxis=dict(showgrid=False, showticklabels=False, title=''),
            zaxis=dict(showgrid=False, showticklabels=False, title=''),
            bgcolor='rgba(30, 30, 30, 0.1)',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        paper_bgcolor='rgba(30, 30, 30, 0)',
        plot_bgcolor='rgba(30, 30, 30, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=400,
        showlegend=False
    )
    
    return fig

def render_hero_section():
    """Render big tech style hero section."""
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #2D2D2D 0%, #1E1E1E 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
        border: 1px solid rgba(255, 107, 53, 0.2);
    ">
        <h1 style="
            color: #FF6B35;
            font-size: 3.5rem;
            font-weight: 700;
            margin: 0;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        ">🧠 Neural AdBrain</h1>
        <p style="
            color: rgba(255,255,255,0.9);
            font-size: 1.3rem;
            text-align: center;
            margin: 1rem 0 0 0;
            font-weight: 300;
        ">Enterprise Multi-Agent AI Platform for Campaign Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

def render_agent_card(agent_name: str, description: str, status: str, execution_time: float = 0):
    """Render Next.js style agent status card."""
    
    status_colors = {
        "idle": "#6B7280",
        "running": "#F59E0B", 
        "completed": "#10B981",
        "error": "#EF4444"
    }
    
    status_icons = {
        "idle": "⚪",
        "running": "🟡",
        "completed": "🟢", 
        "error": "🔴"
    }
    
    color = status_colors.get(status, "#6B7280")
    icon = status_icons.get(status, "⚪")
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #2D2D2D 0%, #1E1E1E 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(255, 107, 53, 0.1);
        border-left: 4px solid {color};
        border: 1px solid rgba(255, 107, 53, 0.2);
        transition: all 0.3s ease;
    ">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <h3 style="
                margin: 0;
                color: #FFFFFF;
                font-size: 1.2rem;
                font-weight: 600;
            ">{icon} {agent_name}</h3>
            <span style="
                background: {color};
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: 500;
            ">{status.upper()}</span>
        </div>
        <p style="
            margin: 0.5rem 0 0 0;
            color: #CCCCCC;
            font-size: 0.9rem;
            line-height: 1.4;
        ">{description}</p>
        {f'<p style="margin: 0.5rem 0 0 0; color: #999999; font-size: 0.8rem;">⏱️ {execution_time:.1f}s</p>' if execution_time > 0 else ''}
    </div>
    """, unsafe_allow_html=True)

def render_workflow_visualization(workflow_data: Dict):
    """Render N8N-style workflow visualization."""
    
    if not workflow_data or "nodes" not in workflow_data:
        st.info("No workflow data available")
        return
    
    # Create workflow graph
    fig = go.Figure()
    
    nodes = workflow_data["nodes"]
    edges = workflow_data.get("edges", [])
    
    # Node positions and colors
    node_colors = {
        "trigger": "#10B981",
        "agent": "#3B82F6", 
        "storage": "#8B5CF6",
        "output": "#F59E0B"
    }
    
    for node in nodes:
        color = node_colors.get(node["type"], "#6B7280")
        
        fig.add_trace(go.Scatter(
            x=[node["position"]["x"]],
            y=[node["position"]["y"]],
            mode='markers+text',
            marker=dict(
                size=40,
                color=color,
                line=dict(color='white', width=3)
            ),
            text=node["label"],
            textposition="bottom center",
            textfont=dict(size=10, color='#1F2937'),
            name=node["label"],
            showlegend=False,
            hovertemplate=f"<b>{node['label']}</b><br>Type: {node['type']}<br>Status: {node['status']}<extra></extra>"
        ))
    
    # Add edges
    for edge in edges:
        from_node = next((n for n in nodes if n["id"] == edge["from"]), None)
        to_node = next((n for n in nodes if n["id"] == edge["to"]), None)
        
        if from_node and to_node:
            fig.add_trace(go.Scatter(
                x=[from_node["position"]["x"], to_node["position"]["x"]],
                y=[from_node["position"]["y"], to_node["position"]["y"]],
                mode='lines',
                line=dict(color='#D1D5DB', width=2),
                showlegend=False,
                hoverinfo='skip'
            ))
    
    fig.update_layout(
        title="Workflow Execution Graph",
        title_font=dict(size=16, color='#1F2937'),
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        plot_bgcolor='rgba(255, 244, 230, 0.3)',
        paper_bgcolor='white',
        margin=dict(l=20, r=20, t=40, b=20),
        height=400
    )
    
    return fig

def render_metrics_dashboard(metrics: Dict):
    """Render big tech style metrics dashboard."""
    
    col1, col2, col3, col4 = st.columns(4)
    
    metrics_data = [
        ("Social Momentum", metrics.get("social_momentum", 0), "📈"),
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
    elif value >= 5:
        color = "#F59E0B"  # Yellow
    else:
        color = "#EF4444"  # Red
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #2D2D2D 0%, #1E1E1E 100%);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(255, 107, 53, 0.1);
        border: 1px solid rgba(255, 107, 53, 0.2);
    ">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="
            font-size: 2rem;
            font-weight: 700;
            color: {color};
            margin-bottom: 0.25rem;
        ">{value}/10</div>
        <div style="
            font-size: 0.9rem;
            color: #FFFFFF;
            font-weight: 500;
        ">{label}</div>
    </div>
    """, unsafe_allow_html=True)

def render_campaign_results_panel(results: Dict):
    """Render campaign results in big tech style panel."""
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #2D2D2D 0%, #1E1E1E 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 24px rgba(255, 107, 53, 0.1);
        border: 1px solid rgba(255, 107, 53, 0.2);
    ">
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Campaign Intelligence Results")
    
    # Tabs for different result types
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
            
            if "similar_analogies" in analogy_data and analogy_data["similar_analogies"]:
                st.markdown("**Similar Historical Analogies:**")
                for similar in analogy_data["similar_analogies"]:
                    st.write(f"• **{similar['trend']} × {similar['brand']}** (Similarity: {similar['similarity']:.2f})")
    
    with tab3:
        if "creative_synthesizer" in results:
            creative_data = results["creative_synthesizer"]
            st.markdown("**Generated Creative Content:**")
            st.write(creative_data.get("creative_content", "No creative content available"))
    
    with tab4:
        if "budget_optimizer" in results:
            budget_data = results["budget_optimizer"]
            st.markdown("**Budget Optimization Plan:**")
            st.write(budget_data.get("optimization_plan", "No budget data available"))
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_sidebar_navigation():
    """Render Next.js style sidebar navigation."""
    
    st.sidebar.markdown("""
    <div style="
        background: linear-gradient(180deg, #FF6B35 0%, #F7931E 100%);
        padding: 1.5rem;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 16px 16px;
    ">
        <h2 style="
            color: white;
            margin: 0;
            font-size: 1.5rem;
            font-weight: 600;
            text-align: center;
        ">🧠 Neural AdBrain</h2>
        <p style="
            color: rgba(255,255,255,0.8);
            margin: 0.5rem 0 0 0;
            font-size: 0.9rem;
            text-align: center;
        ">AI Campaign Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

def render_loading_animation():
    """Render big tech style loading animation."""
    
    st.markdown("""
    <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    ">
        <div style="
            width: 50px;
            height: 50px;
            border: 4px solid #2D2D2D;
            border-top: 4px solid #FF6B35;
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
        "success": {"color": "#10B981", "icon": "✅", "bg": "#ECFDF5"},
        "warning": {"color": "#F59E0B", "icon": "⚠️", "bg": "#FFFBEB"},
        "error": {"color": "#EF4444", "icon": "❌", "bg": "#FEF2F2"},
        "info": {"color": "#3B82F6", "icon": "ℹ️", "bg": "#EFF6FF"}
    }
    
    config = status_config.get(status, status_config["info"])
    
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #2D2D2D 0%, #1E1E1E 100%);
        border: 1px solid {config['color']};
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        display: flex;
        align-items: center;
    ">
        <span style="
            font-size: 1.2rem;
            margin-right: 0.75rem;
        ">{config['icon']}</span>
        <span style="
            color: #FFFFFF;
            font-weight: 500;
        ">{message}</span>
    </div>
    """, unsafe_allow_html=True)
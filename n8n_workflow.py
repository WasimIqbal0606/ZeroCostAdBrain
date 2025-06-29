"""
N8N-style workflow orchestration for multi-agent advertising brain.
Implements big tech company workflow patterns and visual orchestration.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
import asyncio
import uuid

logger = logging.getLogger(__name__)

class WorkflowNode:
    """Represents a single node in the workflow graph."""
    
    def __init__(self, node_id: str, node_type: str, name: str, parameters: Dict = None):
        self.id = node_id
        self.type = node_type
        self.name = name
        self.parameters = parameters or {}
        self.position = {"x": 0, "y": 0}
        self.connections = []
        self.status = "idle"  # idle, running, completed, error
        self.output_data = None
        self.execution_time = 0
        
    def connect_to(self, target_node: 'WorkflowNode'):
        """Connect this node to another node."""
        self.connections.append(target_node.id)
        
    def to_dict(self) -> Dict:
        """Convert node to dictionary representation."""
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "parameters": self.parameters,
            "position": self.position,
            "connections": self.connections,
            "status": self.status,
            "execution_time": self.execution_time
        }

class N8NWorkflowEngine:
    """N8N-style workflow execution engine for AI agents."""
    
    def __init__(self):
        self.workflows = {}
        self.execution_history = []
        
    def create_advertising_workflow(self) -> str:
        """Create the main advertising brain workflow."""
        workflow_id = str(uuid.uuid4())
        
        # Define workflow nodes
        nodes = [
            WorkflowNode("start", "trigger", "Campaign Trigger", {"trigger_type": "manual"}),
            WorkflowNode("trend_harvest", "agent", "Trend Harvester", {"agent_type": "TrendHarvester"}),
            WorkflowNode("analogy_reason", "agent", "Analogical Reasoner", {"agent_type": "AnalogicalReasoner"}),
            WorkflowNode("creative_synth", "agent", "Creative Synthesizer", {"agent_type": "CreativeSynthesizer"}),
            WorkflowNode("budget_opt", "agent", "Budget Optimizer", {"agent_type": "BudgetOptimizer"}),
            WorkflowNode("personalize", "agent", "Personalization Agent", {"agent_type": "PersonalizationAgent"}),
            WorkflowNode("save_results", "storage", "Save Campaign", {"storage_type": "campaign_manager"}),
            WorkflowNode("end", "output", "Campaign Complete", {"output_type": "dashboard"})
        ]
        
        # Set positions for visual layout
        positions = [
            {"x": 100, "y": 200},  # start
            {"x": 300, "y": 100},  # trend_harvest
            {"x": 500, "y": 150},  # analogy_reason
            {"x": 700, "y": 100},  # creative_synth
            {"x": 500, "y": 250},  # budget_opt
            {"x": 700, "y": 300},  # personalize
            {"x": 900, "y": 200},  # save_results
            {"x": 1100, "y": 200}  # end
        ]
        
        for i, node in enumerate(nodes):
            node.position = positions[i]
        
        # Connect nodes
        nodes[0].connect_to(nodes[1])  # start -> trend_harvest
        nodes[1].connect_to(nodes[2])  # trend_harvest -> analogy_reason
        nodes[2].connect_to(nodes[3])  # analogy_reason -> creative_synth
        nodes[1].connect_to(nodes[4])  # trend_harvest -> budget_opt (parallel)
        nodes[2].connect_to(nodes[5])  # analogy_reason -> personalize (parallel)
        nodes[3].connect_to(nodes[6])  # creative_synth -> save_results
        nodes[4].connect_to(nodes[6])  # budget_opt -> save_results
        nodes[5].connect_to(nodes[6])  # personalize -> save_results
        nodes[6].connect_to(nodes[7])  # save_results -> end
        
        workflow = {
            "id": workflow_id,
            "name": "Multi-Agent Advertising Brain",
            "description": "Enterprise workflow for AI-powered campaign creation",
            "nodes": {node.id: node for node in nodes},
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "execution_count": 0
        }
        
        self.workflows[workflow_id] = workflow
        return workflow_id
    
    async def execute_workflow(self, workflow_id: str, input_data: Dict) -> Dict:
        """Execute a workflow with given input data."""
        if workflow_id not in self.workflows:
            raise ValueError(f"Workflow {workflow_id} not found")
        
        workflow = self.workflows[workflow_id]
        execution_id = str(uuid.uuid4())
        
        execution_context = {
            "execution_id": execution_id,
            "workflow_id": workflow_id,
            "input_data": input_data,
            "start_time": datetime.now(),
            "status": "running",
            "results": {},
            "node_outputs": {}
        }
        
        try:
            # Execute nodes in topological order
            await self._execute_node_sequence(workflow, execution_context)
            
            execution_context["status"] = "completed"
            execution_context["end_time"] = datetime.now()
            
        except Exception as e:
            execution_context["status"] = "error"
            execution_context["error"] = str(e)
            execution_context["end_time"] = datetime.now()
            logger.error(f"Workflow execution error: {e}")
        
        # Save execution history
        self.execution_history.append(execution_context)
        workflow["execution_count"] += 1
        
        return execution_context
    
    async def _execute_node_sequence(self, workflow: Dict, context: Dict):
        """Execute workflow nodes in sequence."""
        nodes = workflow["nodes"]
        
        # Start with trigger node
        start_node = None
        for node in nodes.values():
            if node.type == "trigger":
                start_node = node
                break
        
        if not start_node:
            raise ValueError("No trigger node found in workflow")
        
        # Execute nodes
        await self._execute_node(start_node, workflow, context)
    
    async def _execute_node(self, node: WorkflowNode, workflow: Dict, context: Dict):
        """Execute a single workflow node."""
        node.status = "running"
        start_time = datetime.now()
        
        try:
            if node.type == "trigger":
                # Trigger node just passes input data
                output = context["input_data"]
                
            elif node.type == "agent":
                # Execute AI agent
                output = await self._execute_agent_node(node, context)
                
            elif node.type == "storage":
                # Save data
                output = await self._execute_storage_node(node, context)
                
            elif node.type == "output":
                # Final output node
                output = {"status": "completed", "results": context["results"]}
                
            else:
                output = {"status": "skipped", "reason": f"Unknown node type: {node.type}"}
            
            node.output_data = output
            context["node_outputs"][node.id] = output
            node.status = "completed"
            
            # Execute connected nodes
            for connection_id in node.connections:
                if connection_id in workflow["nodes"]:
                    connected_node = workflow["nodes"][connection_id]
                    await self._execute_node(connected_node, workflow, context)
            
        except Exception as e:
            node.status = "error"
            node.output_data = {"error": str(e)}
            logger.error(f"Node {node.id} execution error: {e}")
        
        finally:
            end_time = datetime.now()
            node.execution_time = (end_time - start_time).total_seconds()
    
    async def _execute_agent_node(self, node: WorkflowNode, context: Dict) -> Dict:
        """Execute an AI agent node."""
        agent_type = node.parameters.get("agent_type")
        
        # This would integrate with your existing agents
        # For now, return a placeholder that matches your agent structure
        return {
            "agent": agent_type,
            "status": "completed",
            "execution_time": 2.5,
            "node_id": node.id
        }
    
    async def _execute_storage_node(self, node: WorkflowNode, context: Dict) -> Dict:
        """Execute a storage node."""
        storage_type = node.parameters.get("storage_type")
        
        # Save results to appropriate storage
        if storage_type == "campaign_manager":
            # This would integrate with your CampaignManager
            campaign_id = f"campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            context["results"]["campaign_id"] = campaign_id
        
        return {
            "storage_type": storage_type,
            "status": "saved",
            "campaign_id": context["results"].get("campaign_id")
        }
    
    def get_workflow_status(self, workflow_id: str) -> Dict:
        """Get current status of a workflow."""
        if workflow_id not in self.workflows:
            return {"error": "Workflow not found"}
        
        workflow = self.workflows[workflow_id]
        
        # Get node statuses
        node_statuses = {}
        for node_id, node in workflow["nodes"].items():
            node_statuses[node_id] = {
                "name": node.name,
                "type": node.type,
                "status": node.status,
                "execution_time": node.execution_time
            }
        
        return {
            "workflow_id": workflow_id,
            "name": workflow["name"],
            "status": workflow["status"],
            "execution_count": workflow["execution_count"],
            "nodes": node_statuses
        }
    
    def get_workflow_visualization(self, workflow_id: str) -> Dict:
        """Get workflow data for visualization."""
        if workflow_id not in self.workflows:
            return {"error": "Workflow not found"}
        
        workflow = self.workflows[workflow_id]
        
        # Format for visualization
        viz_data = {
            "nodes": [],
            "edges": []
        }
        
        # Add nodes
        for node in workflow["nodes"].values():
            viz_data["nodes"].append({
                "id": node.id,
                "label": node.name,
                "type": node.type,
                "position": node.position,
                "status": node.status,
                "execution_time": node.execution_time
            })
        
        # Add edges
        for node in workflow["nodes"].values():
            for connection_id in node.connections:
                viz_data["edges"].append({
                    "from": node.id,
                    "to": connection_id,
                    "type": "flow"
                })
        
        return viz_data
    
    def get_execution_history(self, limit: int = 10) -> List[Dict]:
        """Get recent workflow execution history."""
        return self.execution_history[-limit:] if self.execution_history else []
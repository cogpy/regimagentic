"""
OpenCog Cognitive Reasoning Tool for Agent Zero
Provides cognitive reasoning capabilities using OpenCog Hyperon
"""

from python.helpers.tool import Tool, Response
from python.helpers.opencog_orchestrator import get_orchestrator
import json


class CognitiveReasoning(Tool):
    """
    Cognitive reasoning tool using OpenCog Hyperon
    
    Enables agents to perform advanced cognitive reasoning including:
    - Pattern matching
    - Knowledge inference
    - Multi-step reasoning
    - Cognitive coordination with other agents
    """
    
    async def execute(self, 
                     query: str = "", 
                     reasoning_type: str = "inference",
                     depth: int = 3,
                     share_with_agents: str = "",
                     **kwargs):
        """
        Execute cognitive reasoning
        
        Args:
            query: The reasoning query or problem statement
            reasoning_type: Type of reasoning (inference, pattern_match, coordination)
            depth: Reasoning depth (1-10)
            share_with_agents: Comma-separated agent IDs to share results with
        """
        
        orchestrator = get_orchestrator()
        
        if not query:
            return Response(
                message="Please provide a query for cognitive reasoning.",
                break_loop=False
            )
        
        # Get agent's cognitive profile
        agent_id = f"agent_{self.agent.number}"
        profile = orchestrator.get_agent_profile(agent_id)
        
        if not profile:
            # Register this agent if not already registered
            profile = orchestrator.register_agent(
                agent_id,
                reasoning_depth=depth
            )
        
        try:
            result_message = f"Cognitive Reasoning ({reasoning_type}):\n"
            result_message += f"Query: {query}\n\n"
            
            if reasoning_type == "inference":
                # Perform knowledge inference
                knowledge = orchestrator.query_knowledge(query, agent_id)
                
                result_message += f"Knowledge Retrieved: {len(knowledge)} atoms\n"
                
                if knowledge:
                    result_message += "Relevant Knowledge:\n"
                    for idx, atom in enumerate(knowledge[:5], 1):
                        result_message += f"{idx}. {atom}\n"
                else:
                    result_message += "No relevant knowledge found in cognitive store.\n"
                    result_message += "Consider learning this information first.\n"
                    
            elif reasoning_type == "pattern_match":
                # Pattern matching reasoning
                result_message += "Pattern Matching Results:\n"
                knowledge = orchestrator.query_knowledge(query)
                
                if knowledge:
                    patterns = self._extract_patterns(knowledge, query)
                    result_message += f"Found {len(patterns)} matching patterns:\n"
                    for pattern in patterns[:3]:
                        result_message += f"- {pattern}\n"
                else:
                    result_message += "No patterns found.\n"
                    
            elif reasoning_type == "coordination":
                # Multi-agent coordination
                if share_with_agents:
                    agent_ids = [aid.strip() for aid in share_with_agents.split(",")]
                    coordination = orchestrator.coordinate_agents(
                        agent_ids,
                        query
                    )
                    result_message += "Coordination Result:\n"
                    result_message += json.dumps(coordination, indent=2)
                else:
                    result_message += "No agents specified for coordination.\n"
                    
            else:
                result_message += f"Unknown reasoning type: {reasoning_type}\n"
                result_message += "Available types: inference, pattern_match, coordination\n"
            
            # Store this reasoning as knowledge
            orchestrator.add_knowledge_atom(agent_id, {
                "type": "reasoning",
                "query": query,
                "reasoning_type": reasoning_type,
                "timestamp": str(self.agent.context.created_at)
            })
            
            # Share knowledge if requested
            if share_with_agents and reasoning_type != "coordination":
                target_ids = [aid.strip() for aid in share_with_agents.split(",")]
                for target_id in target_ids:
                    orchestrator.share_knowledge(agent_id, target_id, query)
                result_message += f"\nKnowledge shared with: {', '.join(target_ids)}\n"
            
            return Response(
                message=result_message,
                break_loop=False
            )
            
        except Exception as e:
            return Response(
                message=f"Cognitive reasoning error: {str(e)}",
                break_loop=False
            )
    
    def _extract_patterns(self, knowledge: list, query: str) -> list:
        """Extract patterns from knowledge atoms"""
        patterns = []
        
        # Simple pattern extraction based on common elements
        query_words = set(query.lower().split())
        
        for atom in knowledge:
            atom_str = str(atom).lower()
            atom_words = set(atom_str.split())
            
            # Find common words
            common = query_words.intersection(atom_words)
            if len(common) >= 2:
                patterns.append(f"Pattern: {' '.join(common)}")
                
        return patterns
    
    def get_log_object(self):
        """Get log object for this tool execution"""
        return self.agent.context.log.log(
            type="tool",
            heading=f"icon://brain {self.agent.agent_name}: Cognitive Reasoning",
            content="",
            kvps=self.args,
        )

"""
OpenCog Knowledge Learning Tool for Agent Zero
Stores knowledge in cognitive architecture for future reasoning
"""

from python.helpers.tool import Tool, Response
from python.helpers.opencog_orchestrator import get_orchestrator, CognitiveState


class CognitiveKnowledge(Tool):
    """
    Cognitive knowledge learning and storage tool
    
    Allows agents to:
    - Learn and store knowledge in OpenCog AtomSpace
    - Retrieve stored knowledge
    - Build cognitive understanding over time
    """
    
    async def execute(self, 
                     action: str = "learn",
                     content: str = "",
                     category: str = "general",
                     **kwargs):
        """
        Execute knowledge learning or retrieval
        
        Args:
            action: Action to perform (learn, retrieve, list)
            content: Content to learn or query to retrieve
            category: Knowledge category for organization
        """
        
        orchestrator = get_orchestrator()
        
        # Ensure orchestrator is initialized
        if not orchestrator._initialized:
            init_success = orchestrator.initialize()
            if not init_success:
                return Response(
                    message="Cognitive knowledge system not available. OpenCog Hyperon may not be installed.",
                    break_loop=False
                )
        
        agent_id = f"agent_{self.agent.number}"
        profile = orchestrator.get_agent_profile(agent_id)
        
        if not profile:
            profile = orchestrator.register_agent(agent_id)
        
        try:
            if action == "learn":
                if not content:
                    return Response(
                        message="Please provide content to learn.",
                        break_loop=False
                    )
                
                # Store knowledge
                profile.cognitive_state = CognitiveState.LEARNING
                
                knowledge_atom = {
                    "content": content,
                    "category": category,
                    "agent_id": agent_id,
                    "timestamp": str(self.agent.context.created_at)
                }
                
                orchestrator.add_knowledge_atom(agent_id, knowledge_atom)
                
                profile.cognitive_state = CognitiveState.IDLE
                
                message = f"✓ Knowledge learned and stored in cognitive architecture:\n"
                message += f"Category: {category}\n"
                message += f"Content: {content[:200]}{'...' if len(content) > 200 else ''}\n"
                message += f"\nTotal knowledge atoms: {len(profile.knowledge_atoms)}"
                
                return Response(message=message, break_loop=False)
                
            elif action == "retrieve":
                if not content:
                    return Response(
                        message="Please provide a query to retrieve knowledge.",
                        break_loop=False
                    )
                
                # Query knowledge
                results = orchestrator.query_knowledge(content, agent_id)
                
                message = f"Knowledge Retrieval Results:\n"
                message += f"Query: {content}\n"
                message += f"Found: {len(results)} matching atoms\n\n"
                
                if results:
                    for idx, result in enumerate(results[:10], 1):
                        result_content = result.get("content", str(result))
                        result_category = result.get("category", "unknown")
                        message += f"{idx}. [{result_category}] {result_content[:150]}...\n"
                    
                    if len(results) > 10:
                        message += f"\n... and {len(results) - 10} more results"
                else:
                    message += "No matching knowledge found in cognitive store."
                
                return Response(message=message, break_loop=False)
                
            elif action == "list":
                # List all knowledge atoms for this agent
                knowledge_by_category = {}
                
                for atom in profile.knowledge_atoms:
                    cat = atom.get("category", "uncategorized")
                    if cat not in knowledge_by_category:
                        knowledge_by_category[cat] = []
                    knowledge_by_category[cat].append(atom)
                
                message = f"Cognitive Knowledge Inventory for {agent_id}:\n\n"
                
                for category, atoms in knowledge_by_category.items():
                    message += f"Category: {category} ({len(atoms)} atoms)\n"
                    for idx, atom in enumerate(atoms[:3], 1):
                        content_preview = str(atom.get("content", ""))[:80]
                        message += f"  {idx}. {content_preview}...\n"
                    if len(atoms) > 3:
                        message += f"  ... and {len(atoms) - 3} more\n"
                    message += "\n"
                
                message += f"Total: {len(profile.knowledge_atoms)} knowledge atoms"
                
                return Response(message=message, break_loop=False)
                
            else:
                return Response(
                    message=f"Unknown action: {action}\nAvailable actions: learn, retrieve, list",
                    break_loop=False
                )
                
        except Exception as e:
            return Response(
                message=f"Cognitive knowledge error: {str(e)}",
                break_loop=False
            )
    
    def get_log_object(self):
        """Get log object for this tool execution"""
        return self.agent.context.log.log(
            type="tool",
            heading=f"icon://book {self.agent.agent_name}: Cognitive Knowledge",
            content="",
            kvps=self.args,
        )

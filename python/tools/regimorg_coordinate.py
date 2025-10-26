"""
RegimOrg Product Range Coordination Tool
Coordinates products within a product range and manages distributed cognition
"""

from python.helpers.tool import Tool, Response
from python.helpers.regimorg_orchestrator import get_regimorg_orchestrator
import json


class RegimorgCoordinate(Tool):
    """
    Product range coordination tool for RegimOrg AGI
    
    Enables distributed cognition across product microkernels:
    - Coordinate products in a range for complex tasks
    - Share knowledge across the product range
    - Monitor product range performance
    """
    
    async def execute(
        self,
        action: str = "coordinate",
        range_id: str = "",
        task: str = "",
        knowledge_content: str = "",
        knowledge_category: str = "general",
        target_products: str = "",
        **kwargs
    ):
        """
        Execute product range coordination actions
        
        Args:
            action: Action to perform (coordinate, share_knowledge, get_status)
            range_id: Product range identifier
            task: Task description for coordination
            knowledge_content: Knowledge content to share
            knowledge_category: Category for knowledge sharing
            target_products: Comma-separated product IDs (empty = all products in range)
        """
        
        orchestrator = get_regimorg_orchestrator()
        
        if not orchestrator._initialized:
            return Response(
                message="RegimOrg orchestrator not initialized. Initialize it first.",
                break_loop=False
            )
        
        try:
            if action == "coordinate":
                if not range_id or not task:
                    return Response(
                        message="Please provide both range_id and task for coordination.",
                        break_loop=False
                    )
                
                # Coordinate products in the range
                result = orchestrator.coordinate_product_range(
                    range_id=range_id,
                    task=task
                )
                
                if "error" in result:
                    return Response(
                        message=f"Coordination error: {result['error']}",
                        break_loop=False
                    )
                
                message = f"✓ Product Range Coordination Initiated\n\n"
                message += f"Range: {result.get('range_name', range_id)} (ID: {result.get('range_id', range_id)})\n"
                message += f"Hub Agent: {result.get('hub_agent_id', 'N/A')}\n"
                message += f"Task: {result['task']}\n"
                message += f"Strategy: {result['strategy']}\n"
                message += f"Status: {result.get('status', 'pending')}\n\n"
                
                if result.get('agents'):
                    message += f"Coordinated Products ({len(result['agents'])}):\n"
                    for agent_info in result['agents']:
                        message += f"  • Agent: {agent_info['agent_id']}\n"
                        message += f"    State: {agent_info['state']}\n"
                        message += f"    Assigned: {agent_info['assigned']}\n"
                    message += "\n"
                
                message += "Products in the range are now working on the task collaboratively."
                
                return Response(message=message, break_loop=False)
                
            elif action == "share_knowledge":
                if not range_id or not knowledge_content:
                    return Response(
                        message="Please provide range_id and knowledge_content to share knowledge.",
                        break_loop=False
                    )
                
                # Parse target products if specified
                target_list = None
                if target_products:
                    target_list = [p.strip() for p in target_products.split(",")]
                
                # Create knowledge data
                knowledge_data = {
                    "type": "shared_knowledge",
                    "content": knowledge_content,
                    "category": knowledge_category,
                    "source": f"agent_{self.agent.number}",
                }
                
                # Share knowledge in the range
                orchestrator.share_knowledge_in_range(
                    range_id=range_id,
                    knowledge_data=knowledge_data,
                    target_products=target_list
                )
                
                product_range = orchestrator.get_product_range(range_id)
                
                if not product_range:
                    return Response(
                        message=f"Product range {range_id} not found.",
                        break_loop=False
                    )
                
                message = f"✓ Knowledge Shared via Distributed Cognition\n\n"
                message += f"Range: {product_range.range_name} (ID: {range_id})\n"
                message += f"Category: {knowledge_category}\n"
                message += f"Content: {knowledge_content[:200]}{'...' if len(knowledge_content) > 200 else ''}\n\n"
                
                if target_list:
                    message += f"Shared with specific products: {', '.join(target_list)}\n"
                else:
                    message += f"Shared with all {len(product_range.products)} products in range\n"
                
                message += f"\nTotal shared knowledge in range: {len(product_range.shared_knowledge)} atoms"
                
                return Response(message=message, break_loop=False)
                
            elif action == "get_status":
                if not range_id:
                    return Response(
                        message="Please provide range_id to get status.",
                        break_loop=False
                    )
                
                product_range = orchestrator.get_product_range(range_id)
                
                if not product_range:
                    return Response(
                        message=f"Product range {range_id} not found.",
                        break_loop=False
                    )
                
                message = f"📊 Product Range Status Report\n\n"
                message += f"Range: {product_range.range_name} (ID: {product_range.range_id})\n"
                message += f"Type: {product_range.range_type.value}\n"
                message += f"Hub Agent: {product_range.hub_agent_id}\n"
                message += f"Coordination Strategy: {product_range.coordination_strategy}\n\n"
                
                message += f"Products in Range: {len(product_range.products)}\n"
                
                if product_range.products:
                    message += "\nProduct Status:\n"
                    for p in product_range.products:
                        message += f"  • {p.product_name} ({p.product_id})\n"
                        message += f"    Agent: {p.cognitive_agent_id}\n"
                        message += f"    State: {p.state.value}\n"
                        message += f"    Capabilities: {len(p.capabilities)}\n"
                        message += f"    Knowledge Domains: {len(p.knowledge_domains)}\n"
                
                message += f"\nShared Knowledge: {len(product_range.shared_knowledge)} atoms\n"
                
                # Get cognitive profiles from base orchestrator
                base_state = orchestrator._base_orchestrator.get_orchestration_state()
                hub_agent_data = next(
                    (a for a in base_state.get('agents', []) if a['agent_id'] == product_range.hub_agent_id),
                    None
                )
                
                if hub_agent_data:
                    message += f"\nHub Cognitive Profile:\n"
                    message += f"  Reasoning Depth: {hub_agent_data.get('reasoning_depth', 'N/A')}\n"
                    message += f"  Knowledge Atoms: {hub_agent_data.get('knowledge_atoms', 0)}\n"
                    message += f"  State: {hub_agent_data.get('state', 'unknown')}\n"
                
                return Response(message=message, break_loop=False)
                
            else:
                available_actions = [
                    "coordinate",
                    "share_knowledge",
                    "get_status"
                ]
                return Response(
                    message=f"Unknown action: {action}\nAvailable actions: {', '.join(available_actions)}",
                    break_loop=False
                )
                
        except Exception as e:
            return Response(
                message=f"RegimOrg coordination error: {str(e)}",
                break_loop=False
            )
    
    def get_log_object(self):
        """Get log object for this tool execution"""
        return self.agent.context.log.log(
            type="tool",
            heading=f"icon://network-wired {self.agent.agent_name}: RegimOrg Coordination",
            content="",
            kvps=self.args,
        )

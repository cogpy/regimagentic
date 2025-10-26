"""
RegimOrg Organizational Management Tool
Allows agents to manage organizational hierarchy, product ranges, and products
"""

from python.helpers.tool import Tool, Response
from python.helpers.regimorg_orchestrator import (
    get_regimorg_orchestrator,
    ProductRangeType
)
import json


class RegimorgManage(Tool):
    """
    Organizational management tool for RegimOrg AGI
    
    Enables agents to:
    - Create and manage product-range cognition hubs
    - Deploy product microkernels
    - View organizational hierarchy
    - Manage organizational knowledge
    """
    
    async def execute(
        self,
        action: str = "view_hierarchy",
        range_id: str = "",
        range_name: str = "",
        range_type: str = "custom",
        product_id: str = "",
        product_name: str = "",
        capabilities: str = "",
        knowledge_domains: str = "",
        **kwargs
    ):
        """
        Execute organizational management actions
        
        Args:
            action: Action to perform (create_range, create_product, view_hierarchy, list_ranges, list_products)
            range_id: Product range identifier
            range_name: Product range name
            range_type: Type of product range (cognitive_services, automation_tools, data_analytics, integration_platforms, custom)
            product_id: Product identifier
            product_name: Product name
            capabilities: Comma-separated list of product capabilities
            knowledge_domains: Comma-separated list of knowledge domains
        """
        
        orchestrator = get_regimorg_orchestrator()
        
        # Ensure orchestrator is initialized
        if not orchestrator._initialized:
            orchestrator.initialize()
        
        try:
            if action == "create_range":
                if not range_id or not range_name:
                    return Response(
                        message="Please provide both range_id and range_name to create a product range.",
                        break_loop=False
                    )
                
                # Parse range type
                try:
                    rt = ProductRangeType[range_type.upper()]
                except KeyError:
                    rt = ProductRangeType.CUSTOM
                
                # Create product range
                hub = orchestrator.create_product_range(
                    range_id=range_id,
                    range_name=range_name,
                    range_type=rt,
                    **kwargs
                )
                
                message = f"✓ Product Range Cognition Hub Created:\n\n"
                message += f"Range ID: {hub.range_id}\n"
                message += f"Range Name: {hub.range_name}\n"
                message += f"Range Type: {hub.range_type.value}\n"
                message += f"Hub Agent ID: {hub.hub_agent_id}\n"
                message += f"Coordination Strategy: {hub.coordination_strategy}\n\n"
                message += "The product range is now ready to host product microkernels."
                
                return Response(message=message, break_loop=False)
                
            elif action == "create_product":
                if not product_id or not product_name or not range_id:
                    return Response(
                        message="Please provide product_id, product_name, and range_id to create a product microkernel.",
                        break_loop=False
                    )
                
                # Parse capabilities and domains
                caps = [c.strip() for c in capabilities.split(",")] if capabilities else []
                domains = [d.strip() for d in knowledge_domains.split(",")] if knowledge_domains else []
                
                # Create product microkernel
                product = orchestrator.create_product_microkernel(
                    product_id=product_id,
                    product_name=product_name,
                    product_range_id=range_id,
                    capabilities=caps,
                    knowledge_domains=domains,
                    **kwargs
                )
                
                message = f"✓ Product Agentic Microkernel Created:\n\n"
                message += f"Product ID: {product.product_id}\n"
                message += f"Product Name: {product.product_name}\n"
                message += f"Product Range: {product.product_range_id}\n"
                message += f"Cognitive Agent ID: {product.cognitive_agent_id}\n"
                message += f"Capabilities: {', '.join(product.capabilities) if product.capabilities else 'None'}\n"
                message += f"Knowledge Domains: {', '.join(product.knowledge_domains) if product.knowledge_domains else 'None'}\n"
                message += f"State: {product.state.value}\n\n"
                message += "The product microkernel is now autonomous and ready for tasks."
                
                return Response(message=message, break_loop=False)
                
            elif action == "view_hierarchy":
                hierarchy = orchestrator.get_organizational_hierarchy()
                
                message = "🏢 RegimOrg Organizational Hierarchy\n"
                message += "=" * 50 + "\n\n"
                message += f"Organization: {hierarchy['organization']}\n"
                message += f"Initialized: {hierarchy['initialized']}\n"
                message += f"Total Product Ranges: {hierarchy['total_product_ranges']}\n"
                message += f"Total Products: {hierarchy['total_products']}\n\n"
                
                if hierarchy['product_ranges']:
                    message += "📦 Product Ranges:\n\n"
                    for pr in hierarchy['product_ranges']:
                        message += f"  🔹 {pr['range_name']} (ID: {pr['range_id']})\n"
                        message += f"     Type: {pr['range_type']}\n"
                        message += f"     Hub Agent: {pr['hub_agent_id']}\n"
                        message += f"     Products: {pr['products_count']}\n"
                        message += f"     Shared Knowledge: {pr['shared_knowledge_count']} atoms\n"
                        
                        if pr['products']:
                            message += f"     \n     Products in Range:\n"
                            for p in pr['products']:
                                message += f"       • {p['product_name']} ({p['product_id']})\n"
                                message += f"         Agent: {p['cognitive_agent_id']}\n"
                                message += f"         State: {p['state']}\n"
                                if p['capabilities']:
                                    message += f"         Capabilities: {', '.join(p['capabilities'])}\n"
                        message += "\n"
                else:
                    message += "No product ranges created yet.\n"
                
                return Response(message=message, break_loop=False)
                
            elif action == "list_ranges":
                ranges = orchestrator.list_product_ranges()
                
                message = f"Product Ranges ({len(ranges)}):\n\n"
                
                for idx, pr in enumerate(ranges, 1):
                    message += f"{idx}. {pr.range_name}\n"
                    message += f"   ID: {pr.range_id}\n"
                    message += f"   Type: {pr.range_type.value}\n"
                    message += f"   Products: {len(pr.products)}\n"
                    message += f"   Hub Agent: {pr.hub_agent_id}\n\n"
                
                if not ranges:
                    message = "No product ranges found. Create one with action='create_range'."
                
                return Response(message=message, break_loop=False)
                
            elif action == "list_products":
                products = orchestrator.list_products(range_id if range_id else None)
                
                filter_msg = f" in range '{range_id}'" if range_id else ""
                message = f"Products{filter_msg} ({len(products)}):\n\n"
                
                for idx, p in enumerate(products, 1):
                    message += f"{idx}. {p.product_name}\n"
                    message += f"   ID: {p.product_id}\n"
                    message += f"   Range: {p.product_range_id}\n"
                    message += f"   Agent: {p.cognitive_agent_id}\n"
                    message += f"   State: {p.state.value}\n"
                    if p.capabilities:
                        message += f"   Capabilities: {', '.join(p.capabilities)}\n"
                    message += "\n"
                
                if not products:
                    message = f"No products found{filter_msg}. Create one with action='create_product'."
                
                return Response(message=message, break_loop=False)
                
            else:
                available_actions = [
                    "create_range",
                    "create_product",
                    "view_hierarchy",
                    "list_ranges",
                    "list_products"
                ]
                return Response(
                    message=f"Unknown action: {action}\nAvailable actions: {', '.join(available_actions)}",
                    break_loop=False
                )
                
        except Exception as e:
            return Response(
                message=f"RegimOrg management error: {str(e)}",
                break_loop=False
            )
    
    def get_log_object(self):
        """Get log object for this tool execution"""
        return self.agent.context.log.log(
            type="tool",
            heading=f"icon://building {self.agent.agent_name}: RegimOrg Management",
            content="",
            kvps=self.args,
        )

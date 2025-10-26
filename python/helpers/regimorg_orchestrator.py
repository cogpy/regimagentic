"""
RegimOrg Organizational AGI Orchestrator
Extends OpenCog integration to provide organizational multi-agent coordination
for regimazone.org with product-range cognition hubs and product microkernels
"""

import asyncio
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
from python.helpers.opencog_orchestrator import (
    OpenCogOrchestrator,
    AgentCognitiveProfile,
    CognitiveState,
    get_orchestrator as get_base_orchestrator
)


class OrganizationalLevel(Enum):
    """Organizational hierarchy levels"""
    ORGANIZATION = "organization"  # Top-level organizational AGI
    PRODUCT_RANGE = "product_range"  # Product-range cognition hubs
    PRODUCT = "product"  # Individual product microkernels
    FEATURE = "feature"  # Product features/components


class ProductRangeType(Enum):
    """Types of product ranges in regimazone.org"""
    COGNITIVE_SERVICES = "cognitive_services"
    AUTOMATION_TOOLS = "automation_tools"
    DATA_ANALYTICS = "data_analytics"
    INTEGRATION_PLATFORMS = "integration_platforms"
    CUSTOM = "custom"


@dataclass
class ProductMicrokernel:
    """
    Agentic core microkernel for individual products
    Each product has autonomous decision-making capabilities
    """
    product_id: str
    product_name: str
    product_range_id: str
    cognitive_agent_id: str
    capabilities: List[str] = field(default_factory=list)
    state: CognitiveState = CognitiveState.IDLE
    knowledge_domains: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    

@dataclass
class ProductRangeHub:
    """
    Distributed cognition hub for product ranges
    Coordinates multiple product microkernels and shared knowledge
    """
    range_id: str
    range_name: str
    range_type: ProductRangeType
    hub_agent_id: str
    products: List[ProductMicrokernel] = field(default_factory=list)
    shared_knowledge: List[Any] = field(default_factory=list)
    coordination_strategy: str = "distributed"
    metadata: Dict[str, Any] = field(default_factory=dict)


class RegimOrgOrchestrator:
    """
    RegimOrg Organizational AGI Orchestrator
    
    Multi-layered autonomous agent system:
    - Organization level: Overall AGI coordination
    - Product-range level: Distributed cognition hubs
    - Product level: Agentic core microkernels
    
    Extends OpenCog cognitive architecture with organizational hierarchy
    """
    
    def __init__(self):
        self._base_orchestrator: OpenCogOrchestrator = get_base_orchestrator()
        self._product_ranges: Dict[str, ProductRangeHub] = {}
        self._products: Dict[str, ProductMicrokernel] = {}
        self._org_knowledge: List[Any] = []
        self._initialized = False
        
    def initialize(self) -> bool:
        """
        Initialize the RegimOrg orchestrator
        Returns True if successful
        """
        if self._initialized:
            return True
            
        # Initialize base OpenCog orchestrator
        base_init = self._base_orchestrator.initialize()
        
        # Create organizational root agent
        self._base_orchestrator.register_agent(
            "regimorg_root",
            reasoning_depth=10,
            learning_rate=0.05,
            evolution_enabled=True
        )
        
        self._initialized = True
        return True
        
    def create_product_range(
        self,
        range_id: str,
        range_name: str,
        range_type: ProductRangeType = ProductRangeType.CUSTOM,
        **metadata
    ) -> ProductRangeHub:
        """
        Create a product-range cognition hub
        
        Args:
            range_id: Unique identifier for the product range
            range_name: Human-readable name
            range_type: Type of product range
            **metadata: Additional metadata
            
        Returns:
            ProductRangeHub instance
        """
        if range_id in self._product_ranges:
            return self._product_ranges[range_id]
            
        # Create hub agent in base orchestrator
        hub_agent_id = f"hub_{range_id}"
        self._base_orchestrator.register_agent(
            hub_agent_id,
            reasoning_depth=7,
            learning_rate=0.1,
            evolution_enabled=True
        )
        
        # Add organizational knowledge
        self._base_orchestrator.add_knowledge_atom(hub_agent_id, {
            "type": "organizational_entity",
            "level": OrganizationalLevel.PRODUCT_RANGE.value,
            "range_id": range_id,
            "range_name": range_name,
            "range_type": range_type.value
        })
        
        hub = ProductRangeHub(
            range_id=range_id,
            range_name=range_name,
            range_type=range_type,
            hub_agent_id=hub_agent_id,
            metadata=metadata
        )
        
        self._product_ranges[range_id] = hub
        return hub
        
    def create_product_microkernel(
        self,
        product_id: str,
        product_name: str,
        product_range_id: str,
        capabilities: Optional[List[str]] = None,
        knowledge_domains: Optional[List[str]] = None,
        **metadata
    ) -> ProductMicrokernel:
        """
        Create a product agentic microkernel
        
        Args:
            product_id: Unique product identifier
            product_name: Human-readable product name
            product_range_id: Parent product range ID
            capabilities: List of product capabilities
            knowledge_domains: Knowledge domains for this product
            **metadata: Additional metadata
            
        Returns:
            ProductMicrokernel instance
        """
        if product_id in self._products:
            return self._products[product_id]
            
        # Verify product range exists
        if product_range_id not in self._product_ranges:
            raise ValueError(f"Product range {product_range_id} does not exist")
            
        # Create product agent in base orchestrator
        product_agent_id = f"product_{product_id}"
        self._base_orchestrator.register_agent(
            product_agent_id,
            reasoning_depth=5,
            learning_rate=0.15,
            evolution_enabled=True
        )
        
        # Add product knowledge
        self._base_orchestrator.add_knowledge_atom(product_agent_id, {
            "type": "organizational_entity",
            "level": OrganizationalLevel.PRODUCT.value,
            "product_id": product_id,
            "product_name": product_name,
            "product_range_id": product_range_id,
            "capabilities": capabilities or [],
            "knowledge_domains": knowledge_domains or []
        })
        
        microkernel = ProductMicrokernel(
            product_id=product_id,
            product_name=product_name,
            product_range_id=product_range_id,
            cognitive_agent_id=product_agent_id,
            capabilities=capabilities or [],
            knowledge_domains=knowledge_domains or [],
            metadata=metadata
        )
        
        # Add to product range
        product_range = self._product_ranges[product_range_id]
        product_range.products.append(microkernel)
        
        self._products[product_id] = microkernel
        return microkernel
        
    def coordinate_product_range(
        self,
        range_id: str,
        task: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Coordinate all products in a product range for a task
        
        Args:
            range_id: Product range ID
            task: Task description
            
        Returns:
            Coordination result
        """
        if range_id not in self._product_ranges:
            return {"error": f"Product range {range_id} not found"}
            
        product_range = self._product_ranges[range_id]
        
        # Get all product agent IDs
        product_agent_ids = [p.cognitive_agent_id for p in product_range.products]
        
        if not product_agent_ids:
            return {
                "range_id": range_id,
                "task": task,
                "status": "no_products",
                "message": "No products in this range to coordinate"
            }
        
        # Use base orchestrator for coordination
        coordination = self._base_orchestrator.coordinate_agents(
            product_agent_ids,
            task
        )
        
        # Add range context
        coordination["range_id"] = range_id
        coordination["range_name"] = product_range.range_name
        coordination["hub_agent_id"] = product_range.hub_agent_id
        
        return coordination
        
    def share_knowledge_in_range(
        self,
        range_id: str,
        knowledge_data: Dict[str, Any],
        target_products: Optional[List[str]] = None
    ):
        """
        Share knowledge across products in a range (distributed cognition)
        
        Args:
            range_id: Product range ID
            knowledge_data: Knowledge to share
            target_products: Specific product IDs, or None for all
        """
        if range_id not in self._product_ranges:
            return
            
        product_range = self._product_ranges[range_id]
        
        # Add to hub's shared knowledge
        product_range.shared_knowledge.append(knowledge_data)
        
        # Add to hub agent
        self._base_orchestrator.add_knowledge_atom(
            product_range.hub_agent_id,
            knowledge_data
        )
        
        # Distribute to products
        products_to_share = (
            [self._products[pid] for pid in target_products if pid in self._products]
            if target_products
            else product_range.products
        )
        
        for product in products_to_share:
            self._base_orchestrator.add_knowledge_atom(
                product.cognitive_agent_id,
                knowledge_data
            )
            
    def get_organizational_hierarchy(self) -> Dict[str, Any]:
        """
        Get the complete organizational hierarchy
        
        Returns:
            Dictionary representing the organizational structure
        """
        return {
            "organization": "regimorg",
            "initialized": self._initialized,
            "product_ranges": [
                {
                    "range_id": pr.range_id,
                    "range_name": pr.range_name,
                    "range_type": pr.range_type.value,
                    "hub_agent_id": pr.hub_agent_id,
                    "products_count": len(pr.products),
                    "products": [
                        {
                            "product_id": p.product_id,
                            "product_name": p.product_name,
                            "cognitive_agent_id": p.cognitive_agent_id,
                            "capabilities": p.capabilities,
                            "knowledge_domains": p.knowledge_domains,
                            "state": p.state.value
                        }
                        for p in pr.products
                    ],
                    "shared_knowledge_count": len(pr.shared_knowledge)
                }
                for pr in self._product_ranges.values()
            ],
            "total_product_ranges": len(self._product_ranges),
            "total_products": len(self._products),
            "base_orchestrator_state": self._base_orchestrator.get_orchestration_state()
        }
        
    async def evolve_product(
        self,
        product_id: str,
        performance_metrics: Dict[str, float]
    ):
        """
        Evolve a product microkernel based on performance
        
        Args:
            product_id: Product identifier
            performance_metrics: Performance metrics
        """
        if product_id not in self._products:
            return
            
        product = self._products[product_id]
        
        # Evolve the product's cognitive agent
        await self._base_orchestrator.evolve_agent(
            product.cognitive_agent_id,
            performance_metrics
        )
        
        # Share evolution insights with product range hub
        if product.product_range_id in self._product_ranges:
            hub = self._product_ranges[product.product_range_id]
            self._base_orchestrator.add_knowledge_atom(
                hub.hub_agent_id,
                {
                    "type": "evolution_event",
                    "product_id": product_id,
                    "metrics": performance_metrics,
                    "evolved": True
                }
            )
            
    def get_product_range(self, range_id: str) -> Optional[ProductRangeHub]:
        """Get a product range by ID"""
        return self._product_ranges.get(range_id)
        
    def get_product(self, product_id: str) -> Optional[ProductMicrokernel]:
        """Get a product by ID"""
        return self._products.get(product_id)
        
    def list_product_ranges(self) -> List[ProductRangeHub]:
        """List all product ranges"""
        return list(self._product_ranges.values())
        
    def list_products(self, range_id: Optional[str] = None) -> List[ProductMicrokernel]:
        """
        List products, optionally filtered by range
        
        Args:
            range_id: Optional product range ID to filter by
            
        Returns:
            List of ProductMicrokernel instances
        """
        if range_id:
            product_range = self._product_ranges.get(range_id)
            return product_range.products if product_range else []
        return list(self._products.values())
        
    def shutdown(self):
        """Shutdown the RegimOrg orchestrator"""
        self._product_ranges.clear()
        self._products.clear()
        self._org_knowledge.clear()
        self._initialized = False


# Global singleton instance
_global_regimorg: Optional[RegimOrgOrchestrator] = None


def get_regimorg_orchestrator() -> RegimOrgOrchestrator:
    """Get or create the global RegimOrg orchestrator instance"""
    global _global_regimorg
    if _global_regimorg is None:
        _global_regimorg = RegimOrgOrchestrator()
    return _global_regimorg


def initialize_regimorg() -> bool:
    """Initialize the global RegimOrg orchestrator"""
    orchestrator = get_regimorg_orchestrator()
    return orchestrator.initialize()

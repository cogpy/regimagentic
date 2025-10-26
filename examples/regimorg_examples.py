#!/usr/bin/env python3
"""
RegimOrg Organizational AGI Examples
Demonstrates multi-level organizational orchestration with product ranges and microkernels
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from python.helpers.regimorg_orchestrator import (
    get_regimorg_orchestrator,
    initialize_regimorg,
    ProductRangeType
)


def example_basic_setup():
    """Example 1: Basic organizational setup"""
    print("=" * 70)
    print("Example 1: Basic RegimOrg Setup")
    print("=" * 70)
    
    # Initialize RegimOrg
    initialize_regimorg()
    orchestrator = get_regimorg_orchestrator()
    
    print(f"✓ RegimOrg initialized: {orchestrator._initialized}")
    print(f"✓ Base orchestrator available: {orchestrator._base_orchestrator is not None}")
    print()


def example_create_product_ranges():
    """Example 2: Create product-range cognition hubs"""
    print("=" * 70)
    print("Example 2: Create Product-Range Cognition Hubs")
    print("=" * 70)
    
    orchestrator = get_regimorg_orchestrator()
    
    # Create AI Services range
    ai_range = orchestrator.create_product_range(
        range_id="ai_services",
        range_name="AI & Cognitive Services",
        range_type=ProductRangeType.COGNITIVE_SERVICES
    )
    
    # Create Automation Tools range
    automation_range = orchestrator.create_product_range(
        range_id="automation",
        range_name="Automation & Workflow Tools",
        range_type=ProductRangeType.AUTOMATION_TOOLS
    )
    
    # Create Data Analytics range
    analytics_range = orchestrator.create_product_range(
        range_id="analytics",
        range_name="Data Analytics Platform",
        range_type=ProductRangeType.DATA_ANALYTICS
    )
    
    print(f"✓ Created {len(orchestrator._product_ranges)} product ranges:")
    print(f"  - {ai_range.range_name} (Hub: {ai_range.hub_agent_id})")
    print(f"  - {automation_range.range_name} (Hub: {automation_range.hub_agent_id})")
    print(f"  - {analytics_range.range_name} (Hub: {analytics_range.hub_agent_id})")
    print()


def example_create_products():
    """Example 3: Deploy product agentic microkernels"""
    print("=" * 70)
    print("Example 3: Deploy Product Agentic Microkernels")
    print("=" * 70)
    
    orchestrator = get_regimorg_orchestrator()
    
    # AI Services products
    sentiment_ai = orchestrator.create_product_microkernel(
        product_id="sentiment_ai",
        product_name="Sentiment Analysis AI",
        product_range_id="ai_services",
        capabilities=["sentiment_analysis", "emotion_detection", "opinion_mining"],
        knowledge_domains=["nlp", "psychology", "statistics"]
    )
    
    visual_ai = orchestrator.create_product_microkernel(
        product_id="visual_ai",
        product_name="Visual Recognition AI",
        product_range_id="ai_services",
        capabilities=["image_classification", "object_detection", "ocr"],
        knowledge_domains=["computer_vision", "deep_learning"]
    )
    
    # Automation products
    workflow_engine = orchestrator.create_product_microkernel(
        product_id="workflow_engine",
        product_name="Intelligent Workflow Engine",
        product_range_id="automation",
        capabilities=["workflow_orchestration", "task_scheduling", "process_mining"],
        knowledge_domains=["bpm", "scheduling", "optimization"]
    )
    
    rpa_bot = orchestrator.create_product_microkernel(
        product_id="rpa_bot",
        product_name="RPA Automation Bot",
        product_range_id="automation",
        capabilities=["ui_automation", "data_extraction", "report_generation"],
        knowledge_domains=["rpa", "automation", "scripting"]
    )
    
    # Analytics products
    data_viz = orchestrator.create_product_microkernel(
        product_id="data_viz",
        product_name="Interactive Data Visualization",
        product_range_id="analytics",
        capabilities=["chart_generation", "dashboard_creation", "data_exploration"],
        knowledge_domains=["visualization", "statistics", "ui_design"]
    )
    
    print(f"✓ Deployed {len(orchestrator._products)} product microkernels:")
    print(f"\n  AI Services Range:")
    print(f"    • {sentiment_ai.product_name} (Agent: {sentiment_ai.cognitive_agent_id})")
    print(f"      Capabilities: {', '.join(sentiment_ai.capabilities)}")
    print(f"    • {visual_ai.product_name} (Agent: {visual_ai.cognitive_agent_id})")
    print(f"      Capabilities: {', '.join(visual_ai.capabilities)}")
    
    print(f"\n  Automation Range:")
    print(f"    • {workflow_engine.product_name} (Agent: {workflow_engine.cognitive_agent_id})")
    print(f"      Capabilities: {', '.join(workflow_engine.capabilities)}")
    print(f"    • {rpa_bot.product_name} (Agent: {rpa_bot.cognitive_agent_id})")
    print(f"      Capabilities: {', '.join(rpa_bot.capabilities)}")
    
    print(f"\n  Analytics Range:")
    print(f"    • {data_viz.product_name} (Agent: {data_viz.cognitive_agent_id})")
    print(f"      Capabilities: {', '.join(data_viz.capabilities)}")
    
    print()


def example_distributed_cognition():
    """Example 4: Distributed cognition - share knowledge across products"""
    print("=" * 70)
    print("Example 4: Distributed Cognition - Knowledge Sharing")
    print("=" * 70)
    
    orchestrator = get_regimorg_orchestrator()
    
    # Share AI best practices across AI services
    orchestrator.share_knowledge_in_range(
        range_id="ai_services",
        knowledge_data={
            "type": "best_practice",
            "content": "All AI services must implement bias detection and fairness checks",
            "category": "ai_ethics",
            "priority": "high"
        }
    )
    
    # Share automation patterns
    orchestrator.share_knowledge_in_range(
        range_id="automation",
        knowledge_data={
            "type": "pattern",
            "content": "Implement retry logic with exponential backoff for all external API calls",
            "category": "reliability",
            "priority": "medium"
        }
    )
    
    # Share data security requirements
    orchestrator.share_knowledge_in_range(
        range_id="analytics",
        knowledge_data={
            "type": "requirement",
            "content": "All data visualizations must support role-based access control",
            "category": "security",
            "priority": "high"
        }
    )
    
    print("✓ Knowledge distributed via cognition hubs:")
    
    for range_id in ["ai_services", "automation", "analytics"]:
        product_range = orchestrator.get_product_range(range_id)
        print(f"\n  {product_range.range_name}:")
        print(f"    • Shared knowledge atoms: {len(product_range.shared_knowledge)}")
        print(f"    • Products receiving knowledge: {len(product_range.products)}")
        if product_range.shared_knowledge:
            latest = product_range.shared_knowledge[-1]
            print(f"    • Latest: [{latest.get('category')}] {latest.get('content')[:60]}...")
    
    print()


def example_coordination():
    """Example 5: Coordinate products for complex tasks"""
    print("=" * 70)
    print("Example 5: Product Range Coordination")
    print("=" * 70)
    
    orchestrator = get_regimorg_orchestrator()
    
    # Coordinate AI services
    ai_coordination = orchestrator.coordinate_product_range(
        range_id="ai_services",
        task="Analyze user-generated content for sentiment and visual insights"
    )
    
    print(f"✓ AI Services Coordination:")
    print(f"  Task: {ai_coordination['task']}")
    print(f"  Strategy: {ai_coordination['strategy']}")
    print(f"  Agents coordinated: {len(ai_coordination['agents'])}")
    
    # Coordinate automation tools
    automation_coordination = orchestrator.coordinate_product_range(
        range_id="automation",
        task="Automate customer onboarding workflow"
    )
    
    print(f"\n✓ Automation Tools Coordination:")
    print(f"  Task: {automation_coordination['task']}")
    print(f"  Strategy: {automation_coordination['strategy']}")
    print(f"  Agents coordinated: {len(automation_coordination['agents'])}")
    
    print()


def example_hierarchy_view():
    """Example 6: View organizational hierarchy"""
    print("=" * 70)
    print("Example 6: Organizational Hierarchy")
    print("=" * 70)
    
    orchestrator = get_regimorg_orchestrator()
    
    hierarchy = orchestrator.get_organizational_hierarchy()
    
    print(f"🏢 Organization: {hierarchy['organization'].upper()}")
    print(f"   Initialized: {hierarchy['initialized']}")
    print(f"   Product Ranges: {hierarchy['total_product_ranges']}")
    print(f"   Total Products: {hierarchy['total_products']}")
    print()
    
    for pr in hierarchy['product_ranges']:
        print(f"📦 {pr['range_name']} ({pr['range_type']})")
        print(f"   Hub Agent: {pr['hub_agent_id']}")
        print(f"   Products: {pr['products_count']}")
        print(f"   Shared Knowledge: {pr['shared_knowledge_count']} atoms")
        
        if pr['products']:
            print(f"   \n   Product Microkernels:")
            for p in pr['products']:
                print(f"     • {p['product_name']}")
                print(f"       ID: {p['product_id']}")
                print(f"       Agent: {p['cognitive_agent_id']}")
                print(f"       State: {p['state']}")
                if p['capabilities']:
                    print(f"       Capabilities: {', '.join(p['capabilities'][:3])}...")
        print()
    
    print()


async def example_product_evolution():
    """Example 7: Product evolution based on performance"""
    print("=" * 70)
    print("Example 7: Product Evolution")
    print("=" * 70)
    
    orchestrator = get_regimorg_orchestrator()
    
    # Get initial state
    sentiment_ai = orchestrator.get_product("sentiment_ai")
    profile_before = orchestrator._base_orchestrator.get_agent_profile(
        sentiment_ai.cognitive_agent_id
    )
    
    print(f"Product: {sentiment_ai.product_name}")
    print(f"Initial State:")
    print(f"  Reasoning Depth: {profile_before.reasoning_depth}")
    print(f"  Learning Rate: {profile_before.learning_rate}")
    
    # Evolve based on high performance
    await orchestrator.evolve_product(
        product_id="sentiment_ai",
        performance_metrics={
            "accuracy": 0.95,
            "speed": 0.88,
            "user_satisfaction": 0.92
        }
    )
    
    profile_after = orchestrator._base_orchestrator.get_agent_profile(
        sentiment_ai.cognitive_agent_id
    )
    
    print(f"\nAfter Evolution (high performance):")
    print(f"  Reasoning Depth: {profile_after.reasoning_depth}")
    print(f"  Learning Rate: {profile_after.learning_rate}")
    
    # Check if knowledge was shared to hub
    ai_range = orchestrator.get_product_range("ai_services")
    hub_profile = orchestrator._base_orchestrator.get_agent_profile(ai_range.hub_agent_id)
    
    print(f"\nHub Knowledge Updated:")
    print(f"  Hub knowledge atoms: {len(hub_profile.knowledge_atoms)}")
    
    print()


async def main():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + "  RegimOrg Organizational AGI Examples".center(68) + "║")
    print("║" + "  Multi-Agent Orchestrator for regimazone.org".center(68) + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    try:
        example_basic_setup()
        example_create_product_ranges()
        example_create_products()
        example_distributed_cognition()
        example_coordination()
        example_hierarchy_view()
        await example_product_evolution()
        
        print("=" * 70)
        print("✓ All examples completed!")
        print("=" * 70)
        print("\nRegimOrg demonstrates:")
        print("  • Multi-level organizational hierarchy")
        print("  • Product-range cognition hubs")
        print("  • Agentic product microkernels")
        print("  • Distributed cognition and knowledge sharing")
        print("  • Autonomous coordination and evolution")
        print("\nSee docs/regimorg_agi.md for detailed guide")
        print()
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

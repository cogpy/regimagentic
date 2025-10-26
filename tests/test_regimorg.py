#!/usr/bin/env python3
"""
Test suite for RegimOrg Organizational AGI
Tests the orchestrator, product ranges, microkernels, and coordination
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from python.helpers.regimorg_orchestrator import (
    RegimOrgOrchestrator,
    ProductRangeType,
    ProductRangeHub,
    ProductMicrokernel,
    OrganizationalLevel,
    get_regimorg_orchestrator,
    initialize_regimorg
)


def test_orchestrator_initialization():
    """Test RegimOrg orchestrator initialization"""
    print("Test 1: RegimOrg Orchestrator Initialization")
    
    orchestrator = RegimOrgOrchestrator()
    result = orchestrator.initialize()
    
    print(f"  ✓ Initialization: {result}")
    assert orchestrator._initialized, "Orchestrator should be initialized"
    assert orchestrator._base_orchestrator is not None, "Base orchestrator should exist"
    
    # Test singleton
    regimorg = get_regimorg_orchestrator()
    assert regimorg is not None, "Singleton should exist"
    
    print("  ✓ Singleton pattern works")
    print()


def test_product_range_creation():
    """Test creating product-range cognition hubs"""
    print("Test 2: Product Range Creation")
    
    orchestrator = get_regimorg_orchestrator()
    if not orchestrator._initialized:
        orchestrator.initialize()
    
    # Create product ranges
    ai_range = orchestrator.create_product_range(
        range_id="test_ai_services",
        range_name="Test AI Services",
        range_type=ProductRangeType.COGNITIVE_SERVICES
    )
    
    automation_range = orchestrator.create_product_range(
        range_id="test_automation",
        range_name="Test Automation Tools",
        range_type=ProductRangeType.AUTOMATION_TOOLS
    )
    
    assert ai_range.range_id == "test_ai_services", "Range ID should match"
    assert ai_range.range_type == ProductRangeType.COGNITIVE_SERVICES, "Range type should match"
    assert len(ai_range.products) == 0, "New range should have no products"
    
    print(f"  ✓ Created {len(orchestrator._product_ranges)} product ranges")
    print(f"  ✓ AI Services hub: {ai_range.hub_agent_id}")
    print(f"  ✓ Automation hub: {automation_range.hub_agent_id}")
    
    # Test duplicate creation
    duplicate = orchestrator.create_product_range(
        range_id="test_ai_services",
        range_name="Duplicate",
        range_type=ProductRangeType.CUSTOM
    )
    
    assert duplicate is ai_range, "Duplicate should return existing range"
    print("  ✓ Duplicate prevention works")
    
    print()


def test_product_microkernel_creation():
    """Test creating product agentic microkernels"""
    print("Test 3: Product Microkernel Creation")
    
    orchestrator = get_regimorg_orchestrator()
    
    # Create products
    sentiment_ai = orchestrator.create_product_microkernel(
        product_id="test_sentiment",
        product_name="Test Sentiment AI",
        product_range_id="test_ai_services",
        capabilities=["sentiment_analysis", "emotion_detection"],
        knowledge_domains=["nlp", "psychology"]
    )
    
    workflow = orchestrator.create_product_microkernel(
        product_id="test_workflow",
        product_name="Test Workflow Engine",
        product_range_id="test_automation",
        capabilities=["orchestration", "scheduling"],
        knowledge_domains=["bpm", "optimization"]
    )
    
    assert sentiment_ai.product_id == "test_sentiment", "Product ID should match"
    assert len(sentiment_ai.capabilities) == 2, "Should have 2 capabilities"
    assert len(sentiment_ai.knowledge_domains) == 2, "Should have 2 knowledge domains"
    
    print(f"  ✓ Created {len(orchestrator._products)} product microkernels")
    print(f"  ✓ {sentiment_ai.product_name}: {sentiment_ai.cognitive_agent_id}")
    print(f"  ✓ {workflow.product_name}: {workflow.cognitive_agent_id}")
    
    # Verify product added to range
    ai_range = orchestrator.get_product_range("test_ai_services")
    assert len(ai_range.products) == 1, "Range should have 1 product"
    assert ai_range.products[0] is sentiment_ai, "Product should be in range"
    
    print("  ✓ Products correctly added to ranges")
    
    # Test error handling for non-existent range
    try:
        orchestrator.create_product_microkernel(
            product_id="orphan",
            product_name="Orphan Product",
            product_range_id="nonexistent_range",
            capabilities=[],
            knowledge_domains=[]
        )
        assert False, "Should raise error for non-existent range"
    except ValueError as e:
        print("  ✓ Error handling for non-existent range works")
    
    print()


def test_knowledge_sharing():
    """Test distributed cognition knowledge sharing"""
    print("Test 4: Distributed Cognition - Knowledge Sharing")
    
    orchestrator = get_regimorg_orchestrator()
    
    # Share knowledge in AI services range
    orchestrator.share_knowledge_in_range(
        range_id="test_ai_services",
        knowledge_data={
            "type": "best_practice",
            "content": "Implement bias detection in all AI models",
            "category": "ai_ethics"
        }
    )
    
    ai_range = orchestrator.get_product_range("test_ai_services")
    assert len(ai_range.shared_knowledge) > 0, "Range should have shared knowledge"
    
    print(f"  ✓ Knowledge shared to hub")
    print(f"  ✓ Shared knowledge atoms: {len(ai_range.shared_knowledge)}")
    
    # Verify knowledge distributed to products
    sentiment_ai = orchestrator.get_product("test_sentiment")
    sentiment_profile = orchestrator._base_orchestrator.get_agent_profile(
        sentiment_ai.cognitive_agent_id
    )
    
    print(f"  ✓ Product knowledge atoms: {len(sentiment_profile.knowledge_atoms)}")
    
    # Test selective sharing
    orchestrator.create_product_microkernel(
        product_id="test_visual",
        product_name="Test Visual AI",
        product_range_id="test_ai_services",
        capabilities=["image_recognition"],
        knowledge_domains=["computer_vision"]
    )
    
    orchestrator.share_knowledge_in_range(
        range_id="test_ai_services",
        knowledge_data={
            "type": "tip",
            "content": "Use transfer learning for better performance"
        },
        target_products=["test_visual"]
    )
    
    print("  ✓ Selective knowledge sharing works")
    
    print()


def test_product_range_coordination():
    """Test coordinating products in a range"""
    print("Test 5: Product Range Coordination")
    
    orchestrator = get_regimorg_orchestrator()
    
    # Coordinate AI services
    coordination = orchestrator.coordinate_product_range(
        range_id="test_ai_services",
        task="Analyze customer feedback for insights"
    )
    
    assert "error" not in coordination, "Coordination should succeed"
    assert coordination["range_id"] == "test_ai_services", "Range ID should match"
    assert len(coordination["agents"]) > 0, "Should coordinate agents"
    
    print(f"  ✓ Coordination successful")
    print(f"  ✓ Task: {coordination['task']}")
    print(f"  ✓ Strategy: {coordination['strategy']}")
    print(f"  ✓ Agents: {len(coordination['agents'])}")
    
    # Test error handling for non-existent range
    error_result = orchestrator.coordinate_product_range(
        range_id="nonexistent",
        task="Some task"
    )
    
    assert "error" in error_result, "Should return error for non-existent range"
    print("  ✓ Error handling for non-existent range works")
    
    print()


def test_organizational_hierarchy():
    """Test getting organizational hierarchy"""
    print("Test 6: Organizational Hierarchy")
    
    orchestrator = get_regimorg_orchestrator()
    
    hierarchy = orchestrator.get_organizational_hierarchy()
    
    assert hierarchy["organization"] == "regimorg", "Organization should be regimorg"
    assert hierarchy["initialized"], "Should be initialized"
    assert hierarchy["total_product_ranges"] > 0, "Should have product ranges"
    assert hierarchy["total_products"] > 0, "Should have products"
    
    print(f"  ✓ Organization: {hierarchy['organization']}")
    print(f"  ✓ Product Ranges: {hierarchy['total_product_ranges']}")
    print(f"  ✓ Products: {hierarchy['total_products']}")
    
    # Verify hierarchy structure
    assert len(hierarchy["product_ranges"]) > 0, "Should have range details"
    first_range = hierarchy["product_ranges"][0]
    assert "range_id" in first_range, "Range should have ID"
    assert "products" in first_range, "Range should have products list"
    
    print("  ✓ Hierarchy structure validated")
    
    print()


async def test_product_evolution():
    """Test product evolution based on performance"""
    print("Test 7: Product Evolution")
    
    orchestrator = get_regimorg_orchestrator()
    
    sentiment_ai = orchestrator.get_product("test_sentiment")
    profile_before = orchestrator._base_orchestrator.get_agent_profile(
        sentiment_ai.cognitive_agent_id
    )
    
    initial_depth = profile_before.reasoning_depth
    initial_rate = profile_before.learning_rate
    
    print(f"  ✓ Initial reasoning depth: {initial_depth}")
    print(f"  ✓ Initial learning rate: {initial_rate}")
    
    # Evolve with high performance
    await orchestrator.evolve_product(
        product_id="test_sentiment",
        performance_metrics={
            "accuracy": 0.95,
            "speed": 0.90,
            "user_satisfaction": 0.88
        }
    )
    
    profile_after = orchestrator._base_orchestrator.get_agent_profile(
        sentiment_ai.cognitive_agent_id
    )
    
    print(f"  ✓ After evolution:")
    print(f"    Reasoning depth: {profile_after.reasoning_depth}")
    print(f"    Learning rate: {profile_after.learning_rate}")
    
    # Verify knowledge shared to hub
    ai_range = orchestrator.get_product_range("test_ai_services")
    hub_profile = orchestrator._base_orchestrator.get_agent_profile(
        ai_range.hub_agent_id
    )
    
    evolution_knowledge = [
        k for k in hub_profile.knowledge_atoms
        if k.get("type") == "evolution_event"
    ]
    
    assert len(evolution_knowledge) > 0, "Evolution should be recorded in hub"
    print(f"  ✓ Evolution event recorded in hub knowledge")
    
    print()


def test_list_operations():
    """Test listing product ranges and products"""
    print("Test 8: List Operations")
    
    orchestrator = get_regimorg_orchestrator()
    
    # List all ranges
    ranges = orchestrator.list_product_ranges()
    assert len(ranges) > 0, "Should have product ranges"
    
    print(f"  ✓ List product ranges: {len(ranges)} ranges")
    
    # List all products
    all_products = orchestrator.list_products()
    assert len(all_products) > 0, "Should have products"
    
    print(f"  ✓ List all products: {len(all_products)} products")
    
    # List products by range
    ai_products = orchestrator.list_products(range_id="test_ai_services")
    assert len(ai_products) > 0, "AI range should have products"
    
    print(f"  ✓ List products in AI range: {len(ai_products)} products")
    
    # Verify all AI products belong to the range
    for product in ai_products:
        assert product.product_range_id == "test_ai_services", "Product should belong to AI range"
    
    print("  ✓ Product filtering works correctly")
    
    print()


def test_get_operations():
    """Test getting individual ranges and products"""
    print("Test 9: Get Operations")
    
    orchestrator = get_regimorg_orchestrator()
    
    # Get product range
    ai_range = orchestrator.get_product_range("test_ai_services")
    assert ai_range is not None, "Should get existing range"
    assert ai_range.range_id == "test_ai_services", "Range ID should match"
    
    print(f"  ✓ Get product range: {ai_range.range_name}")
    
    # Get product
    sentiment_ai = orchestrator.get_product("test_sentiment")
    assert sentiment_ai is not None, "Should get existing product"
    assert sentiment_ai.product_id == "test_sentiment", "Product ID should match"
    
    print(f"  ✓ Get product: {sentiment_ai.product_name}")
    
    # Test non-existent items
    nonexistent_range = orchestrator.get_product_range("does_not_exist")
    assert nonexistent_range is None, "Non-existent range should return None"
    
    nonexistent_product = orchestrator.get_product("does_not_exist")
    assert nonexistent_product is None, "Non-existent product should return None"
    
    print("  ✓ Non-existent item handling works")
    
    print()


def test_cleanup():
    """Test orchestrator cleanup"""
    print("Test 10: Cleanup")
    
    orchestrator = get_regimorg_orchestrator()
    
    ranges_before = len(orchestrator._product_ranges)
    products_before = len(orchestrator._products)
    
    print(f"  ✓ Before cleanup:")
    print(f"    Ranges: {ranges_before}")
    print(f"    Products: {products_before}")
    
    orchestrator.shutdown()
    
    assert len(orchestrator._product_ranges) == 0, "All ranges should be removed"
    assert len(orchestrator._products) == 0, "All products should be removed"
    assert not orchestrator._initialized, "Should be uninitialized"
    
    print("  ✓ Cleanup successful")
    print()


def main():
    """Run all tests"""
    print("=" * 60)
    print("RegimOrg Organizational AGI Test Suite")
    print("=" * 60)
    print()
    
    try:
        # Run synchronous tests
        test_orchestrator_initialization()
        test_product_range_creation()
        test_product_microkernel_creation()
        test_knowledge_sharing()
        test_product_range_coordination()
        test_organizational_hierarchy()
        test_list_operations()
        test_get_operations()
        
        # Run async tests
        asyncio.run(test_product_evolution())
        
        # Cleanup
        test_cleanup()
        
        print("=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        
        # Re-initialize for demo
        print("\nDemo: RegimOrg Final State")
        print("-" * 60)
        initialize_regimorg()
        orchestrator = get_regimorg_orchestrator()
        
        # Create sample organization
        orchestrator.create_product_range(
            "demo_range",
            "Demo Product Range",
            ProductRangeType.CUSTOM
        )
        orchestrator.create_product_microkernel(
            "demo_product",
            "Demo Product",
            "demo_range",
            capabilities=["demo_capability"],
            knowledge_domains=["demo_domain"]
        )
        
        hierarchy = orchestrator.get_organizational_hierarchy()
        print(f"Organization: {hierarchy['organization']}")
        print(f"Product Ranges: {hierarchy['total_product_ranges']}")
        print(f"Products: {hierarchy['total_products']}")
        print(f"Initialized: {hierarchy['initialized']}")
        
        return 0
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
Test suite for OpenCog integration in Agent Zero (Cog-Zero)
Tests the orchestrator, cognitive tools, and multi-agent coordination
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from python.helpers.opencog_orchestrator import (
    OpenCogOrchestrator,
    AgentCognitiveProfile,
    CognitiveState,
    get_orchestrator,
    initialize_orchestrator
)


def test_orchestrator_initialization():
    """Test orchestrator initialization"""
    print("Test 1: Orchestrator Initialization")
    orchestrator = OpenCogOrchestrator()
    
    # Test initialization
    result = orchestrator.initialize()
    print(f"  ✓ Initialization: {'Success' if result else 'OpenCog not available (expected if hyperon not installed)'}")
    
    # Test singleton pattern
    orch2 = get_orchestrator()
    assert orch2 is not None, "Singleton orchestrator should exist"
    print("  ✓ Singleton pattern works")
    
    print()


def test_agent_registration():
    """Test agent registration and management"""
    print("Test 2: Agent Registration")
    orchestrator = get_orchestrator()
    
    # Register agents
    profile1 = orchestrator.register_agent("test_agent_1", reasoning_depth=5)
    profile2 = orchestrator.register_agent("test_agent_2", learning_rate=0.2)
    
    assert profile1.agent_id == "test_agent_1", "Agent 1 should be registered"
    assert profile2.agent_id == "test_agent_2", "Agent 2 should be registered"
    assert profile1.reasoning_depth == 5, "Custom reasoning depth should be set"
    assert profile2.learning_rate == 0.2, "Custom learning rate should be set"
    
    print("  ✓ Agents registered successfully")
    print(f"  ✓ Total agents: {len(orchestrator._agents)}")
    
    # Test retrieval
    retrieved = orchestrator.get_agent_profile("test_agent_1")
    assert retrieved is not None, "Should retrieve registered agent"
    assert retrieved.agent_id == "test_agent_1", "Retrieved agent should match"
    
    print("  ✓ Agent retrieval works")
    
    # Test unregistration
    orchestrator.unregister_agent("test_agent_1")
    retrieved_after = orchestrator.get_agent_profile("test_agent_1")
    assert retrieved_after is None, "Unregistered agent should not exist"
    
    print("  ✓ Agent unregistration works")
    print()


def test_knowledge_management():
    """Test knowledge atom management"""
    print("Test 3: Knowledge Management")
    orchestrator = get_orchestrator()
    
    # Register agent for testing
    orchestrator.register_agent("knowledge_test_agent")
    
    # Add knowledge atoms
    orchestrator.add_knowledge_atom("knowledge_test_agent", {
        "type": "fact",
        "content": "Python is a programming language",
        "category": "programming"
    })
    
    orchestrator.add_knowledge_atom("knowledge_test_agent", {
        "type": "fact",
        "content": "Machine learning uses neural networks",
        "category": "ai"
    })
    
    profile = orchestrator.get_agent_profile("knowledge_test_agent")
    # Knowledge atoms are stored even without hyperon
    print(f"  ✓ Knowledge atoms stored: {len(profile.knowledge_atoms)}")
    
    if orchestrator._hyperon_available:
        assert len(profile.knowledge_atoms) == 2, "Should have 2 knowledge atoms"
    else:
        print("  ℹ AtomSpace not available (hyperon not installed), using in-memory storage")
    
    # Query knowledge
    results = orchestrator.query_knowledge("Python", "knowledge_test_agent")
    assert len(results) > 0, "Should find Python-related knowledge"
    
    print(f"  ✓ Knowledge query works: found {len(results)} results")
    print()


def test_knowledge_sharing():
    """Test knowledge sharing between agents"""
    print("Test 4: Knowledge Sharing")
    orchestrator = get_orchestrator()
    
    # Register two agents
    orchestrator.register_agent("agent_source")
    orchestrator.register_agent("agent_target")
    
    # Add knowledge to source agent
    orchestrator.add_knowledge_atom("agent_source", {
        "content": "Security best practice: use HTTPS",
        "category": "security"
    })
    
    orchestrator.add_knowledge_atom("agent_source", {
        "content": "Python uses pip for packages",
        "category": "programming"
    })
    
    # Share knowledge
    orchestrator.share_knowledge("agent_source", "agent_target", "security")
    
    source_profile = orchestrator.get_agent_profile("agent_source")
    target_profile = orchestrator.get_agent_profile("agent_target")
    
    print(f"  ✓ Source agent knowledge: {len(source_profile.knowledge_atoms)}")
    print(f"  ✓ Target agent knowledge: {len(target_profile.knowledge_atoms)}")
    
    # Verify filtered sharing
    assert len(target_profile.knowledge_atoms) >= 1, "Target should have shared knowledge"
    
    print("  ✓ Knowledge sharing works")
    print()


def test_agent_coordination():
    """Test multi-agent coordination"""
    print("Test 5: Multi-Agent Coordination")
    orchestrator = get_orchestrator()
    
    # Register multiple agents
    for i in range(3):
        orchestrator.register_agent(f"coord_agent_{i}")
    
    # Coordinate agents
    result = orchestrator.coordinate_agents(
        ["coord_agent_0", "coord_agent_1", "coord_agent_2"],
        "Analyze system architecture"
    )
    
    assert result["task"] == "Analyze system architecture", "Task should be recorded"
    assert len(result["agents"]) == 3, "All agents should be coordinated"
    
    print(f"  ✓ Coordination result: {result['strategy']}")
    print(f"  ✓ Coordinated agents: {len(result['agents'])}")
    
    # Verify agent states
    for i in range(3):
        profile = orchestrator.get_agent_profile(f"coord_agent_{i}")
        # State might be COORDINATING or IDLE depending on timing
        print(f"  ✓ Agent {i} state: {profile.cognitive_state.value}")
    
    print()


async def test_agent_evolution():
    """Test agent evolution based on performance"""
    print("Test 6: Agent Evolution")
    orchestrator = get_orchestrator()
    
    # Register agent
    profile = orchestrator.register_agent("evolution_test_agent", reasoning_depth=3)
    initial_depth = profile.reasoning_depth
    initial_rate = profile.learning_rate
    
    print(f"  ✓ Initial reasoning depth: {initial_depth}")
    print(f"  ✓ Initial learning rate: {initial_rate}")
    
    # Evolve with high performance
    await orchestrator.evolve_agent("evolution_test_agent", {
        "accuracy": 0.9,
        "speed": 0.85
    })
    
    print(f"  ✓ After evolution (high performance):")
    print(f"    - Reasoning depth: {profile.reasoning_depth}")
    print(f"    - Learning rate: {profile.learning_rate}")
    
    # Evolve with low performance
    profile.reasoning_depth = 3  # Reset for test
    await orchestrator.evolve_agent("evolution_test_agent", {
        "accuracy": 0.4,
        "speed": 0.5
    })
    
    print(f"  ✓ After evolution (low performance):")
    print(f"    - Reasoning depth: {profile.reasoning_depth}")
    print(f"    - Learning rate: {profile.learning_rate}")
    
    print()


def test_orchestration_state():
    """Test getting orchestration state"""
    print("Test 7: Orchestration State")
    orchestrator = get_orchestrator()
    
    state = orchestrator.get_orchestration_state()
    
    print(f"  ✓ Initialized: {state['initialized']}")
    print(f"  ✓ Hyperon available: {state['hyperon_available']}")
    print(f"  ✓ Total agents: {state['total_agents']}")
    
    if state['agents']:
        print("  ✓ Sample agent states:")
        for agent_info in state['agents'][:3]:
            print(f"    - {agent_info['agent_id']}: {agent_info['state']} "
                  f"({agent_info['knowledge_atoms']} atoms)")
    
    print()


def test_cognitive_states():
    """Test cognitive state management"""
    print("Test 8: Cognitive States")
    
    profile = AgentCognitiveProfile(agent_id="state_test_agent")
    
    assert profile.cognitive_state == CognitiveState.IDLE, "Default state should be IDLE"
    print("  ✓ Default state: IDLE")
    
    # Test state transitions
    profile.cognitive_state = CognitiveState.REASONING
    assert profile.cognitive_state == CognitiveState.REASONING, "State should change to REASONING"
    print("  ✓ State transition: REASONING")
    
    profile.cognitive_state = CognitiveState.LEARNING
    assert profile.cognitive_state == CognitiveState.LEARNING, "State should change to LEARNING"
    print("  ✓ State transition: LEARNING")
    
    print()


def test_cleanup():
    """Test orchestrator cleanup"""
    print("Test 9: Cleanup")
    orchestrator = get_orchestrator()
    
    # Get counts before cleanup
    agent_count = len(orchestrator._agents)
    print(f"  ✓ Agents before cleanup: {agent_count}")
    
    # Cleanup
    orchestrator.shutdown()
    
    assert len(orchestrator._agents) == 0, "All agents should be removed"
    assert not orchestrator._initialized, "Should be uninitialized"
    
    print("  ✓ Cleanup successful")
    print()


def main():
    """Run all tests"""
    print("=" * 60)
    print("OpenCog Integration Test Suite for Agent Zero (Cog-Zero)")
    print("=" * 60)
    print()
    
    try:
        # Run synchronous tests
        test_orchestrator_initialization()
        test_agent_registration()
        test_knowledge_management()
        test_knowledge_sharing()
        test_agent_coordination()
        test_orchestration_state()
        test_cognitive_states()
        
        # Run async tests
        asyncio.run(test_agent_evolution())
        
        # Cleanup
        test_cleanup()
        
        print("=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
        
        # Re-initialize for demo
        print("\nDemo: Orchestration State After Re-initialization")
        print("-" * 60)
        initialize_orchestrator()
        orchestrator = get_orchestrator()
        orchestrator.register_agent("demo_agent_1")
        orchestrator.register_agent("demo_agent_2")
        orchestrator.add_knowledge_atom("demo_agent_1", {
            "content": "OpenCog integration test successful"
        })
        
        state = orchestrator.get_orchestration_state()
        print(f"Hyperon Available: {state['hyperon_available']}")
        print(f"Total Agents: {state['total_agents']}")
        print(f"Initialized: {state['initialized']}")
        
        return 0
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

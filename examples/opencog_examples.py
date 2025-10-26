#!/usr/bin/env python3
"""
Example: OpenCog Integration with Agent Zero (Cog-Zero)
Demonstrates cognitive reasoning and multi-agent orchestration
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from python.helpers.opencog_orchestrator import get_orchestrator, initialize_orchestrator


def example_basic_usage():
    """Example 1: Basic orchestrator usage"""
    print("=" * 70)
    print("Example 1: Basic OpenCog Orchestrator Usage")
    print("=" * 70)
    
    # Initialize the orchestrator
    initialize_orchestrator()
    orchestrator = get_orchestrator()
    
    # Register agents
    agent1 = orchestrator.register_agent("research_agent", reasoning_depth=5)
    agent2 = orchestrator.register_agent("analysis_agent", reasoning_depth=4)
    
    print(f"✓ Registered {len(orchestrator._agents)} agents")
    print(f"  - {agent1.agent_id} (depth: {agent1.reasoning_depth})")
    print(f"  - {agent2.agent_id} (depth: {agent2.reasoning_depth})")
    print()


def example_knowledge_management():
    """Example 2: Knowledge storage and retrieval"""
    print("=" * 70)
    print("Example 2: Cognitive Knowledge Management")
    print("=" * 70)
    
    orchestrator = get_orchestrator()
    
    # Add knowledge to an agent
    orchestrator.add_knowledge_atom("research_agent", {
        "type": "fact",
        "content": "OpenCog Hyperon provides cognitive architecture for AGI research",
        "category": "ai_architecture",
        "confidence": 0.95
    })
    
    orchestrator.add_knowledge_atom("research_agent", {
        "type": "fact",
        "content": "Agent Zero is a dynamic, learning agentic framework",
        "category": "frameworks",
        "confidence": 0.98
    })
    
    print("✓ Added knowledge atoms to research_agent")
    
    # Query knowledge
    results = orchestrator.query_knowledge("OpenCog", "research_agent")
    print(f"✓ Query 'OpenCog' found {len(results)} results")
    
    print()


def example_multi_agent_coordination():
    """Example 3: Coordinate multiple agents"""
    print("=" * 70)
    print("Example 3: Multi-Agent Coordination")
    print("=" * 70)
    
    orchestrator = get_orchestrator()
    
    # Register additional agents for coordination
    orchestrator.register_agent("coding_agent")
    orchestrator.register_agent("testing_agent")
    
    # Coordinate agents on a task
    task = "Develop and test a secure authentication system"
    coordination = orchestrator.coordinate_agents(
        ["coding_agent", "testing_agent"],
        task
    )
    
    print(f"✓ Coordination initiated")
    print(f"✓ Strategy: {coordination['strategy']}")
    print(f"✓ Coordinated agents: {len(coordination['agents'])}")
    
    print()


async def main():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + "  OpenCog Integration Examples (Cog-Zero)".center(70) + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    try:
        example_basic_usage()
        example_knowledge_management()
        example_multi_agent_coordination()
        
        print("=" * 70)
        print("✓ Examples completed!")
        print("=" * 70)
        print("\nSee docs/opencog_integration.md for detailed guide")
        print()
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

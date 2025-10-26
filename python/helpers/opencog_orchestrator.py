"""
OpenCog Hyperon Orchestrator for Agent Zero
Provides cognitive architecture and multi-agent orchestration capabilities
"""

import asyncio
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class CognitiveState(Enum):
    """States for cognitive processing"""
    IDLE = "idle"
    REASONING = "reasoning"
    LEARNING = "learning"
    COORDINATING = "coordinating"
    EVOLVING = "evolving"


@dataclass
class AgentCognitiveProfile:
    """Cognitive profile for an agent in the orchestration system"""
    agent_id: str
    cognitive_state: CognitiveState = CognitiveState.IDLE
    knowledge_atoms: List[Any] = field(default_factory=list)
    reasoning_depth: int = 3
    learning_rate: float = 0.1
    evolution_enabled: bool = True
    
    
class OpenCogOrchestrator:
    """
    OpenCog Hyperon-based orchestrator for Agent Zero
    Provides cognitive architecture capabilities including:
    - Knowledge representation via AtomSpace
    - Multi-agent coordination
    - Adaptive evolutionary learning
    - Pattern matching and reasoning
    """
    
    def __init__(self):
        self._initialized = False
        self._atomspace = None
        self._agents: Dict[str, AgentCognitiveProfile] = {}
        self._shared_knowledge: List[Any] = []
        self._hyperon_available = False
        
        # Try to import hyperon
        try:
            import hyperon
            self._hyperon_available = True
            self._hyperon = hyperon
        except ImportError:
            self._hyperon_available = False
            
    def initialize(self) -> bool:
        """
        Initialize the OpenCog orchestrator
        Returns True if successful, False otherwise
        """
        if self._initialized:
            return True
            
        if not self._hyperon_available:
            print("OpenCog Hyperon not available. Install with: pip install hyperon")
            return False
            
        try:
            # Initialize AtomSpace for knowledge representation
            from hyperon import AtomSpace, MeTTa
            self._atomspace = AtomSpace()
            self._metta = MeTTa(space=self._atomspace)
            self._initialized = True
            return True
        except Exception as e:
            print(f"Failed to initialize OpenCog orchestrator: {e}")
            return False
            
    def register_agent(self, agent_id: str, **kwargs) -> AgentCognitiveProfile:
        """
        Register an agent with the cognitive orchestrator
        
        Args:
            agent_id: Unique identifier for the agent
            **kwargs: Additional cognitive profile parameters
            
        Returns:
            AgentCognitiveProfile instance
        """
        if agent_id in self._agents:
            return self._agents[agent_id]
            
        profile = AgentCognitiveProfile(
            agent_id=agent_id,
            reasoning_depth=kwargs.get("reasoning_depth", 3),
            learning_rate=kwargs.get("learning_rate", 0.1),
            evolution_enabled=kwargs.get("evolution_enabled", True)
        )
        
        self._agents[agent_id] = profile
        return profile
        
    def unregister_agent(self, agent_id: str):
        """Remove an agent from the orchestrator"""
        if agent_id in self._agents:
            del self._agents[agent_id]
            
    def get_agent_profile(self, agent_id: str) -> Optional[AgentCognitiveProfile]:
        """Get cognitive profile for an agent"""
        return self._agents.get(agent_id)
        
    def add_knowledge_atom(self, agent_id: str, atom_data: Dict[str, Any]):
        """
        Add a knowledge atom to an agent's cognitive profile
        
        Args:
            agent_id: Agent identifier
            atom_data: Knowledge data to store as an atom
        """
        profile = self._agents.get(agent_id)
        if profile:
            # Always store in profile's knowledge atoms
            profile.knowledge_atoms.append(atom_data)
            
            # Add to shared AtomSpace if available and initialized
            if self._initialized and self._atomspace and self._hyperon_available:
                try:
                    # Store knowledge in MeTTa format
                    knowledge_str = f"(knowledge {agent_id} {atom_data})"
                    self._metta.run(knowledge_str)
                except Exception as e:
                    print(f"Error adding atom to AtomSpace: {e}")
                    
    def share_knowledge(self, source_agent_id: str, target_agent_id: str, 
                       knowledge_filter: Optional[str] = None):
        """
        Share knowledge between agents
        
        Args:
            source_agent_id: Source agent
            target_agent_id: Target agent
            knowledge_filter: Optional filter for knowledge sharing
        """
        source = self._agents.get(source_agent_id)
        target = self._agents.get(target_agent_id)
        
        if not source or not target:
            return
            
        # Copy relevant knowledge atoms
        if knowledge_filter:
            # Filter knowledge based on criteria
            shared = [atom for atom in source.knowledge_atoms 
                     if knowledge_filter in str(atom)]
        else:
            # Share all knowledge
            shared = source.knowledge_atoms.copy()
            
        target.knowledge_atoms.extend(shared)
        
    def coordinate_agents(self, agent_ids: List[str], task: str) -> Dict[str, Any]:
        """
        Coordinate multiple agents for a complex task
        
        Args:
            agent_ids: List of agent IDs to coordinate
            task: Task description
            
        Returns:
            Coordination result with agent assignments
        """
        coordination_result = {
            "task": task,
            "agents": [],
            "strategy": "distributed",
            "status": "pending"
        }
        
        for agent_id in agent_ids:
            profile = self._agents.get(agent_id)
            if profile:
                profile.cognitive_state = CognitiveState.COORDINATING
                coordination_result["agents"].append({
                    "agent_id": agent_id,
                    "state": profile.cognitive_state.value,
                    "assigned": True
                })
                
        return coordination_result
        
    async def evolve_agent(self, agent_id: str, performance_metrics: Dict[str, float]):
        """
        Evolve an agent's cognitive capabilities based on performance
        
        Args:
            agent_id: Agent identifier
            performance_metrics: Performance metrics for evolution
        """
        profile = self._agents.get(agent_id)
        if not profile or not profile.evolution_enabled:
            return
            
        profile.cognitive_state = CognitiveState.EVOLVING
        
        # Adaptive learning rate adjustment
        if performance_metrics.get("accuracy", 0) > 0.8:
            profile.reasoning_depth = min(profile.reasoning_depth + 1, 10)
        elif performance_metrics.get("accuracy", 0) < 0.5:
            profile.learning_rate = min(profile.learning_rate * 1.1, 0.5)
            
        profile.cognitive_state = CognitiveState.IDLE
        
    def get_orchestration_state(self) -> Dict[str, Any]:
        """
        Get current state of the orchestration system
        
        Returns:
            Dictionary with orchestration state information
        """
        return {
            "initialized": self._initialized,
            "hyperon_available": self._hyperon_available,
            "total_agents": len(self._agents),
            "agents": [
                {
                    "agent_id": agent_id,
                    "state": profile.cognitive_state.value,
                    "knowledge_atoms": len(profile.knowledge_atoms),
                    "reasoning_depth": profile.reasoning_depth
                }
                for agent_id, profile in self._agents.items()
            ]
        }
        
    def query_knowledge(self, query: str, agent_id: Optional[str] = None) -> List[Any]:
        """
        Query knowledge from AtomSpace or in-memory storage
        
        Args:
            query: Query string
            agent_id: Optional agent ID to query specific agent knowledge
            
        Returns:
            List of matching knowledge atoms
        """
        results = []
        
        if agent_id:
            # Query specific agent's knowledge
            profile = self._agents.get(agent_id)
            if profile:
                results = [atom for atom in profile.knowledge_atoms 
                          if query.lower() in str(atom).lower()]
        else:
            # Query all agents' knowledge
            for profile in self._agents.values():
                results.extend([atom for atom in profile.knowledge_atoms 
                              if query.lower() in str(atom).lower()])
                              
        return results
        
    def shutdown(self):
        """Shutdown the orchestrator and clean up resources"""
        self._agents.clear()
        self._shared_knowledge.clear()
        self._initialized = False


# Global singleton instance
_global_orchestrator: Optional[OpenCogOrchestrator] = None


def get_orchestrator() -> OpenCogOrchestrator:
    """Get or create the global OpenCog orchestrator instance"""
    global _global_orchestrator
    if _global_orchestrator is None:
        _global_orchestrator = OpenCogOrchestrator()
    return _global_orchestrator


def initialize_orchestrator() -> bool:
    """Initialize the global orchestrator"""
    orchestrator = get_orchestrator()
    return orchestrator.initialize()

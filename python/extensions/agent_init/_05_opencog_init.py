"""
OpenCog Integration Extension for Agent Zero
Initializes OpenCog orchestrator when agent is created
"""

from python.helpers.extension import Extension
from python.helpers.opencog_orchestrator import get_orchestrator


class OpenCogInitExtension(Extension):
    """
    Extension that initializes OpenCog cognitive capabilities for agents
    """
    
    async def execute(self, **kwargs):
        """
        Initialize OpenCog orchestrator and register this agent
        """
        
        orchestrator = get_orchestrator()
        
        # Initialize orchestrator if not already initialized
        if not orchestrator._initialized:
            success = orchestrator.initialize()
            if success:
                self.agent.context.log.log(
                    type="info",
                    heading="OpenCog Hyperon Initialized",
                    content="Cognitive architecture ready for multi-agent orchestration",
                )
        
        # Register this agent with the orchestrator
        agent_id = f"agent_{self.agent.number}"
        profile = orchestrator.register_agent(
            agent_id,
            reasoning_depth=3,
            learning_rate=0.1,
            evolution_enabled=True
        )
        
        # Store orchestrator reference in agent data
        self.agent.set_data("opencog_orchestrator", orchestrator)
        self.agent.set_data("cognitive_profile", profile)
        self.agent.set_data("cognitive_agent_id", agent_id)

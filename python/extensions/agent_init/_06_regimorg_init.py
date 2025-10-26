"""
RegimOrg Initialization Extension
Initializes the RegimOrg organizational AGI orchestrator when agents are created
"""

from python.helpers.extension import Extension
from python.helpers.regimorg_orchestrator import get_regimorg_orchestrator


class RegimOrgInitExtension(Extension):
    """
    Extension that initializes RegimOrg organizational capabilities
    """
    
    async def execute(self, **kwargs):
        """
        Initialize RegimOrg orchestrator if this is agent 0
        """
        
        # Only initialize for the root agent (agent 0)
        if self.agent.number == 0:
            orchestrator = get_regimorg_orchestrator()
            
            # Initialize orchestrator if not already initialized
            if not orchestrator._initialized:
                success = orchestrator.initialize()
                if success:
                    self.agent.context.log.log(
                        type="info",
                        heading="RegimOrg Organizational AGI Initialized",
                        content="Multi-agent organizational orchestrator ready for regimazone.org",
                    )
            
            # Store orchestrator reference in agent data
            self.agent.set_data("regimorg_orchestrator", orchestrator)

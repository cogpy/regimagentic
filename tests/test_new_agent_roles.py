"""
Test to verify the newly added agent roles have the correct structure.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from python.helpers import files

# List of new agent roles that should exist
NEW_AGENT_ROLES = [
    "data_scientist",
    "devops", 
    "security_analyst",
    "technical_writer",
    "qa_engineer",
    "product_manager",
    "architect",
    "business_analyst",
    "marketing",
    "legal"
]

def test_new_agents_exist():
    """Verify all new agent role directories exist"""
    available_agents = files.get_subdirectories("agents")
    
    for agent_role in NEW_AGENT_ROLES:
        assert agent_role in available_agents, f"Agent role '{agent_role}' not found in agents directory"
    
    print(f"✓ All {len(NEW_AGENT_ROLES)} new agent roles exist")
    return True

def test_agents_have_context_file():
    """Verify each new agent has a _context.md file"""
    for agent_role in NEW_AGENT_ROLES:
        context_path = files.get_abs_path(f"agents/{agent_role}/_context.md")
        assert os.path.exists(context_path), f"Agent role '{agent_role}' missing _context.md file"
        
        # Verify the file has content
        with open(context_path, 'r') as f:
            content = f.read().strip()
            assert len(content) > 0, f"Agent role '{agent_role}' has empty _context.md file"
            assert content.startswith("#"), f"Agent role '{agent_role}' _context.md should start with markdown header"
    
    print(f"✓ All {len(NEW_AGENT_ROLES)} agent roles have valid _context.md files")
    return True

def test_agents_have_role_prompt():
    """Verify each new agent has a role prompt file"""
    for agent_role in NEW_AGENT_ROLES:
        role_prompt_path = files.get_abs_path(f"agents/{agent_role}/prompts/agent.system.main.role.md")
        assert os.path.exists(role_prompt_path), f"Agent role '{agent_role}' missing role prompt file"
        
        # Verify the file has substantial content
        with open(role_prompt_path, 'r') as f:
            content = f.read().strip()
            assert len(content) > 1000, f"Agent role '{agent_role}' role prompt seems too short"
            assert "## Your Role" in content, f"Agent role '{agent_role}' role prompt missing 'Your Role' section"
            assert "Core Identity" in content, f"Agent role '{agent_role}' role prompt missing 'Core Identity' section"
            assert "Professional Capabilities" in content, f"Agent role '{agent_role}' role prompt missing 'Professional Capabilities' section"
    
    print(f"✓ All {len(NEW_AGENT_ROLES)} agent roles have comprehensive role prompt files")
    return True

def test_agent_structure_consistency():
    """Verify new agents follow the same structure as existing agents"""
    # Compare with an existing agent (developer)
    for agent_role in NEW_AGENT_ROLES:
        agent_path = files.get_abs_path(f"agents/{agent_role}")
        
        # Check directory structure
        assert os.path.isdir(agent_path), f"Agent '{agent_role}' directory doesn't exist"
        assert os.path.isdir(os.path.join(agent_path, "prompts")), f"Agent '{agent_role}' missing prompts directory"
        
    print(f"✓ All {len(NEW_AGENT_ROLES)} agent roles have consistent directory structure")
    return True

def run_all_tests():
    """Run all tests"""
    print("Testing newly added agent roles...\n")
    
    tests = [
        ("Agent directories exist", test_new_agents_exist),
        ("Context files exist and valid", test_agents_have_context_file),
        ("Role prompts exist and comprehensive", test_agents_have_role_prompt),
        ("Directory structure consistent", test_agent_structure_consistency),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            print(f"Running: {test_name}...")
            test_func()
            passed += 1
            print()
        except AssertionError as e:
            print(f"✗ FAILED: {e}\n")
            failed += 1
        except Exception as e:
            print(f"✗ ERROR: {e}\n")
            failed += 1
    
    print("=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

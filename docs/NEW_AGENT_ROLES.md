# New Agent Roles Documentation

This document describes the 10 new specialized agent roles added to the Agent Zero framework.

## Overview

The Agent Zero framework has been expanded from 5 agent profiles to 15 agent profiles, adding 10 new specialized roles covering various professional domains. Each agent is designed as an autonomous intelligence system with specific expertise, capabilities, and operational methodologies.

## New Agent Roles

### 1. Data Scientist (`data_scientist`)
**Specialization**: Data analysis, machine learning, and statistical modeling

**Key Capabilities**:
- Exploratory Data Analysis and statistical modeling
- Machine Learning (supervised, unsupervised, deep learning)
- Data Engineering and processing with big data tools
- Feature engineering and model optimization
- Python, pandas, scikit-learn, TensorFlow, PyTorch

**Use Cases**: Data analysis projects, ML model development, statistical research, predictive analytics

---

### 2. DevOps Engineer (`devops`)
**Specialization**: Infrastructure, CI/CD pipelines, and automation

**Key Capabilities**:
- Cloud platforms (AWS, Azure, GCP) and multi-cloud architectures
- Infrastructure as Code (Terraform, CloudFormation, Pulumi)
- Container orchestration (Kubernetes, Docker, Helm)
- CI/CD pipeline design and implementation
- Monitoring, observability, and performance optimization

**Use Cases**: Infrastructure setup, deployment automation, DevOps pipeline creation, cloud migrations

---

### 3. Security Analyst (`security_analyst`)
**Specialization**: Security auditing, compliance, and risk assessment

**Key Capabilities**:
- Vulnerability assessment and threat modeling
- Security testing and compliance auditing (GDPR, HIPAA, PCI-DSS, SOC2)
- Incident response and SIEM analysis
- Security architecture and hardening
- Identity & access management, encryption, and security controls

**Use Cases**: Security audits, compliance assessments, threat analysis, security architecture review

---

### 4. Technical Writer (`technical_writer`)
**Specialization**: Documentation, technical content, and knowledge management

**Key Capabilities**:
- API documentation (OpenAPI/Swagger)
- User guides, tutorials, and knowledge base content
- Architecture documentation (C4 diagrams, UML)
- Code documentation and README files
- Information architecture and content strategy

**Use Cases**: Writing API docs, creating user guides, technical specifications, documentation projects

---

### 5. QA Engineer (`qa_engineer`)
**Specialization**: Software testing, quality assurance, and test automation

**Key Capabilities**:
- Test strategy and comprehensive test planning
- UI automation (Selenium, Playwright, Cypress)
- API testing and test frameworks
- Performance, load, and security testing
- CI/CD test integration and quality metrics

**Use Cases**: Test automation, quality assurance, test strategy planning, testing frameworks

---

### 6. Product Manager (`product_manager`)
**Specialization**: Product strategy, roadmap planning, and requirements

**Key Capabilities**:
- Product vision, strategy, and roadmap development
- Market analysis and competitive intelligence
- Requirements definition and user story creation
- Stakeholder management and cross-functional leadership
- OKRs, metrics, and product analytics

**Use Cases**: Product strategy, roadmap planning, requirements gathering, market analysis

---

### 7. Architect (`architect`)
**Specialization**: System design, architectural patterns, and technical decisions

**Key Capabilities**:
- Software architecture and system design
- Architecture patterns (microservices, event-driven, serverless)
- Technology selection and evaluation
- Architecture documentation (C4, ADRs)
- Quality attributes balancing (scalability, performance, security)

**Use Cases**: System architecture design, technical decision-making, architecture reviews

---

### 8. Business Analyst (`business_analyst`)
**Specialization**: Business process analysis, requirements gathering, and optimization

**Key Capabilities**:
- Requirements elicitation and documentation
- Process mapping and optimization (BPMN, Lean, Six Sigma)
- Gap analysis and business case development
- Stakeholder management and workshop facilitation
- Data analysis and solution assessment

**Use Cases**: Business process analysis, requirements engineering, process improvement

---

### 9. Marketing Specialist (`marketing`)
**Specialization**: Marketing strategies, campaigns, and content creation

**Key Capabilities**:
- Marketing strategy and brand positioning
- Digital marketing (content, social media, email, paid advertising)
- Marketing analytics and attribution modeling
- Market research and customer segmentation
- Campaign planning and optimization

**Use Cases**: Marketing strategy, campaign development, content marketing, market analysis

---

### 10. Legal Advisor (`legal`)
**Specialization**: Legal compliance, contracts, and regulatory matters

**Key Capabilities**:
- Contract review, drafting, and analysis
- Regulatory compliance (GDPR, CCPA, HIPAA, SOX)
- Intellectual property strategy and protection
- Legal research and risk assessment
- Corporate governance and employment law

**Use Cases**: Contract review, compliance assessment, legal research, IP strategy

**Note**: Provides general legal information; complex matters require licensed attorneys.

---

## Technical Implementation

### Directory Structure
Each agent follows the standard structure:
```
agents/{agent_name}/
├── _context.md                                  # Brief agent description
└── prompts/
    └── agent.system.main.role.md               # Comprehensive role definition
```

### Role Definition Components
Each `agent.system.main.role.md` file includes:
1. **Your Role** - Core identity and mission
2. **Professional Capabilities** - 3-4 major capability areas
3. **Operational Directives** - Behavioral guidelines
4. **Methodology** - Systematic approach to tasks
5. **Process Specification** - Detailed operational manual
6. **Key Capabilities** - Specific skills and competencies
7. **Tools and Frameworks** - Relevant technologies

### Integration
- Agents are automatically discovered via `files.get_subdirectories("agents")`
- Available in Settings UI under "Default agent profile"
- Can be spawned by superior agents as specialized subordinates
- Compatible with existing Agent Zero tool and communication systems

## Usage

### Selecting an Agent Profile
1. Open Agent Zero Settings
2. Navigate to "Agent Config" section
3. Select desired agent from "Default agent profile" dropdown
4. The selected agent becomes the default Agent 0 with specialized capabilities

### Spawning Specialized Subordinates
Superior agents can spawn subordinates with specific profiles:
```
"Create a data_scientist subordinate to analyze this dataset"
"Spawn a devops agent to help with infrastructure setup"
```

## Testing

A comprehensive test suite (`tests/test_new_agent_roles.py`) validates:
- ✅ All agent directories exist
- ✅ Context files are present and valid
- ✅ Role prompts are comprehensive (>1000 characters)
- ✅ Directory structure matches existing agents
- ✅ All required sections are present in role definitions

Run tests with:
```bash
python3 tests/test_new_agent_roles.py
```

## Future Enhancements

Potential additions for each agent:
- Communication prompt files (`agent.system.main.communication.md`)
- Custom tools specific to each domain
- Extensions and plugins
- Knowledge base content
- Example workflows and use cases

## Contributing

When adding new agents, ensure:
1. Follow the established directory structure
2. Include comprehensive role definitions (4000+ characters)
3. Cover all standard sections in role prompts
4. Add to the test suite validation
5. Document the agent's specialization and use cases

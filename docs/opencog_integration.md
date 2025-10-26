# OpenCog Integration for Agent Zero (Cog-Zero)

## Overview

This integration brings OpenCog Hyperon's cognitive architecture capabilities to Agent Zero, creating a powerful multi-agent orchestration workbench called **Cog-Zero**. It enables adaptive evolutionary agentic frameworks embedded in living dynamical systems.

## What is OpenCog Hyperon?

OpenCog Hyperon is the next-generation cognitive architecture platform that provides:
- **AtomSpace**: Knowledge representation and graph-based memory
- **MeTTa**: Meta-programming language for cognitive processes
- **Pattern Matching**: Advanced pattern recognition and inference
- **Evolutionary Learning**: Adaptive learning mechanisms

## Installation

### Prerequisites
- Python 3.7 or newer
- Agent Zero installation (existing)

### Installing OpenCog Hyperon

The integration automatically uses OpenCog Hyperon if available. To install:

```bash
pip install hyperon
```

Or update your Agent Zero installation:

```bash
pip install -r requirements.txt
```

The OpenCog integration will automatically initialize when agents are created.

## Architecture

### Components

1. **OpenCog Orchestrator** (`python/helpers/opencog_orchestrator.py`)
   - Central cognitive coordination system
   - Manages agent cognitive profiles
   - Maintains shared AtomSpace for knowledge
   - Coordinates multi-agent collaboration

2. **Cognitive Tools**
   - `cognitive_reasoning`: Advanced reasoning using OpenCog
   - `cognitive_knowledge`: Knowledge storage and retrieval

3. **Extensions**
   - `_05_opencog_init.py`: Initializes OpenCog for each agent

### Integration Points

```
Agent Zero Framework
├── Agent Initialization
│   └── OpenCog Extension → Registers agent with orchestrator
├── Tools
│   ├── cognitive_reasoning → Pattern matching, inference, coordination
│   └── cognitive_knowledge → Learn, retrieve, organize knowledge
└── Memory System
    └── AtomSpace Integration → Persistent cognitive memory
```

## Features

### 1. Cognitive Reasoning

Perform advanced reasoning operations:

```python
# Example: Inference reasoning
{
    "tool_name": "cognitive_reasoning",
    "tool_args": {
        "query": "What are the security implications of this API?",
        "reasoning_type": "inference",
        "depth": 5
    }
}
```

**Reasoning Types:**
- **Inference**: Draw conclusions from existing knowledge
- **Pattern Match**: Find patterns and relationships
- **Coordination**: Multi-agent collaborative reasoning

### 2. Knowledge Management

Store and retrieve knowledge in cognitive architecture:

```python
# Learn new knowledge
{
    "tool_name": "cognitive_knowledge",
    "tool_args": {
        "action": "learn",
        "content": "API keys should be stored in environment variables",
        "category": "security"
    }
}

# Retrieve knowledge
{
    "tool_name": "cognitive_knowledge",
    "tool_args": {
        "action": "retrieve",
        "content": "API security"
    }
}
```

### 3. Multi-Agent Orchestration

Coordinate multiple agents using cognitive architecture:

```python
{
    "tool_name": "cognitive_reasoning",
    "tool_args": {
        "query": "Analyze this complex system",
        "reasoning_type": "coordination",
        "share_with_agents": "agent_1, agent_2, agent_3"
    }
}
```

### 4. Adaptive Evolution

Agents automatically evolve based on performance:
- Reasoning depth adjusts based on task complexity
- Learning rates adapt to success/failure patterns
- Cognitive profiles optimize over time

## Usage Examples

### Example 1: Building a Knowledge Base

```python
# Agent learns facts
{
    "tool_name": "cognitive_knowledge",
    "tool_args": {
        "action": "learn",
        "content": "Python uses indentation for code blocks",
        "category": "programming"
    }
}

# Later, retrieve and reason about it
{
    "tool_name": "cognitive_reasoning",
    "tool_args": {
        "query": "Python code structure",
        "reasoning_type": "pattern_match"
    }
}
```

### Example 2: Multi-Agent Collaboration

Agent 0 coordinates with subordinates:

```python
# Coordinate agents for complex analysis
{
    "tool_name": "cognitive_reasoning",
    "tool_args": {
        "query": "Perform comprehensive security audit",
        "reasoning_type": "coordination",
        "share_with_agents": "agent_1, agent_2"
    }
}
```

### Example 3: Pattern Recognition

```python
{
    "tool_name": "cognitive_reasoning",
    "tool_args": {
        "query": "authentication mechanisms",
        "reasoning_type": "pattern_match",
        "depth": 7
    }
}
```

## How It Works

### Agent Registration

When an agent is initialized:
1. OpenCog orchestrator initializes (if not already)
2. Agent is registered with a cognitive profile
3. AtomSpace is prepared for knowledge storage
4. Cognitive capabilities are enabled

### Knowledge Flow

```
User Input → Agent Processing → Cognitive Tools
                                      ↓
                              OpenCog AtomSpace
                                      ↓
                    Pattern Matching & Reasoning
                                      ↓
                              Agent Response
```

### Multi-Agent Coordination

```
Agent 0 (Superior)
    ↓
Cognitive Orchestrator
    ↓
├── Agent 1 (Subordinate) → Shared AtomSpace
├── Agent 2 (Subordinate) → Shared AtomSpace
└── Agent 3 (Subordinate) → Shared AtomSpace
```

## Advanced Configuration

### Cognitive Profile Parameters

Agents can be configured with custom cognitive parameters:

```python
# In agent initialization
orchestrator.register_agent(
    agent_id="agent_1",
    reasoning_depth=5,      # Depth of reasoning (1-10)
    learning_rate=0.15,     # Adaptation speed
    evolution_enabled=True  # Enable adaptive evolution
)
```

### Performance Metrics

Monitor and evolve agents based on performance:

```python
await orchestrator.evolve_agent(
    agent_id="agent_1",
    performance_metrics={
        "accuracy": 0.85,
        "speed": 0.90,
        "resource_efficiency": 0.75
    }
)
```

## API Reference

### OpenCogOrchestrator

Main orchestrator class for cognitive coordination.

**Methods:**
- `initialize()` - Initialize the orchestrator
- `register_agent(agent_id, **kwargs)` - Register an agent
- `add_knowledge_atom(agent_id, atom_data)` - Add knowledge
- `share_knowledge(source, target, filter)` - Share between agents
- `coordinate_agents(agent_ids, task)` - Coordinate multiple agents
- `evolve_agent(agent_id, metrics)` - Evolve agent capabilities
- `query_knowledge(query, agent_id)` - Query knowledge base
- `get_orchestration_state()` - Get system state

### cognitive_reasoning Tool

**Parameters:**
- `query` (str, required) - Reasoning query
- `reasoning_type` (str) - Type: inference, pattern_match, coordination
- `depth` (int) - Reasoning depth 1-10
- `share_with_agents` (str) - Comma-separated agent IDs

### cognitive_knowledge Tool

**Parameters:**
- `action` (str, required) - Action: learn, retrieve, list
- `content` (str) - Content to learn or query
- `category` (str) - Knowledge category

## Benefits

1. **Enhanced Reasoning**: Beyond simple LLM reasoning with cognitive architecture
2. **Knowledge Persistence**: AtomSpace provides robust knowledge storage
3. **Multi-Agent Synergy**: Agents share and coordinate knowledge
4. **Adaptive Learning**: Agents improve over time through evolution
5. **Pattern Recognition**: Advanced pattern matching capabilities
6. **Scalability**: Handles complex multi-agent orchestration

## Troubleshooting

### OpenCog Not Available

If you see messages about OpenCog not being available:

```bash
pip install hyperon
```

Restart your Agent Zero instance after installation.

### Knowledge Not Persisting

Knowledge is session-based. For persistent storage:
- Use the regular memory tools for long-term storage
- Cognitive knowledge is optimized for session reasoning

### Agent Coordination Issues

Ensure all agents are registered before coordination:
- Subordinate agents are automatically registered
- Check orchestration state: `get_orchestration_state()`

## Performance Considerations

- **Reasoning Depth**: Higher depths (7-10) are more thorough but slower
- **Knowledge Volume**: Large knowledge bases may slow queries
- **Agent Count**: Coordination scales with agent count
- **Memory**: AtomSpace uses memory for knowledge storage

## Future Enhancements

Planned features:
- Persistent AtomSpace storage
- Advanced evolutionary algorithms
- Integration with Agent Zero's existing memory system
- Visual cognitive architecture dashboard
- Real-time cognitive state monitoring
- Custom reasoning patterns

## Contributing

To extend the OpenCog integration:

1. Add new tools in `python/tools/`
2. Create prompt files in `prompts/agent.system.tool.*.md`
3. Extend orchestrator in `python/helpers/opencog_orchestrator.py`
4. Add extensions in `python/extensions/`

## References

- [OpenCog Hyperon](https://hyperon.opencog.org/)
- [Agent Zero Documentation](../README.md)
- [MeTTa Language](https://github.com/trueagi-io/metta-lang)
- [AtomSpace Specification](https://wiki.opencog.org/w/AtomSpace)

## License

This integration follows the same license as Agent Zero.

---

**Note**: This integration requires `hyperon>=0.2.8`. The system gracefully handles cases where OpenCog is not installed, allowing Agent Zero to function normally without cognitive features.

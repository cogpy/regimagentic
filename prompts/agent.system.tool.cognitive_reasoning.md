# Cognitive Reasoning Tool

Use this tool to perform advanced cognitive reasoning using OpenCog Hyperon architecture.

## When to Use
- When you need to perform complex reasoning beyond simple logic
- When you want to find patterns in your knowledge
- When coordinating with other agents on complex tasks
- When making inferences from existing knowledge

## Capabilities
1. **Inference**: Draw conclusions from existing knowledge
2. **Pattern Matching**: Find patterns and relationships in knowledge
3. **Coordination**: Coordinate reasoning across multiple agents

## Usage

```python
{
    "thoughts": [
        "I need to perform cognitive reasoning on the user's query",
        "I will use inference to draw conclusions from my knowledge base"
    ],
    "tool_name": "cognitive_reasoning",
    "tool_args": {
        "query": "What are the relationships between machine learning and neural networks?",
        "reasoning_type": "inference",
        "depth": 3,
        "share_with_agents": ""
    }
}
```

## Parameters

- **query** (required): The reasoning query or problem to analyze
- **reasoning_type** (optional): Type of reasoning - inference, pattern_match, or coordination (default: inference)
- **depth** (optional): Reasoning depth from 1-10 (default: 3)
- **share_with_agents** (optional): Comma-separated agent IDs to share results with

## Notes
- Knowledge must be stored first using the cognitive_knowledge tool
- Higher reasoning depth may take longer but provide deeper insights
- Coordination requires multiple registered agents

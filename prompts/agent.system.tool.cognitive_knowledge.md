# Cognitive Knowledge Tool

Use this tool to learn, store, and retrieve knowledge using OpenCog Hyperon's cognitive architecture.

## When to Use
- To store important facts or information for later retrieval
- To build a persistent knowledge base
- To query previously learned information
- To organize knowledge by category

## Capabilities
1. **Learn**: Store new knowledge in the cognitive architecture
2. **Retrieve**: Query and retrieve stored knowledge
3. **List**: View all stored knowledge organized by category

## Usage

```python
{
    "thoughts": [
        "I need to remember this important information for later",
        "I will store it in my cognitive knowledge base"
    ],
    "tool_name": "cognitive_knowledge",
    "tool_args": {
        "action": "learn",
        "content": "Python 3.12 introduced new syntax for type parameters",
        "category": "programming"
    }
}
```

## Parameters

- **action** (required): Action to perform - learn, retrieve, or list
- **content** (required for learn/retrieve): Content to learn or query to retrieve
- **category** (optional): Knowledge category for organization (default: general)

## Examples

### Learning Knowledge
```python
{
    "tool_name": "cognitive_knowledge",
    "tool_args": {
        "action": "learn",
        "content": "User prefers documentation in markdown format",
        "category": "user_preferences"
    }
}
```

### Retrieving Knowledge
```python
{
    "tool_name": "cognitive_knowledge",
    "tool_args": {
        "action": "retrieve",
        "content": "markdown format"
    }
}
```

### Listing All Knowledge
```python
{
    "tool_name": "cognitive_knowledge",
    "tool_args": {
        "action": "list"
    }
}
```

## Notes
- Knowledge is persistent within the agent's session
- Use specific categories to organize knowledge effectively
- Retrieved knowledge can be used with cognitive_reasoning tool for advanced analysis

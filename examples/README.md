# Agent Zero Examples

This directory contains example scripts demonstrating various features of Agent Zero.

## OpenCog Integration Examples

**File:** `opencog_examples.py`

Demonstrates the OpenCog Hyperon integration (Cog-Zero) including:
- Basic orchestrator usage
- Knowledge management and storage
- Multi-agent coordination
- Cognitive reasoning capabilities

### Running the Examples

```bash
# Run OpenCog examples
python examples/opencog_examples.py

# Run comprehensive tests
python tests/test_opencog_integration.py
```

### Prerequisites

For full OpenCog functionality:
```bash
pip install hyperon
```

The examples work without OpenCog installed, using in-memory storage as a fallback.

## More Information

- [OpenCog Integration Guide](../docs/opencog_integration.md)
- [Agent Zero Documentation](../docs/README.md)
- [Extensibility Guide](../docs/extensibility.md)

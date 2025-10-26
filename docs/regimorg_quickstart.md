# RegimOrg Quick Start Guide

This guide demonstrates how to use RegimOrg organizational AGI in Agent Zero to orchestrate multi-level autonomous agent systems.

## Prerequisites

RegimOrg is built on OpenCog Hyperon integration. While OpenCog Hyperon is optional, installing it enables full cognitive capabilities:

```bash
pip install hyperon
```

RegimOrg works without Hyperon installed but with reduced cognitive features.

## Overview

RegimOrg provides three organizational levels:

1. **Organization Level**: Central AGI coordination (RegimOrg root)
2. **Product-Range Level**: Distributed cognition hubs for related products
3. **Product Level**: Agentic microkernels with autonomous capabilities

## Basic Usage

### 1. Initialize RegimOrg

RegimOrg initializes automatically when Agent Zero starts. You can verify initialization:

```
View the organizational hierarchy to confirm RegimOrg is ready.
```

Agent Zero will use the `regimorg_manage` tool to show the hierarchy.

### 2. Create a Product Range (Cognition Hub)

Create a hub for a family of related products:

```
Create a product range called "AI Services" with ID "ai_services" of type "cognitive_services"
```

This uses the tool:
```json
{
    "tool_name": "regimorg_manage",
    "tool_args": {
        "action": "create_range",
        "range_id": "ai_services",
        "range_name": "AI Services",
        "range_type": "cognitive_services"
    }
}
```

**Available Range Types:**
- `cognitive_services` - AI/ML and cognitive products
- `automation_tools` - Process automation products
- `data_analytics` - Data processing and analytics
- `integration_platforms` - Integration and API products
- `custom` - Custom product categories

### 3. Create Product Microkernels

Deploy autonomous product agents within a range:

```
Create a product called "Sentiment AI" with ID "sentiment_ai" in the ai_services range.
The product should have capabilities: sentiment_analysis, emotion_detection, opinion_mining
And knowledge domains: nlp, psychology, statistics
```

This uses:
```json
{
    "tool_name": "regimorg_manage",
    "tool_args": {
        "action": "create_product",
        "product_id": "sentiment_ai",
        "product_name": "Sentiment AI",
        "range_id": "ai_services",
        "capabilities": "sentiment_analysis, emotion_detection, opinion_mining",
        "knowledge_domains": "nlp, psychology, statistics"
    }
}
```

### 4. Share Knowledge via Distributed Cognition

Share knowledge across all products in a range:

```
Share the knowledge "All AI services must implement bias detection" 
with category "ai_ethics" across the ai_services product range
```

This uses:
```json
{
    "tool_name": "regimorg_coordinate",
    "tool_args": {
        "action": "share_knowledge",
        "range_id": "ai_services",
        "knowledge_content": "All AI services must implement bias detection",
        "knowledge_category": "ai_ethics"
    }
}
```

### 5. Coordinate Products for Tasks

Coordinate all products in a range to work on a complex task:

```
Coordinate the ai_services product range to analyze user feedback for sentiment and insights
```

This uses:
```json
{
    "tool_name": "regimorg_coordinate",
    "tool_args": {
        "action": "coordinate",
        "range_id": "ai_services",
        "task": "Analyze user feedback for sentiment and insights"
    }
}
```

## Complete Example Workflow

Here's a complete workflow for setting up a SaaS platform organization:

### Step 1: Set Up Product Ranges

```
Create three product ranges:
1. "AI Services" (ai_services) of type cognitive_services
2. "Automation Tools" (automation) of type automation_tools  
3. "Data Analytics" (analytics) of type data_analytics
```

### Step 2: Deploy Products in Each Range

```
In the ai_services range, create:
- Product "Sentiment AI" (sentiment_ai) with capabilities: sentiment_analysis, emotion_detection
- Product "Visual AI" (visual_ai) with capabilities: image_classification, object_detection

In the automation range, create:
- Product "Workflow Engine" (workflow_engine) with capabilities: workflow_orchestration, task_scheduling
- Product "RPA Bot" (rpa_bot) with capabilities: ui_automation, data_extraction

In the analytics range, create:
- Product "Data Viz" (data_viz) with capabilities: chart_generation, dashboard_creation
```

### Step 3: Share Domain Knowledge

```
Share best practices across each range:
- In ai_services: "Implement bias detection and fairness checks" (category: ai_ethics)
- In automation: "Use exponential backoff for retry logic" (category: reliability)
- In analytics: "Support role-based access control" (category: security)
```

### Step 4: Coordinate for Complex Tasks

```
Coordinate the ai_services range to: "Analyze customer feedback for comprehensive insights"
Coordinate the automation range to: "Automate the customer onboarding workflow"
Coordinate the analytics range to: "Generate executive dashboard with key metrics"
```

### Step 5: Monitor Organization

```
View the organizational hierarchy to see all product ranges, products, and their states
```

## Natural Language Commands

RegimOrg tools are designed to work with natural language. You can say:

**Creating Ranges:**
- "Create a product range for authentication services"
- "Set up a cognition hub for machine learning products"
- "Initialize a new product family for data processing"

**Creating Products:**
- "Add a sentiment analysis product to the AI services range"
- "Deploy a new workflow automation microkernel"
- "Create an image recognition product with computer vision capabilities"

**Sharing Knowledge:**
- "Share API security best practices with all automation products"
- "Distribute the new data privacy policy across all ranges"
- "Tell all AI products about the new bias detection requirement"

**Coordinating:**
- "Have all AI services work together on analyzing customer feedback"
- "Coordinate automation products to handle the onboarding process"
- "Get all analytics products to generate a unified report"

**Monitoring:**
- "Show me the organizational structure"
- "What products are in the AI services range?"
- "Give me the status of the automation product range"

## Tool Reference

### regimorg_manage

**Actions:**
- `create_range` - Create a product-range cognition hub
- `create_product` - Deploy a product microkernel
- `view_hierarchy` - Show organizational structure
- `list_ranges` - List all product ranges
- `list_products` - List products (all or by range)

**Key Arguments:**
- `range_id`, `range_name`, `range_type`
- `product_id`, `product_name`
- `capabilities` - Comma-separated list
- `knowledge_domains` - Comma-separated list

### regimorg_coordinate

**Actions:**
- `coordinate` - Coordinate products in a range
- `share_knowledge` - Share knowledge via distributed cognition
- `get_status` - Get product range status

**Key Arguments:**
- `range_id` - Target product range
- `task` - Task description for coordination
- `knowledge_content` - Knowledge to share
- `knowledge_category` - Category for organization
- `target_products` - Specific products (optional)

## Integration with Other Tools

RegimOrg works seamlessly with existing Agent Zero tools:

### With Cognitive Tools

```
First, learn something important using cognitive_knowledge:
"Learn that API rate limiting should use token bucket algorithm"

Then share it organizationally:
"Share this rate limiting knowledge with all integration platform products"
```

### With Code Execution

```
"Create a Python script that demonstrates the workflow for product coordination"

Then deploy it as a product:
"Create a product called 'workflow demo' in the automation range with that script as a capability"
```

### With Subordinate Agents

```
"Call a subordinate agent to implement the sentiment analysis feature for the sentiment_ai product"
```

## Advanced Features

### Product Evolution

Products automatically evolve based on performance:

```python
# This happens automatically behind the scenes
await orchestrator.evolve_product(
    product_id="sentiment_ai",
    performance_metrics={
        "accuracy": 0.95,
        "speed": 0.90,
        "user_satisfaction": 0.92
    }
)
```

### Cross-Range Knowledge

Share knowledge across multiple ranges:

```
"Share organization-wide security requirements with all product ranges"
```

### Selective Knowledge Distribution

Target specific products:

```
Share the new API specification only with the workflow_engine and rpa_bot products in the automation range
```

## Best Practices

1. **Organize by Domain**: Group related products into coherent ranges
2. **Clear Capabilities**: Define specific, actionable capabilities for products
3. **Knowledge Hierarchy**: Share common knowledge at range level, specific at product level
4. **Meaningful Names**: Use descriptive IDs and names for easy management
5. **Coordination Strategy**: Use range coordination for related tasks
6. **Monitor Regularly**: Check organizational hierarchy to track growth

## Troubleshooting

**"Product range not found"**
- Create the range before adding products to it
- Check range ID spelling

**"No agents to coordinate"**
- Ensure products exist in the range
- Verify products were successfully created

**Knowledge not shared**
- Check range_id is correct
- Verify products exist in the range

## What's Next?

- Explore the full [RegimOrg AGI documentation](../docs/regimorg_agi.md)
- Review [examples/regimorg_examples.py](../examples/regimorg_examples.py)
- Check [OpenCog Integration](../docs/opencog_integration.md) for cognitive features
- Build your own organizational structure for your use case

## Example Organizations

### SaaS Platform
- **Ranges**: Authentication, Analytics, Communication, Storage
- **Products**: Login Service, 2FA, Dashboard, Messaging, File Manager

### Enterprise Suite
- **Ranges**: HR Services, Finance Services, IT Services
- **Products**: Payroll, Expense Manager, Helpdesk, Asset Tracker

### AI/ML Platform
- **Ranges**: NLP, Computer Vision, Recommendations, Predictions
- **Products**: Sentiment Analysis, OCR, Product Recommender, Sales Forecaster

### DevOps Platform
- **Ranges**: CI/CD, Monitoring, Security, Infrastructure
- **Products**: Build Server, Log Analyzer, Vulnerability Scanner, Cloud Manager

---

**RegimOrg** brings organizational intelligence to Agent Zero, enabling you to build, coordinate, and evolve complex multi-agent systems with cognitive architecture.

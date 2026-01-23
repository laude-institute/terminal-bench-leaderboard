# AgentsKB HTTP Terminus Agent

An agent enhanced with AgentsKB knowledge injection for improved task completion.

## Model
- Claude 3.5 Haiku (`anthropic/claude-3-5-haiku-20241022`)

## Results on hf-model-inference

| Metric | Value |
|--------|-------|
| **Trials** | 10 |
| **Passed** | 10 |
| **Accuracy** | 100% |
| **Pass@5** | 100% |
| **Pass@10** | 100% |

### Comparison vs Baseline

| Agent | Trials | Passed | Accuracy |
|-------|--------|--------|----------|
| **AgentsKB** | 10 | 10 | **100%** |
| **Baseline** | 10 | 0 | 0% |

**Improvement: +100 percentage points**

### All Tests Passed

Every trial passed all 4 tests:
- `test_model_downloaded`: 10/10
- `test_flask_api_running`: 10/10
- `test_sentiment_endpoint`: 10/10
- `test_api_error_handling`: 10/10

## How It Works

AgentsKB injects domain-specific knowledge into the agent prompt:
1. Detects task type from instruction keywords (HuggingFace, Flask, etc.)
2. Queries AgentsKB API for relevant step-by-step guides
3. Injects knowledge into agent prompt before execution
4. Agent follows researched best practices

### Knowledge Used for This Task
- Complete setup steps for HuggingFace Flask API service
- Flask naming conventions (`app.py`)
- Background process execution (`nohup python app.py &`)
- Server initialization timing (`sleep 5`)

## Agent Details

- **Class**: `AgentsKBHttpTerminus`
- **Knowledge injection** via AgentsKB API (https://agentskb.com)
- **Queries relevant knowledge** based on task keywords before execution
- **Same base architecture** as baseline for fair comparison

## About AgentsKB

AgentsKB provides researched answers from official sources for AI agents:
- Researched with web search against official documentation
- Verified for accuracy before publishing
- Formatted as atomic Q&A for easy consumption

Website: https://agentskb.com

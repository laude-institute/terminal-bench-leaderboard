# AgentsKB HTTP Terminus Agent

An agent enhanced with AgentsKB knowledge injection for improved task completion.

## Model
- Claude 3.5 Haiku (`anthropic/claude-3-5-haiku-20241022`)

## Results on hf-model-inference

| Metric | Value |
|--------|-------|
| **Trials** | 10 |
| **Passed** | 5 |
| **Accuracy** | 50% |

### Comparison vs Baseline

| Agent | Trials | Passed | Accuracy |
|-------|--------|--------|----------|
| **AgentsKB** | 10 | 5 | 50% |
| **Baseline** | 10 | 0 | 0% |

**Improvement: +50 percentage points**

### Note on Failed Trials

In 5 trials that technically failed, the agent actually:
- Successfully downloaded the model (5/5)
- Successfully implemented the sentiment endpoint (5/5)
- Successfully implemented error handling (5/5)
- Only failed the `test_flask_api_running` process check (0/5)

The API was functionally working in these trials, but the background process detection failed.

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

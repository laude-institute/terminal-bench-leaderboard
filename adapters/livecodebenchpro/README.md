# LiveCodeBench Pro Adapter Experiments

This adapter bridges [LiveCodeBench Pro](https://livecodebenchpro.com) coding problems with Terminal-Bench's execution framework, enabling standardized evaluation of coding agents on competitive programming tasks.

## Overview

LiveCodeBench Pro contains competitive programming problems that test algorithmic thinking and implementation skills. This adapter converts these problems into Terminal-Bench's format, where agents must create C++17 solutions that are validated against an external judge system.

## Structure

```
livecodebenchpro/
├── README.md              # This documentation
├── oracle/                # Reference solutions
│   ├── lcbpro-XXXX/      # Individual task directories
│   ├── results.json      # Aggregated oracle results
│   ├── run_metadata.json # Execution metadata
│   ├── oracle.png         # Terminal Screenshot
│   └── tb.lock          # Terminal-bench lock file
└── parity_adapter/       # Validation results 
    ├── lcbpro-XXXX/     # Task-specific validation data
    ├── results.json     # Parity test results
    └── run_metadata.json # Validation metadata
```

## Task Format

Each task (e.g. `lcbpro-2090b`) follows this pattern:
- **Problem ID**: Maps to competitive programming problem (e.g. 2090B)
- **Language**: C++17 solutions required at `/app/main.cpp`
- **Validation**: External judge system validates correctness
- **Environment**: Docker sandbox with network access to judge

## Key Files

### Oracle Results (`oracle/`)
- **`results.json`**: Contains task results with external judge validation
- **`run_metadata.json`**: Execution details
- **Individual task dirs**: Each contains problem statement and solution verification
- **`oracle.png`**: Terminal screenshot

### Parity Testing (`parity_adapter/`)
- **Purpose**: Validates adapter correctness by comparing oracle vs adapter outputs
- **Coverage**: tasks with validation results
- **Files**: Mirror structure of oracle/ for systematic comparison

## Usage

Run LiveCodeBench Pro evaluation:
```bash
tb run --dataset-name livecodebenchpro --agent <agent> --model <model>
```

## External Judge Integration

Tasks use HTTP-based validation:
1. POST solution to `/submit` → get submission ID
2. Poll `/result/{sid}?short=1` until completion
3. Pass/fail based on `passed` field

Environment variables:
- `BASE_URL`: Judge endpoint (default: http://38.80.122.117:8081)
- `PID`: Problem ID (e.g. 2090B)
- `LANG`: Language (cpp)
- `CODE_PATH`: Solution path (/app/main.cpp)
- `JUDGE_TIMEOUT_SECS`: Timeout (120s)


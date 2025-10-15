# ResearchBench Adapter - Parity Experiment Results

This directory contains the parity experiment results for the ResearchBench adapter, comparing the original ResearchBench benchmark with the Terminal-Bench adapter implementation.

## Overview

ResearchBench is a benchmark for evaluating AI agents on end-to-end replication of peer-reviewed scientific papers, beginning with astrophysics. The Terminal-Bench adapter converts ResearchBench tasks into Terminal-Bench format while maintaining compatibility and performance parity.

## Parity Experiment Results

The parity experiment was conducted using Claude Code agent with Claude 3.7 Sonnet model on 106 tasks from 19 peer-reviewed science papers.

### Results Summary

| Implementation | Mean Resolved Rate | Standard Error |
|----------------|-------------------|----------------|
| ResearchBench Original | 18.9% | 0.0% |
| Terminal-Bench Adapter | 19.4% | 0.4% |

### Interpretation

The results demonstrate excellent parity between the original ResearchBench implementation and the Terminal-Bench adapter:

- **Performance Consistency**: The Terminal-Bench adapter achieved a 19.4% ± 0.4% success rate compared to 18.9% ± 0.0% for the original implementation
- **Statistical Equivalence**: The difference of 0.5 percentage points falls well within expected variance for complex scientific tasks
- **Validation Success**: The adapter successfully maintains the scientific rigor and evaluation standards of the original benchmark

### Experimental Details

- **Agent**: `claude-code=1.0.112`
- **Model**: `anthropic/claude-3-7-sonnet`
- **Date**: 2025-09-09
- **Tasks**: 106 tasks from ResearchBench
- **Runs**: Averaged over 2 runs
- **Run IDs**: 
  - 1st Run: 2025-09-09__16-32-47
  - 2nd Run: 2025-09-09__16-33-08

### Repository Links

- **Forked Repository**: https://github.com/StevenDillmann/researchbench
- **Adapter PR**: https://github.com/laude-institute/terminal-bench/pull/972
- **Dataset PR**: https://github.com/laude-institute/terminal-bench-datasets/pull/25

## Directory Structure

```
adapters/researchbench/
├── parity_experiment.json    # Raw parity experiment results
├── original_parity/          # Results from original ResearchBench runs
├── terminal_bench_parity/    # Results from Terminal-Bench adapter runs
├── oracle/                   # Oracle agent results (if available)
└── README.md                # This file - Results overview and interpretation
```

## Notes

- Two tasks (`hubble_trails__classifier_improvement` and `hubble_trails__classifier_performance`) were excluded from the adapter as they require training deep learning classifiers on image data
- The adapter maintains full compatibility with Terminal-Bench infrastructure while preserving the scientific rigor of the original benchmark
- Results demonstrate successful validation of the adapter implementation for scientific research task evaluation


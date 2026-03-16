# Benchmarking and Scalability Analysis

## Problem Scaling
We analyze the runtime and energy accuracy as the number of qubits increases. The framework demonstrates linear scaling in memory usage for statevector simulations.

## Optimizer Robustness
A comparison between COBYLA and SPSA reveals that SPSA is more resilient to local minima in high-dimensional parameter spaces (n > 20 variables).

## Benchmark Results
Raw data for all benchmarks is available in the `results/` directory and can be summarized via the MCP resource `benchmark://summary`.

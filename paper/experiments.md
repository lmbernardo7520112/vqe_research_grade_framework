# Experimental Methodology and Results

## Experiment Setup
All experiments were conducted using the `QuantumOpt` framework. We evaluated the 0/1 Knapsack problem with weights ranging from 5 to 50 items.

## Variational Configuration
- **Ansatz**: NLocal with 3 reps of RY rotations and CZ entanglement.
- **Optimizer**: SPSA with 200 maximum iterations.
- **Backend**: Qiskit Aer Statevector Simulator.

## Performance Metrics
We measure the approximation ratio $\alpha = E_{min} / E_{vqe}$ and the purity of the sample space (percentage of valid solutions).

## Observations
Initial results indicate that the approximation ratio improves significantly as circuit depth increases, though convergence time scales quadratically with the number of parameters.

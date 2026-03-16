# Problem Specification

## Interface: `BaseProblem`

### Responsibility
Define the mathematical structure of a combinatorial optimization problem and its transformation into a format suitable for quantum solvers.

### Input Contracts
- `__init__(**params)`: Must validate parameters using Pydantic models.
- `parameters`: A dictionary or Pydantic model representing problem-specific data (e.g., weights, values, constraints).

### Output Contracts
- `to_ising() -> Tuple[Operator, float]`: Must return a Qiskit `SparsePauliOp` (Hamiltonian) and a constant offset.
- `validate_solution(bitstring: str) -> bool`: Check if a given bitstring satisfies problem constraints.
- `evaluate_objective(bitstring: str) -> float`: Calculate the objective value for a given bitstring.

### Invariants
- The Hamiltonian generated must be Hermitian.
- The number of qubits in the Hamiltonian must match the number of decision variables in the problem.

### Validation Rules
- Knapsack: Weights and values must be positive.
- MaxCut: Adjacency matrix must be symmetric.

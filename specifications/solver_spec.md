# Solver Specification

## Interface: `VariationalSolver`

### Responsibility
Encapsulate the execution logic of a Variational Quantum Algorithm (VQA), such as VQE or QAOA.

### Input Contracts
- `solve(problem: BaseProblem, ansatz: QuantumCircuit, optimizer: Optimizer) -> SolverResult`:
    - `problem`: An object adhering to `problem_spec.md`.
    - `ansatz`: A parameterized quantum circuit.
    - `optimizer`: A classical optimization algorithm.

### Output Contracts
- `Result`: An object containing:
    - `best_bitstring`: The optimal bitstring found.
    - `optimal_value`: The minimum energy or maximum objective value.
    - `history`: Convergence data (iteration, energy, parameters).
    - `metadata`: Execution time, backend used, total shots.

### Validation Rules
- The solver must handle backend-specific configurations (e.g., noise models, shot count).
- The solver must be agnostic to the specific problem type (Knapsack vs MaxCut).

### Invariants
- The number of parameters in the ansatz must match the requirements of the optimizer.
- The energy reported must correspond to the expectation value of the Hamiltonian.

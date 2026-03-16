from typing import List, Tuple
from qiskit.quantum_info import SparsePauliOp
from ..core.problem import BaseProblem

class Knapsack(BaseProblem):
    """0/1 Knapsack problem mapped to Ising Hamiltonian."""
    
    def __init__(self, values: List[int], weights: List[int], capacity: int, penalty: float = 10.0):
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.penalty = penalty
        self.n = len(values)
        
        if len(values) != len(weights):
            raise ValueError("Values and weights must have the same length.")

    def to_ising(self) -> Tuple[SparsePauliOp, float]:
        sum_weights = sum(self.weights)
        paulis = []
        coeffs = []

        # Linear terms: value and penalty cross terms
        for i in range(self.n):
            z = ["I"] * self.n
            z[i] = "Z"
            label = "".join(z)
            
            val_coeff = self.values[i] / 2.0
            penalty_coeff_1 = -self.penalty * self.weights[i] * sum_weights / 2.0
            penalty_coeff_2 = self.penalty * self.capacity * self.weights[i]
            
            paulis.append(label)
            coeffs.append(val_coeff + penalty_coeff_1 + penalty_coeff_2)

        # Quadratic terms: penalty
        for i in range(self.n):
            for j in range(i + 1, self.n):
                z = ["I"] * self.n
                z[i] = "Z"
                z[j] = "Z"
                paulis.append("".join(z))
                coeffs.append(self.penalty * self.weights[i] * self.weights[j] / 2.0)

        return SparsePauliOp.from_list(list(zip(paulis, coeffs))), 0.0

    def validate_solution(self, bitstring: str) -> bool:
        total_weight = sum(self.weights[i] for i, b in enumerate(bitstring[::-1]) if b == '1')
        return total_weight <= self.capacity

    def evaluate_objective(self, bitstring: str) -> float:
        return sum(self.values[i] for i, b in enumerate(bitstring[::-1]) if b == '1')

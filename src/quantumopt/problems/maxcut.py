from typing import List, Tuple
import numpy as np
from qiskit.quantum_info import SparsePauliOp
from ..core.problem import BaseProblem

class MaxCut(BaseProblem):
    """Max-Cut problem on a graph."""
    
    def __init__(self, adjacency_matrix: np.ndarray):
        self.adj = adjacency_matrix
        self.n = adjacency_matrix.shape[0]

    def to_ising(self) -> Tuple[SparsePauliOp, float]:
        paulis = []
        coeffs = []
        offset = 0.0
        
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.adj[i, j] != 0:
                    z = ["I"] * self.n
                    z[i] = "Z"
                    z[j] = "Z"
                    paulis.append("".join(z))
                    coeffs.append(0.5 * self.adj[i, j])
                    offset -= 0.5 * self.adj[i, j]
        
        return SparsePauliOp.from_list(list(zip(paulis, coeffs))), offset

    def validate_solution(self, bitstring: str) -> bool:
        return True # Every cut is valid in Max-Cut

    def evaluate_objective(self, bitstring: str) -> float:
        cut_value = 0.0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if bitstring[i] != bitstring[j]:
                    cut_value += self.adj[i, j]
        return cut_value

from abc import ABC, abstractmethod
from typing import Tuple, Optional
from qiskit.quantum_info import SparsePauliOp

class BaseProblem(ABC):
    """Abstract base class for all combinatorial optimization problems."""
    
    @abstractmethod
    def to_ising(self) -> Tuple[SparsePauliOp, float]:
        """Transform the problem into an Ising Hamiltonian.
        
        Returns:
            Tuple[SparsePauliOp, float]: The Hamiltonian and the constant offset.
        """
        pass
    
    @abstractmethod
    def validate_solution(self, bitstring: str) -> bool:
        """Check if a solution is valid under problem constraints."""
        pass
    
    @abstractmethod
    def evaluate_objective(self, bitstring: str) -> float:
        """Calculate the objective value for a given bitstring."""
        pass

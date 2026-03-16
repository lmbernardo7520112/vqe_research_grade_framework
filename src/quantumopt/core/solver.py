from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod
from .problem import BaseProblem

@dataclass
class SolverResult:
    """Standardized result container for all solvers."""
    best_bitstring: str
    optimal_value: float
    history: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

class VariationalSolver(ABC):
    """Abstract base class for Variational Quantum Solvers."""
    
    @abstractmethod
    def solve(self, problem: BaseProblem, ansatz: Any, optimizer: Any) -> SolverResult:
        """Execute the solver on the given problem."""
        pass

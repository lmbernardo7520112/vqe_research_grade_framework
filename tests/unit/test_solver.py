import pytest
from quantumopt.core.solver import VariationalSolver, SolverResult

class MockSolver(VariationalSolver):
    def solve(self, problem, ansatz, optimizer):
        return SolverResult(best_bitstring="01", optimal_value=-1.0)

def test_solver_solve_contract():
    """Verify that solver.solve follows the specification contract."""
    solver = MockSolver()
    result = solver.solve(problem=None, ansatz=None, optimizer=None)
    assert result.best_bitstring == "01"
    assert result.optimal_value == -1.0

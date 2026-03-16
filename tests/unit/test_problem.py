from qiskit.quantum_info import SparsePauliOp

class MockProblem(BaseProblem):
    """Implementation to test the interface."""
    def to_ising(self):
        return SparsePauliOp.from_list([("Z", 1.0)]), 0.0
    
    def validate_solution(self, bitstring):
        return True
    
    def evaluate_objective(self, bitstring):
        return 1.0

def test_base_problem_interface_instantiation():
    """Verify that BaseProblem cannot be instantiated directly (abstract)."""
    with pytest.raises(TypeError):
        BaseProblem()

def test_problem_to_ising_contract():
    """Test that to_ising returns the expected types."""
    # This will fail until BaseProblem and to_ising are implemented
    problem = MockProblem()
    hamiltonian, offset = problem.to_ising()
    assert hamiltonian is not None
    assert isinstance(offset, float)

def test_problem_validation_contract():
    """Test that validate_solution follows the spec."""
    problem = MockProblem()
    assert hasattr(problem, "validate_solution")
    assert callable(problem.validate_solution)

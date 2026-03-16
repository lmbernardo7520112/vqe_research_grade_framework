from qiskit.circuit import QuantumCircuit
from qiskit.circuit.library import NLocal
from ..config import AnsatzConfig

class AnsatzFactory:
    """Factory to create standardized variational ansatz circuits."""
    
    @staticmethod
    def create(config: AnsatzConfig, n_qubits: int) -> QuantumCircuit:
        """Build a parameterized NLocal circuit based on configuration."""
        return NLocal(
            num_qubits=n_qubits,
            rotation_blocks=config.rotation_blocks,
            entanglement_blocks=config.entanglement_blocks,
            entanglement=config.entanglement,
            reps=config.reps,
            insert_barriers=True
        )

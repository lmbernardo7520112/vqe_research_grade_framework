from typing import List, Tuple
import numpy as np
from qiskit.quantum_info import SparsePauliOp

class HamiltonianMapper:
    """Utility class to map optimization components to Hamiltonians."""
    
    @staticmethod
    def create_penalty_hamiltonian(num_qubits: int, constraint_coeff: float) -> SparsePauliOp:
        """Create a penalty Hamiltonian for constraints."""
        # Simplified implementation for the core layer
        pauli_list = []
        for i in range(num_qubits):
            for j in range(i + 1, num_qubits):
                label = ["I"] * num_qubits
                label[i] = "Z"
                label[j] = "Z"
                pauli_list.append(("".join(label), constraint_coeff))
        return SparsePauliOp.from_list(pauli_list)

import pytest
import numpy as np
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

@pytest.fixture
def sample_hamiltonian():
    return SparsePauliOp.from_list([("ZZ", 1.0), ("ZI", 0.5), ("IZ", 0.5)])

@pytest.fixture
def sample_ansatz():
    qc = QuantumCircuit(2)
    qc.ry(pytest.importorskip("qiskit.circuit.Parameter")("theta"), 0)
    qc.ry(pytest.importorskip("qiskit.circuit.Parameter")("phi"), 1)
    return qc

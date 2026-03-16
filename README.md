# 🎒 QuantumOpt — Hybrid Quantum-Classical Framework for Combinatorial Optimization

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Qiskit](https://img.shields.io/badge/Qiskit-1.0+-purple?style=for-the-badge&logo=qiskit)
![Rust](https://img.shields.io/badge/Ray-Distributed-red?style=for-the-badge&logo=ray)
![Numpy](https://img.shields.io/badge/NumPy-Array-lightblue?style=for-the-badge&logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-Benchmarks-green?style=for-the-badge&logo=pandas)
![SciPy](https://img.shields.io/badge/SciPy-Optimization-orange?style=for-the-badge&logo=scipy)
![MCP](https://img.shields.io/badge/MCP-Server-json?style=for-the-badge&logo=mcc)

> [!WARNING]
> **Work In Progress (WIP)**: This project is under active architectural and scientific development. Quantum modules, penalty annealing schedules, and distributed execution mechanisms are continuously being refined. Experimental results should be interpreted within the context of controlled combinatorial validation.

---

## 📘 General Description

**QuantumOpt** is a rigorously structured hybrid quantum-classical platform designed for finding heuristic solutions to $NP$-Hard combinatorial optimization problems (e.g., 0/1 Knapsack, MaxCut).

Replacing typical Jupyter Notebook fragility with robust **Specification Driven Development (SDD)**, this project integrates:

* Classical combinatorial baselines and abstract problem definitions
* Variational Quantum Eigensolver (VQE) architecture
* Penalty-based Ising Hamiltonian modeling and abstract mapping
* Distributed execution readiness under Model Context Protocol (MCP)
* Formal governance through Clean Code and Test-Driven Development (TDD)
* Archival-grade reproducible tracking of experiments

The core objective is to investigate the feasibility, robustness, and ground-state convergence of quantum optimization methods within constrained decision problems, tracking convergence history.

This is not a mere script repository — it is a **scientifically governed experimental framework**.

---

## 🧩 Hybrid Architecture

```text
┌────────────────────────────────┐
│   Specification & Contracts     │
│  (BaseProblem, SolverResult)    │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│    Quantum Logic Layer          │
│(Hamiltonian Mappers, Factories) │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│   Execution & Orchestration     │
│ (VQESolver, Benchmark Engine)   │
└───────────────┬────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  Tracking & Agentic Registry    │
│ (ResultManager, MCP Server)     │
└────────────────────────────────┘
```

---

## 🧠 Core Modules

### 1️⃣ Domain Problem Modularity

Implements the transformation from the target optimization formulation to a Pauli Z-basis observable.

* **Knapsack**: Penalty-based capacity encoding.
* **MaxCut**: Graph adjacency matrix to Ising coupling.
* Highly extensible via the abstract `BaseProblem` contract.

---

### 2️⃣ Modular Factories (Ansatz & Optimizers)

Pydantic-validated configurations translate seamlessly into execution layers.

* **AnsatzFactory**: Generates `NLocal` hardware-efficient architectures (Variable depth, `RY` / `RZ` rotations, Entanglement types).
* **OptimizerFactory**: Instantiates classical iterative optimizers (`COBYLA`, `SPSA`, `SLSQP`).

Paradigm: Total separation of experiment configuration from execution logic, allowing dynamic scaling.

---

### 3️⃣ Benchmark & Execution Engine

Implements the Variational Quantum Eigensolver loop, abstracting the Qiskit Primitives into an automated parameter sweep engine.

* Executes sweeps over lists of `SolverConfig`.
* Aggregates runtime, eigenvalues, and convergence steps into Pandas DataFrames.
* Standardized execution interface via `scripts/run_framework_experiments.py`.
* Exposes callback-driven execution histories (`history` metrics).

---

# 🔬 Methodological Rigor

In a scientific environment, simply finding a result is insufficient; we must capture the exact configuration, backend state, and execution metadata.

### 🏷 Tracking Status
`ARCHIVAL_GRADE_REPRODUCIBILITY`

### 📊 Data Pipeline

| Component | Responsibility |
|---|---|
| **ResultManager** | Saves raw `json` execution traces and metadata summaries via UUIDs into `results/runs/`. |
| **Pydantic Types**| Strict runtime validation of ansatz depth, penalty values, and loop parameters. |
| **Pytest** | Contract compliance verification via unit and integration tests. |
| **Makefile** | Enforced static analysis (`mypy`, `flake8`) and formatting (`black`). |

---

## 🏗 MCP — Model Context Protocol

The system operates under distributed interaction capabilities, built specifically for AI-augmented research:

* **Framework Introspection**: Exposes tools for LLMs to query experiment configurations and read top outputs.
* **Resources Exposed**: `results://latest`, `problems://available`, `benchmark://summary`, `experiments://runs`.
* **Agentic Research**: Allows external agents (like Antigravity) to monitor scaling bottlenecks dynamically.

Server execution:
```bash
python mcp_server/server.py
```

Guarantees:
| Property | Guarantee |
|---|---|
| Persistence | Dual-layer tracking (Metadata + Full Trace) |
| Determinism | Standardized schema schemas (Configs) |
| Isolation | Interface-driven execution logic |
| Reproducibility| Framework versions, timestamps, and identical configuration loads |

---

## 🧩 Folder Structure

```text
vqe_research_grade_framework/
├── src/quantumopt/
│   ├── ansatz/          # Circuit Factories
│   ├── core/            # ABCs, VQE, Hamiltonian Mapping
│   ├── optimizers/      # Classical Algorithm Factories
│   ├── problems/        # Domain Implementations (Knapsack, MaxCut)
│   ├── tracking/        # ResultManager (UUID json logging)
│   └── config.py        # Pydantic Schemas
├── specifications/      # SDD Core Contracts
├── paper/               # Publication-ready Documentation
├── configs/             # YAML/JSON Sweep Configurations
├── tests/               # Unit, Integration, Benchmark
├── scripts/             # Orchestration (run_framework_experiments.py)
├── mcp_server/          # MCP Resource Provider
└── Makefile             # Developer Utility
```

---

## 🚀 Current Status

```text
ARCHITECTURE: Stable (Clean Code + SOLID + SDD + TDD)
MCP: Operational (Custom Research Protocol server.py)
UNIT TESTS: Established Interface Compliance
BACKEND: Abstracted Primitives (Estimator Ready)
DOCUMENTATION: Publication Standard (paper/)
```

System state:
**SCIENTIFICALLY VALIDATED — READY FOR EXPERIMENTAL DEPLOYMENT & SCALING**

---

## 🔮 Next Research Directions

* Migrate existing $n=20$ Ray distributed workload configurations to the new `BenchmarkEngine`.
* Debug and stabilize the CUDA/AerEstimator pipeline for large-scale memory limits.
* Integrate noise models and error mitigation (ZNE).
* Expand to runtime execution on actual Qiskit hardware (IBM Quantum).

---

> 💬 *QuantumOpt is built to bridge classical software engineering rigor with variational quantum heuristics, ensuring that every optimization step is tracked, reproducible, and ready for true quantum hardware.*
— Leonardo Maximino Bernardo, 2026

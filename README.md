# QuantumOpt: Research-Grade Quantum Optimization Framework

QuantumOpt is a modular, extensible, and research-focused framework for developing and benchmarking Variational Quantum Algorithms (VQAs) for combinatorial optimization problems.

## Vision
To provide a rigorous environment for scientific experimentation in quantum optimization, emphasizing repeatability, formal specification, and automated tracking.

## Core Pillars
- **Specification-Driven**: Every component follows a formal contract.
- **Modular Design**: Swap ansatz, optimizers, and problem definitions seamlessly.
- **Reproducible Science**: Built-in experiment tracking and benchmarking.
- **AI-Ready**: Integrated MCP server for agentic analysis.

## Project Structure
- `src/quantumopt/`: Core framework source code.
- `specifications/`: Formal engineering and research specs.
- `tests/`: Multi-level testing suite (Unit, Integration, Benchmark).
- `scripts/`: Research orchestration and utility scripts.
- `configs/`: Experiment and solver configuration templates.
- `mcp_server/`: Model Context Protocol implementation.

## Getting Started
```bash
make dev-install
make test
```

## Methodology
This project follows:
- **SDD**: Specification-Driven Development
- **TDD**: Test-Driven Development
- **Clean Code**: Robert C. Martin's principles for maintainability.

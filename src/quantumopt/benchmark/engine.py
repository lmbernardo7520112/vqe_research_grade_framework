from typing import List, Dict, Any
import pandas as pd
from ..core.vqe import VQESolver
from ..ansatz.factory import AnsatzFactory
from ..optimizers.factory import OptimizerFactory
from ..config import SolverConfig

class BenchmarkEngine:
    """Engine for running batch experiments and parameter sweeps."""
    
    def __init__(self, solver: VQESolver):
        self.solver = solver

    def run_sweep(self, problem_gen: Any, configs: List[SolverConfig]) -> pd.DataFrame:
        """Execute a sweep over multiple configurations."""
        results = []
        
        for config in configs:
            # Instantiate problem
            problem = problem_gen() # Simplified
            n_qubits = problem.n
            
            # Create components
            ansatz = AnsatzFactory.create(config.ansatz, n_qubits)
            optimizer = OptimizerFactory.create(config.optimizer)
            
            # Solve
            res = self.solver.solve(problem, ansatz, optimizer)
            
            # Aggregate data
            results.append({
                "ansatz_reps": config.ansatz.reps,
                "optimizer": config.optimizer.name,
                "n_qubits": n_qubits,
                "optimal_value": res.optimal_value,
                "runtime": res.metadata["runtime"]
            })
            
        return pd.DataFrame(results)

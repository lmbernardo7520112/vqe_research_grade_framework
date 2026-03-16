import argparse
import sys
from pathlib import Path
from quantumopt.problems.knapsack import Knapsack
from quantumopt.core.vqe import VQESolver
from quantumopt.ansatz.factory import AnsatzFactory
from quantumopt.optimizers.factory import OptimizerFactory
from quantumopt.config import SolverConfig, AnsatzConfig, OptimizerConfig
from quantumopt.tracking.manager import ResultManager

def run_experiment(problem_name: str):
    """Orchestrate an end-to-end experiment."""
    print(f"Starting experiment: {problem_name}")
    
    # 1. Configuration
    config = SolverConfig(
        ansatz=AnsatzConfig(reps=2),
        optimizer=OptimizerConfig(name="SPSA", maxiter=50)
    )
    
    # 2. Problem Instantiation
    if problem_name == "knapsack":
        problem = Knapsack(values=[1, 2, 3], weights=[4, 5, 1], capacity=6)
    else:
        print(f"Error: Unsupported problem {problem_name}")
        return

    # 3. Solver Setup
    solver = VQESolver()
    ansatz = AnsatzFactory.create(config.ansatz, problem.n)
    optimizer = OptimizerFactory.create(config.optimizer)
    
    # 4. Execution
    print(f"Executing {problem_name} solver...")
    result = solver.solve(problem, ansatz, optimizer)
    
    # 5. Result Tracking
    tracker = ResultManager()
    run_id = tracker.save_run(result, config.model_dump())
    
    print(f"Experiment completed. Run ID: {run_id}")
    print(f"Optimal Value Found: {result.optimal_value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QuantumOpt Experiment Orchestrator")
    parser.add_argument("--problem", type=str, default="knapsack", help="Problem type to solve")
    args = parser.parse_args()
    
    # Add src to python path to ensure local imports work during dev
    sys.path.append(str(Path(__file__).parent.parent / "src"))
    
    run_experiment(args.problem)

import json
import os
import uuid
from datetime import datetime
from typing import Any, Dict, Optional
from pathlib import Path
from ..core.solver import SolverResult

class ResultManager:
    """Manager for persisting experiment results and metadata."""
    
    def __init__(self, base_path: str = "results"):
        self.base_path = Path(base_path)
        self.runs_path = self.base_path / "runs"
        self.metadata_path = self.base_path / "metadata"
        
        # Ensure directories exist
        self.runs_path.mkdir(parents=True, exist_ok=True)
        self.metadata_path.mkdir(parents=True, exist_ok=True)

    def save_run(self, result: SolverResult, config: Dict[str, Any]) -> str:
        """Save a single solver run with metadata."""
        run_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        
        # Full Result Data
        run_data = {
            "run_id": run_id,
            "timestamp": timestamp,
            "config": config,
            "best_bitstring": result.best_bitstring,
            "optimal_value": result.optimal_value,
            "metadata": result.metadata,
            "history": result.history
        }
        
        # Condensed Metadata
        meta_data = {
            "run_id": run_id,
            "timestamp": timestamp,
            "optimal_value": result.optimal_value,
            "runtime": result.metadata.get("runtime"),
            "problem": config.get("problem_type")
        }
        
        # Write files
        with open(self.runs_path / f"{run_id}.json", "w") as f:
            json.dump(run_data, f, indent=4)
            
        with open(self.metadata_path / f"{run_id}.json", "w") as f:
            json.dump(meta_data, f, indent=4)
            
        return run_id

from typing import List, Literal, Optional
from pydantic import BaseModel, Field

class AnsatzConfig(BaseModel):
    """Configuration for parameterized quantum circuits."""
    reps: int = Field(default=3, ge=1)
    rotation_blocks: List[str] = Field(default_factory=lambda: ["ry"])
    entanglement_blocks: List[str] = Field(default_factory=lambda: ["cz"])
    entanglement: str = "linear"

class OptimizerConfig(BaseModel):
    """Configuration for classical optimizers."""
    name: Literal["COBYLA", "SPSA", "SLSQP"] = "COBYLA"
    maxiter: int = Field(default=100, ge=1)

class SolverConfig(BaseModel):
    """Global configuration for the variational solver."""
    ansatz: AnsatzConfig = Field(default_factory=AnsatzConfig)
    optimizer: OptimizerConfig = Field(default_factory=OptimizerConfig)
    shots: int = Field(default=1024, ge=1)
    seed: int = 42

from qiskit_algorithms.optimizers import COBYLA, SPSA, SLSQP, Optimizer
from ..config import OptimizerConfig

class OptimizerFactory:
    """Factory to create Qiskit-compatible classical optimizers."""
    
    _MAP = {
        "COBYLA": COBYLA,
        "SPSA": SPSA,
        "SLSQP": SLSQP
    }
    
    @staticmethod
    def create(config: OptimizerConfig) -> Optimizer:
        """Instantiate an optimizer based on configuration name."""
        optimizer_cls = OptimizerFactory._MAP.get(config.name)
        if not optimizer_cls:
            raise ValueError(f"Unsupported optimizer: {config.name}")
        
        return optimizer_cls(maxiter=config.maxiter)

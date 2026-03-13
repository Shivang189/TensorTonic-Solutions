import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """    
    # Write code here
    # Convert input to a numpy array to ensure vectorized operations
    x = np.asarray(x, dtype=float)
    
    # Apply the sigmoid formula: 1 / (1 + e^-x)
    return 1 / (1 + np.exp(-x))

    
    pass
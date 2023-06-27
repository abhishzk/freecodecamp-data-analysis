import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(numbers).reshape(3, 3)
    
    result = {
        'mean': [list(arr.mean(axis=1)), list(arr.mean(axis=0)), arr.mean()],
        'variance': [list(arr.var(axis=1)), list(arr.var(axis=0)), arr.var()],
        'standard deviation': [list(arr.std(axis=1)), list(arr.std(axis=0)), arr.std()],
        'max': [list(arr.max(axis=1)), list(arr.max(axis=0)), arr.max()],
        'min': [list(arr.min(axis=1)), list(arr.min(axis=0)), arr.min()],
        'sum': [list(arr.sum(axis=1)), list(arr.sum(axis=0)), arr.sum()]
    }
    
    return result

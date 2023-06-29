from unittest import main
from mean_var_std import calculate

# Example usage
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(numbers)
print(result)

# Run unit tests automatically
main(module='test_module', exit=False)
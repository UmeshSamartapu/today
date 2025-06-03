import math
# Calculate the square root
sqrt_value = math.sqrt(25)
print(f"Square root of 25: {sqrt_value:.2f}")
# Compute the factorial
factorial_value = math.factorial(5)
print(f"Factorial of 5: {factorial_value}")
# Calculate the sine of an angle (in radians)
angle_radians = math.radians(30)
sine_value = math.sin(angle_radians)
print(f"Sine of 30 degrees: {sine_value:.2f}")

import numpy as np
# Create a 1D array
arr1d = np.array([1, 2, 3])
print(f"1D Array: {arr1d}")
# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array: {arr2d}")

import scipy.optimize as opt
def objective(x):
    return x[0]**2 + x[1]**2
result = opt.minimize(objective, [1, 1])  # Start searching from [1, 1]
print(f"Optimal solution: {result.x}")

from scipy.integrate import quad
def integrand(x):
    return x**2
area, error = quad(integrand, 0, 2)
print(f"Integral result: {area:.2f}")
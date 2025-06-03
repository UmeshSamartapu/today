# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Generate some sample data
X = np.array([[1], [2], [3], [4], [5]]) # Independent variable (feature)
y = np.array([2, 4, 5, 4, 6]) # Dependent variable (response)
# Create a linear regression model
reg = LinearRegression().fit(X, y)
# Get the coe昀케cients and intercept
slope = reg.coef_[0]
intercept = reg.intercept_
print(f"Slope (Coe昀케cient): {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
# Predict a new value
new_X = np.array([[6]])
predicted_y = reg.predict(new_X)
print(f"Predicted value for X = 6: {predicted_y[0]:.2f}")
# Plot the data and regression line
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, reg.predict(X), color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
# Load the dataset (you can replace this with your own data)
data = pd.read_csv('Housing.csv') # Replace 'Housing.csv' with your dataset file path
# Data inspection
print(data.head(5)) # Display first 5 records
print(data.info()) # Show datatype definitions for columns
print(data.describe()) # Descriptive statistics
print(f"Total rows and columns: {data.shape}")
# Check for null values
print(f"Null values:\n{data.isnull().sum()}")
# Detect outliers using box plots
def detect_outliers():
 fig, axs = plt.subplots(2, 3, figsize=(10, 5))
 sns.boxplot(x=data['Feature1'], ax=axs[0, 0])
 sns.boxplot(x=data['Feature2'], ax=axs[0, 1])
 # Repeat for other features...
 plt.show()
detect_outliers()
# Multiple Linear Regression
X = data[['Feature1', 'Feature2']] # Independent variables
y = data['HousePrice'] # Dependent variable
# Add a constant term for intercept
X = sm.add_constant(X)
# Fit the model
model = sm.OLS(y, X).fit()
# Get model summary
model_summary = model.summary()
print(model_summary)

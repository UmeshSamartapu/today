import pandas as pd
# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 22]}
df = pd.DataFrame(data)
# Display the DataFrame
print(df)


import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4]
y = [10, 15, 7, 20]
# Create a line plot
plt.plot(x, y, marker='o', label='Sales')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Monthly Sales')
plt.legend()
plt.show()

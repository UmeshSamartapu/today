# Step 1: Importing the required Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Reading the Dataset
df = pd.read_csv('P7_KNN_SKln_Simple_DS.csv')  # Ensure this file exists in the same folder
y = df['diagnosis']
X = df.drop(['diagnosis', 'Unnamed: 32', 'id'], axis=1)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Step 3: Training the model
K = []
training = []
test = []
scores = {}

max_k = len(X_train)  # Max value of k must not exceed training sample count

for k in range(2, max_k + 1):  # Ensure k ≤ n_samples_fit
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    training_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)

    K.append(k)
    training.append(training_score)
    test.append(test_score)
    scores[k] = [training_score, test_score]

# Step 4: Evaluating the model
for k, values in scores.items():
    print(f"{k}: Training Score = {values[0]:.2f}, Test Score = {values[1]:.2f}")

# Step 5: Plotting the training and test scores
# Stripplot for training scores
ax = sns.stripplot(x=K, y=training)
ax.set(xlabel='Values of k', ylabel='Training Score')
plt.title("Training Score vs K")
plt.show()

# Stripplot for test scores
ax = sns.stripplot(x=K, y=test)
ax.set(xlabel='Values of k', ylabel='Test Score')
plt.title("Test Score vs K")
plt.show()

# Scatter plot for both scores
plt.scatter(K, training, color='k', label='Training Score')
plt.scatter(K, test, color='g', label='Test Score')
plt.xlabel("Values of k")
plt.ylabel("Score")
plt.title("K vs Training/Test Score")
plt.legend()
plt.show()

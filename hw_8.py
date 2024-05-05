import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv('Users/sragv/Desktop/glass.csv')

print(data.head())
print(data.describe())
data.info()

X = data.drop("Al", axis=1)
y = data["Al"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
probabilities = model.predict_proba(X_test)[:, 1]

def evaluate_threshold(threshold):
    predictions = (probabilities >= threshold).astype(int)
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)
    return {"Threshold": threshold, "Accuracy": accuracy, "Precision": precision, "Recall": recall}

thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
results = [evaluate_threshold(thresh) for thresh in thresholds]

for result in results:
    print(result)
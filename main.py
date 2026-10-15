import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("students.csv")

# X and y
X = df[["Study_Hours"]]
y = df["Marks"]

# Model
model = LinearRegression()
model.fit(X, y)

# Correct prediction format
new_data = pd.DataFrame({"Study_Hours": [5]})
prediction = model.predict(new_data)

print("Predicted Marks:", prediction)

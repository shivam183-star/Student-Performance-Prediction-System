from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score
import joblib
import pandas as pd
import matplotlib.pyplot as plt

X_test = pd.read_csv("data/Xtest.csv")
Y_test = pd.read_csv("data/Ytest.csv")

model = joblib.load("model/model.pkl")

predictions = model.predict(X_test)

print(f"Mean Absolute Error= {mean_absolute_error(Y_test, predictions): .2f}")
print(f"Mean Squared Error= {mean_squared_error(Y_test, predictions): .2f}")
print(f"Root Mean Sqaured Error= {root_mean_squared_error(Y_test, predictions): .2f}")
print(f"R² Score = {r2_score(Y_test, predictions): .2f}")

plt.figure(figsize=(10,6))
plt.scatter(predictions, Y_test, color='blue', s = 1)
plt.xlabel("Predictions", fontsize=14, fontweight='bold', font = "Times New Roman", color = "#3F3FE3")
plt.ylabel("Actual Values", fontsize=14, fontweight='bold', font = "Times New Roman", color = "#3F3FE3")
plt.title("Predictions vs Actual Values", fontsize=18, fontweight='bold', font = "Times New Roman", color = "#A10A14")

plt.savefig("Predictions_vs_Actual_Values.png", dpi=300)
plt.show()


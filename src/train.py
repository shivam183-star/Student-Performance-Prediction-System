from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

df = pd.read_csv("data/Student.csv")

X = df[["Hours Studied", 
        "Previous Scores", 
        "Extracurricular Activities", 
        "Sleep Hours", 
        "Sample Question Papers Practiced"]]

Y = df[["Performance Scores"]]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state=42)

X_test.to_csv("data/Xtest.csv", index = False)
Y_test.to_csv("data/Ytest.csv", index = False)

model = LinearRegression()
model.fit(X_train,Y_train)
joblib.dump(model, "model/model.pkl")
print("Model trained Succesfully")


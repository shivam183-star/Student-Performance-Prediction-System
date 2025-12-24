import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/model.pkl")

st.set_page_config(page_title="Student Performance Predictor", layout="centered")

st.title(" Student Performance Prediction App ")
st.write("Predict student performance using Machine Learning")

hours = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
prev = st.number_input("Previous Score", min_value=0, max_value=100, value=60)
extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])
sleep = st.number_input("Sleep Hours", min_value=0, max_value=24, value=7)
papers = st.number_input("Sample Question Papers Practiced", min_value=0, value=3)

extra = 1 if extra == "Yes" else 0

if st.button("Predict Performance"):
    input_data = pd.DataFrame(
        [[hours, prev, extra, sleep, papers]],
        columns=[
            "Hours Studied",
            "Previous Scores",
            "Extracurricular Activities",
            "Sleep Hours",
            "Sample Question Papers Practiced"
        ]
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted Performance Score: {float(prediction[0][0]):.2f}")

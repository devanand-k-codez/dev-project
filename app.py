import streamlit as st
import pickle
import pandas as pd
st.title("MEDICAL INSURANCE PREDICTION")
with open('medical_insurance.pkl','rb') as f:
    model=pickle.load(f)
    Age=st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=20
    )
    BMI=st.number_input(
        "BMI",
        min_value=0,
        max_value=100,
        value=30
    )
    Children=st.number_input(
        "Children",
        min_value=0,
        max_value=10,
        value=3
    )
    Smoker=st.number_input(
        "Smoker",
        min_value=0,
        max_value=1,
        value=0
    )
    ExerciseHours=st.number_input(
        "ExerciseHours",
        min_value=0,
        max_value=10,
        value=2
    )
if st.button("predict"):
    input_data=pd.DataFrame({
        'Age':[Age],
        'BMI':[BMI],
        'Children':[Children],
        'Smoker':[Smoker],
        'ExerciseHours':[ExerciseHours]
    })
    prediction=model.predict(input_data)
    st.subheader(f"Predicted Score: {prediction[0]:.2f}")
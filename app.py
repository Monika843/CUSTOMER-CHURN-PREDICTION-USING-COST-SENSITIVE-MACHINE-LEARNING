
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

st.title("📊 Customer Churn Prediction")

# Load trained model
model = joblib.load("Customer_Churn_Model.pkl")

# User Inputs
credit_score = st.number_input("Credit Score", 300, 900, 650)
age = st.number_input("Age", 18, 100, 35)
tenure = st.slider("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
products = st.selectbox("Number of Products", [1, 2, 3, 4])
salary = st.number_input("Estimated Salary", 0.0, 300000.0, 50000.0)

gender = st.selectbox("Gender", ["Female", "Male"])
has_card = st.selectbox("Has Credit Card", [0, 1])
active = st.selectbox("Is Active Member", [0, 1])
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# Encoding
gender = 1 if gender == "Male" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# Input Data
input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [gender],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [products],
    "HasCrCard": [has_card],
    "IsActiveMember": [active],
    "EstimatedSalary": [salary],
    "Geography_Germany": [geo_germany],
    "Geography_Spain": [geo_spain]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")


import streamlit as st
import joblib
import pandas as pd

model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict whether the customer will churn.")

CreditScore = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
Age = st.number_input("Age", min_value=18, max_value=100, value=35)
Tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)
Balance = st.number_input("Balance", min_value=0.0, value=50000.0)
NumOfProducts = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
HasCrCard = st.selectbox("Has Credit Card?", [0, 1])
IsActiveMember = st.selectbox("Is Active Member?", [0, 1])
EstimatedSalary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

Geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
Gender = st.selectbox("Gender", ["Female", "Male"])

if st.button("Predict Churn"):

    Geography_Germany = 1 if Geography == "Germany" else 0
    Geography_Spain = 1 if Geography == "Spain" else 0
    Gender_Male = 1 if Gender == "Male" else 0

    input_data = pd.DataFrame([[
        CreditScore,
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        HasCrCard,
        IsActiveMember,
        EstimatedSalary,
        Geography_Germany,
        Geography_Spain,
        Gender_Male
    ]], columns=[
        "CreditScore",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "EstimatedSalary",
        "Geography_Germany",
        "Geography_Spain",
        "Gender_Male"
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

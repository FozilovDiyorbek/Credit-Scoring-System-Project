import streamlit as st
import pandas as pd
import joblib

# Load model
model_path = "C:/Projects/Credit_scoring_system_project/models/best_model.pkl"
model = joblib.load(model_path)

st.set_page_config(page_title="Credit Scoring App", layout="centered")

# Title
st.title("Credit Scoring Prediction")
st.write("Mijoz ma'lumotlarini kiriting va kredit bo‘yicha Default ehtimolini oling.")

# User inputs
person_age = st.slider("Yoshi", 18, 100, 25)
person_income = st.number_input("Yillik daromad (USD)", min_value=0, max_value=50000, value=5000)
person_home_ownership = st.selectbox("Uy egalik turi", [
    "RENT", "OWN", "MORTGAGE", "OTHER"
])
person_emp_length = st.slider("Ish tajribasi (yil)", 0, 50, 5)
loan_intent = st.selectbox("Kredit maqsadi", [
    "EDUCATION", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION", "MEDICAL", "VENTURE", "PERSONAL"
])
loan_amnt = st.number_input("Kredit summasi (USD)", min_value=0, value=6000)
loan_int_rate = st.slider("Kredit foizi (%)", 0, 50, 14)
cb_person_cred_hist_length = st.slider("Avvalgi kredit tarihi", 2, 30, 3)


data = pd.DataFrame({
    "person_age" : [person_age],
    "person_income" : [person_income],
    "person_home_ownership" : [person_home_ownership],
    "person_emp_length" : [person_emp_length],
    "loan_intent" : [loan_intent],
    "loan_amnt" : [loan_amnt],
    "loan_int_rate" : [loan_int_rate],
    "cb_person_cred_hist_length" : [cb_person_cred_hist_length]
})

# 4. Predict button
if st.button("Predict"):
    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]
    
    if prediction == 1:
        st.error(f"❌ Default bo‘lish ehtimoli yuqori! Ehtimollik: {probability:.2f}")
    else:
        st.success(f"✅ Kreditni to‘lash ehtimoli yuqori. Ehtimollik: {probability:.2f}")

# Footer
st.markdown("---")
st.caption("📌 ML Engineer Portfolio Project — Credit Scoring System")

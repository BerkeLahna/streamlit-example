import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def load_model():
    # Load the pre-trained model
    model = joblib.load('loan_approval_model.pkl')
    return model

def predict_loan_approval(model, input_data):
    # Perform prediction using the model
    prediction = model.predict(input_data)
    return prediction

def main():
    st.title("Loan Application Approval Prediction")
    st.write("This app predicts whether a loan application will be approved or not.")

    # Load the model
    model = load_model()

    # Bank Information Form
    st.header("Bank Information Form")
    loan_amount = st.slider("Loan Amount", 1000, 100000, 50000)
    income = st.slider("Annual Income", 1000, 100000, 50000)
    credit_score = st.slider("Credit Score", 300, 850, 650)
    employment_years = st.slider("Years of Employment", 0, 30, 5)

    input_data = pd.DataFrame({
        'LoanAmount': [loan_amount],
        'AnnualIncome': [income],
        'CreditScore': [credit_score],
        'YearsEmployed': [employment_years]
    })

    if st.button("Predict"):
        # Perform prediction
        prediction = predict_loan_approval(model, input_data)

        # Display the prediction
        if prediction[0] == 1:
            st.markdown("### Loan Application **Approved**")
        else:
            st.markdown("### Loan Application **Not Approved**")

if __name__ == "__main__":
    main()

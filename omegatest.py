import streamlit as st
import joblib

def main():
    st.title("Bank Information Classification")
    
    # Accept inputs from the user
    input_data = {
        'age': st.number_input("Select a number", min_value=18, max_value=100, value=50, step=1),
        'job':  st.selectbox("Enter job:", ['blue-collar','services','admin.', 'entrepreneur', 'self-employed','technician','management','student','retired','housemaid','unemployed']),
        'marital': st.selectbox("Enter marital status:", ['single', 'married', 'divorced']),
        'education': st.selectbox("Enter education level:", ['basic.4y','basic.6y','basic.9y', 'high.school', 'university.degree','professional.course','illiterate']),
        'default': st.selectbox("Has credit in default:", ['no', 'yes']),
        'housing': st.selectbox("Has a housing loan:", ['no', 'yes']),
        'loan': st.selectbox("Has a personal loan:", ['no', 'yes']),
        'contact': st.selectbox("Preferred contact type:", ['cellular', 'telephone']),
        'month': st.selectbox("Last contact month:", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']),
        'day_of_week': st.selectbox("Last contact day of the week:", ['mon', 'tue', 'wed', 'thu', 'fri']),
        'duration': st.number_input("Enter call duration in seconds:", min_value=0, max_value=3600, value=300,step = 1),
        'campaign': st.number_input("Enter number of contacts performed during this campaign for this client:", min_value=0, max_value=50, value=5,step = 1),
        'pdays': st.number_input("Enter number of days that passed after the client was last contacted from a previous campaign:", min_value=0, max_value=1000, value=0,step = 1),
        'previous': st.number_input("Enter number of contacts performed before this campaign for this client:", min_value=0, max_value=50, value=0,step = 1),
        'poutcome': st.selectbox("Outcome of the previous marketing campaign:", ['failure', 'success', 'nonexistent']),
        'emp.var.rate': st.number_input("Enter employment variation rate:", min_value=-5.0, max_value=5.0, value=0.0, step=0.1),
        'cons.price.idx': st.number_input("Enter consumer price index:", min_value=0.0, max_value=105.0, value=93.0, step=0.1),
        'cons.conf.idx': st.number_input("Enter consumer confidence index:", min_value=-50.0, max_value=100.0, value=0.0, step=0.1),    
        'euribor3m': st.number_input("Enter euribor 3 month rate:", min_value=0.0, max_value=5.0, value=3.0, step=0.01),
        'nr.employed': st.number_input("Enter number of employees:", min_value=0.0, max_value=10000.0, value=5000.0, step=10.0),
    }
    

    # Add a button to perform the classification
    if st.button("Perform Classification"):
        prediction = perform_classification(input_data)
        st.subheader("Prediction:")
        st.write(prediction)
        

def perform_classification(input_data):
    # Load the trained model
    model = joblib.load("bank_model (1).pkl")
    
    # Prepare the input data for prediction
    X = prepare_input_data(input_data)
    
    # Perform the prediction
    prediction = model.predict(X)
    
    return prediction


def prepare_input_data(input_data):
    # Convert input data into the format expected by the model
    # You may need to preprocess and transform the input features here
    
    # Example: Creating a pandas DataFrame from the input data
    import pandas as pd
    X = pd.DataFrame([input_data])
    cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    for col in cols:
        X[col] = le.fit_transform(X[col])
  
    # Perform any necessary preprocessing or feature engineering on X
    
    return X


if __name__ == "__main__":
    main()

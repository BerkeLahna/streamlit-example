import streamlit as st
import joblib

keys = ['age', 'duration', 'campaign', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']

col1, col2, col3, col4 = st.columns([6, 1, 1, 1])
if "slider" not in st.session_state:
    st.session_state.slider = 0

def plus(value):
    if st.session_state.slider < 1000:
        st.session_state.slider += value

def minus(value):
    if st.session_state.slider > -1000:
        st.session_state.slider -= value


def main():
    st.title("Bank Information Classification")
    
    with col1 : 
        input_data = {
            'age': st.slider("Enter age:", min_value=18, max_value=100, value=30),
            'job':  st.selectbox("Enter job:", ['blue-collar','services','admin.', 'entrepreneur', 'self-employed','technician','management','student','retired','housemaid','unemployed']),
            'marital': st.selectbox("Enter marital status:", ['single', 'married', 'divorced']),
            'education': st.selectbox("Enter education level:", ['basic.4y','basic.6y','basic.9y', 'high.school', 'university.degree','professional.course','illiterate']),
            'default': st.selectbox("Has credit in default:", ['no', 'yes']),
            'housing': st.selectbox("Has a housing loan:", ['no', 'yes']),
            'loan': st.selectbox("Has a personal loan:", ['no', 'yes']),
            'contact': st.selectbox("Preferred contact type:", ['cellular', 'telephone']),
            'month': st.selectbox("Last contact month:", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']),
            'day_of_week': st.selectbox("Last contact day of the week:", ['mon', 'tue', 'wed', 'thu', 'fri']),
            'duration': st.slider("Enter call duration in seconds:", min_value=0, max_value=3600, value=300),
            'campaign': st.slider("Enter number of contacts performed during this campaign for this client:", min_value=0, max_value=50, value=5),
            'pdays': st.slider("Enter number of days that passed after the client was last contacted from a previous campaign:", min_value=0, max_value=1000, value=0),
            'previous': st.slider("Enter number of contacts performed before this campaign for this client:", min_value=0, max_value=50, value=0),
            'poutcome': st.selectbox("Outcome of the previous marketing campaign:", ['failure', 'success', 'nonexistent']),
            'emp.var.rate': st.slider("Enter employment variation rate:", min_value=-3.0, max_value=3.0, value=0.0, step=0.1),
            'cons.price.idx': st.slider("Enter consumer price index:", min_value=0.0, max_value=105.0, value=93.0, step=0.1),
            'cons.conf.idx': st.slider("Enter consumer confidence index:", min_value=-50.0, max_value=100.0, value=0.0, step=0.1),    
            'euribor3m': st.slider("Enter euribor 3 month rate:", min_value=0.0, max_value=5.0, value=3.0, step=0.01),
            'nr.employed': st.slider("Enter number of employees:", min_value=0.0, max_value=10000.0, value=5000.0, step=10.0),
    }
    with col2:
        add_one = st.button("+1", on_click=plus(1))
        remove_one = st.button("-1", on_click=minus(1))
    with col3:
        add_one = st.button("+1", on_click=plus(5))
        remove_one = st.button("-1", on_click=minus(5))
    with col4:
        add_one = st.button("+1", on_click=plus(10))
        remove_one = st.button("-1", on_click=minus(10))

    # Add a button to perform the classification
    if st.button("Perform Classification"):
        prediction = perform_classification(input_data)
        st.subheader("Prediction:")
        st.write(prediction)
        

def perform_classification(input_data):
    # Load the trained model
    model = joblib.load("bank_model.pkl")
    
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

import streamlit as st

def main():
    st.title("Bank Information Classification")
    
    # Accept inputs from the user
    input_data = {
        'age': st.slider("Enter age:", min_value=18, max_value=100, value=30),
        'job': st.text_input("Enter job:"),
        'marital': st.selectbox("Enter marital status:", ['single', 'married', 'divorced']),
        'education': st.selectbox("Enter education level:", ['primary', 'secondary', 'tertiary']),
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
        'cons.price.idx': st.slider("Enter consumer price index:", min_value=85.0, max_value=105.0, value=93.0, step=0.1),
        'cons.conf.idx': st.slider("Enter consumer confidence index:", min_value=-50.0, max_value=-10.0, value=-30.0, step=0.1),
        'euribor3m': st.slider("Enter euribor 3 month rate:", min_value=0.0, max_value=5.0, value=3.0, step=0.01),
        'nr.employed': st.slider("Enter number of employees:", min_value=4000.0, max_value=10000.0, value=5000.0, step=10.0),
    }
    
    # Display the inputs
    st.subheader("Input Data:")
    for key, value in input_data.items():
        st.write(f"{key}: {value}")
    
    # Add a button to perform the classification
    if st.button("Perform Classification"):
        prediction = perform_classification(input_data)
        st.subheader("Prediction:")
        st.write(prediction)
        

def perform_classification(input_data):
    # Perform the classification here
    # Replace this with your actual classification code
    return "Yes"  # Dummy prediction


if __name__ == "__main__":
    main()

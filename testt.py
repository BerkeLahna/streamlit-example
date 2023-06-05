import streamlit as st
import joblib

keys = ['age', 'duration', 'campaign', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']



for key in keys:
    if key not in st.session_state:
        st.session_state[key] = 0

def plus(value, key):
        st.session_state[key] += value

def minus(value, key):
        st.session_state[key] -= value


def main():
    st.title("Bank Information Classification")
    
    col1, col2, col3 = st.columns([10, 1.4, 1.4])
    with col1:
       
        input_data = {
            'age': st.slider("Enter age:", min_value=18, max_value=100, value=18, key='age'),
            'job':  st.selectbox("Enter job:", ['blue-collar','services','admin.', 'entrepreneur', 'self-employed','technician','management','student','retired','housemaid','unemployed']),
            'marital': st.selectbox("Enter marital status:", ['single', 'married', 'divorced']),
            'education': st.selectbox("Enter education level:", ['basic.4y','basic.6y','basic.9y', 'high.school', 'university.degree','professional.course','illiterate']),
            'default': st.selectbox("Has credit in default:", ['no', 'yes']),
            'housing': st.selectbox("Has a housing loan:", ['no', 'yes']),
            'loan': st.selectbox("Has a personal loan:", ['no', 'yes']),
            'contact': st.selectbox("Preferred contact type:", ['cellular', 'telephone']),
            'month': st.selectbox("Last contact month:", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']),
            'day_of_week': st.selectbox("Last contact day of the week:", ['mon', 'tue', 'wed', 'thu', 'fri']),
            'duration': st.slider("Enter call duration in seconds:", min_value=0, max_value=3600, value=0, key='duration'),
            'campaign': st.slider("Enter number of contacts performed during this campaign for this client:", min_value=0, max_value=50, value=0, key='campaign'),
            'pdays': st.slider("Enter number of days that passed after the client was last contacted from a previous campaign:", min_value=0, max_value=1000, value=0, key='pdays'),
            'previous': st.slider("Enter number of contacts performed before this campaign for this client:", min_value=0, max_value=10, value=0, key='previous'),
            'poutcome': st.selectbox("Outcome of the previous marketing campaign:", ['failure', 'success', 'nonexistent']),
            'emp.var.rate': st.slider("Enter employment variation rate:", min_value=-5.0, max_value=5.0, value=0.0, step=0.1, key='emp.var.rate'),
            'cons.price.idx': st.slider("Enter consumer price index:", min_value=0.0, max_value=105.0, value=0.0, step=0.1, key='cons.price.idx'),
            'cons.conf.idx': st.slider("Enter consumer confidence index:", min_value=-100.0, max_value=100.0, value=0.0, step=0.1, key='cons.conf.idx'),    
            'euribor3m': st.slider("Enter euribor 3 month rate:", min_value=0.0, max_value=7.0, value=0.0, step=0.001, key='euribor3m'),
            'nr.employed': st.slider("Enter number of employees:", min_value=0, max_value=10000, value=0, step=10, key='nr.employed'),
        }
    with col2:
        st.write("")
        st.button("+1", on_click=plus, args=(1, 'age'),key = "age_add_1")
        st.button("-1", on_click=minus, args=(1, 'age'),key = "age_rem_1")
        for i in range(49):
            st.write("")
        st.button("+1", on_click=plus, args=(1, 'duration'),key = "dur_add_1")
        st.button("-1", on_click=minus, args=(1, 'duration'),key = "dur_rem_1")
        st.button("+1", on_click=plus, args=(1, 'campaign'),key = "cam_add_1")
        st.button("-1", on_click=minus, args=(1, 'campaign'),key = "cam_rem_1")
        st.write("")
        st.button("+1", on_click=plus, args=(1, 'pdays'),key = "pdays_add_1")
        st.button("-1", on_click=minus, args=(1, 'pdays'),key = "pdays_rem_1")
        st.button("+1", on_click=plus, args=(1, 'previous'),key = "previous_add_1")
        st.button("-1", on_click=minus, args=(1, 'previous'),key = "previous_rem_1")
        for i in range(6):
           st.write("")
        st.button("+1", on_click=plus, args=(1, 'emp.var.rate'),key = "emp.var.rate_add_1")
        st.button("-1", on_click=minus, args=(1, 'emp.var.rate'),key = "emp.var.rate_rem_1")
        st.button("+0.01", on_click=plus, args=(0.01, 'cons.price.idx'),key = "cons.price.idx_add_1")
        st.button("-0.01", on_click=minus, args=(0.01, 'cons.price.idx'),key = "cons.price.idx_rem_1")
        st.button("+0.1", on_click=plus, args=(0.1, 'cons.conf.idx'),key = "cons.conf.idx_add_1")
        st.button("-0.1", on_click=minus, args=(0.1, 'cons.conf.idx'),key = "cons.conf.idx_rem_1")
        st.button("+0.01", on_click=plus, args=(0.01, 'euribor3m'),key = "euribor3m_add_1")
        st.button("-0.01", on_click=minus, args=(0.01, 'euribor3m'),key = "euribor3m_rem_1")
        st.button("+1", on_click=plus, args=(1, 'nr.employed'),key = "nr.employed_add_1")
        st.button("-1", on_click=minus, args=(1, 'nr.employed'),key = "nr.employed_rem_1")
        

    with col3:
        st.write("")
        st.button("+5", on_click=plus, args=(5, 'age'), key="add_one_5")
        st.button("-5", on_click=minus, args=(5, 'age'), key="remove_one_5")
        for i in range(49):
           st.write("")
        st.button("+5", on_click=plus, args=(5, 'duration'),key = "dur_add_5")
        st.button("-5", on_click=minus, args=(5, 'duration'),key = "dur_rem_5")
        st.button("+5", on_click=plus, args=(5, 'campaign'),key = "cam_add_5")
        st.button("-5", on_click=minus, args=(5, 'campaign'),key = "cam_rem_5")
        st.write("")
        st.button("+5", on_click=plus, args=(5, 'pdays'),key = "pdays_add_5")
        st.button("-5", on_click=minus, args=(5, 'pdays'),key = "pdays_rem_5")
        st.button("+5", on_click=plus, args=(5, 'previous'),key = "previous_add_5")
        st.button("-5", on_click=minus, args=(5, 'previous'),key = "previous_rem_5")
        for i in range(6):
           st.write("")
        st.button("+5", on_click=plus, args=(5, 'emp.var.rate'),key = "emp.var.rate_add_5")
        st.button("-5", on_click=minus, args=(5, 'emp.var.rate'),key = "emp.var.rate_rem_5")
        st.button("+0.1", on_click=plus, args=(0.1, 'cons.price.idx'),key = "cons.price.idx_add_5")
        st.button("-0.1", on_click=minus, args=(0.1, 'cons.price.idx'),key = "cons.price.idx_rem_5")
        st.button("+1", on_click=plus, args=(1, 'cons.conf.idx'),key = "cons.conf.idx_add_5")
        st.button("-1", on_click=minus, args=(1, 'cons.conf.idx'),key = "cons.conf.idx_rem_5")
        st.button("+0.05", on_click=plus, args=(0.05, 'euribor3m'),key = "euribor3m_add_5")
        st.button("-0.05", on_click=minus, args=(0.05, 'euribor3m'),key = "euribor3m_rem_5")
        st.button("+5", on_click=plus, args=(5, 'nr.employed'),key = "nr.employed_add_5")
        st.button("-5", on_click=minus, args=(5, 'nr.employed'),key = "nr.employed_rem_5")

    # Add a button to perform the classification
    if st.button("Perform Classification"):
        prediction = perform_classification(input_data)
#         st.subheader("Prediction:")
#         st.write(prediction)




def perform_classification(input_data):
    # Load the trained model
    model = joblib.load("bank_model1.pkl")

    # Prepare the input data for prediction
    X = prepare_input_data(input_data)

    # Perform the prediction
    prediction = model.predict(X)

    # Map the predicted values to text labels and colors
    label_map = {0: ("You are not elligible for creating a deposit account", "rgba(255, 0, 0, 0.5)"), 1: ("You are elligible for creating a deposit account", "rgba(0, 255, 0, 0.5)")}
    prediction_label, prediction_color = label_map[prediction[0]]

    # Display the text box with colored background
    st.markdown(f'<div style="background-color: {prediction_color}; padding: 20px;">{prediction_label}</div>',
                unsafe_allow_html=True)

#     return prediction_label


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

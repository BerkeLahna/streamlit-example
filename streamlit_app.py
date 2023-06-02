import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("bank-additional.csv")  # Replace "bank_data.csv" with your actual dataset file
print(data.head())
# Split the data into features and target
X = data.drop('y', axis=1)
y = data['y']

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Create a Streamlit app
def main():
    st.title("Bank Information Classification")
    st.write("Predicting whether a customer subscribes to a term deposit")

    # Add input fields for user to enter bank information
    age = st.slider("Age", min_value=18, max_value=100, value=30)
    job = st.selectbox("Job", ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired',
                               'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'])
    marital = st.selectbox("Marital Status", ['divorced', 'married', 'single', 'unknown'])
    education = st.selectbox("Education", ['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate',
                                           'professional.course', 'university.degree', 'unknown'])
    default = st.selectbox("Default Credit", ['no', 'yes', 'unknown'])
    housing = st.selectbox("Housing Loan", ['no', 'yes', 'unknown'])
    loan = st.selectbox("Personal Loan", ['no', 'yes', 'unknown'])
    contact = st.selectbox("Contact Type", ['cellular', 'telephone'])
    month = st.selectbox("Month", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    day_of_week = st.selectbox("Day of Week", ['mon', 'tue', 'wed', 'thu', 'fri'])
    duration = st.slider("Call Duration (seconds)", min_value=0, max_value=5000, value=200)
    campaign = st.slider("Number of Contacts", min_value=1, max_value=50, value=5)
    pdays = st.slider("Days Since Last Contact", min_value=0, max_value=30, value=10)
    previous = st.slider("Number of Previous Contacts", min_value=0, max_value=20, value=2)
    poutcome = st.selectbox("Previous Outcome", ['failure', 'nonexistent', 'success'])
    emp_var_rate = st.slider("Employment Variation Rate", min_value=-3.0, max_value=3.0, value=0.0)
    cons_price_idx = st.slider("Consumer Price Index", min_value=92.0, max_value=95.0, value=93.0)
    cons_conf_idx = st.slider("Consumer Confidence Index", min_value=-60.0, max_value=-20.0, value=-40.0)
    euribor3m = st.slider("Euribor 3 Month Rate", min_value=0.0, max_value=5.0, value=2.0)
    nr_employed = st.slider("Number of Employees", min_value=5000, max_value=6000, value=5500)

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'age': [age],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'default': [default],
        'housing': [housing],
        'loan': [loan],
        'contact': [contact],
        'month': [month],
        'day_of_week': [day_of_week],
        'duration': [duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous],
        'poutcome': [poutcome],
        'emp.var.rate': [emp_var_rate],
        'cons.price.idx': [cons_price_idx],
        'cons.conf.idx': [cons_conf_idx],
        'euribor3m': [euribor3m],
        'nr.employed': [nr_employed]
    })

    # Convert categorical variables to numerical using one-hot encoding
    input_data = pd.get_dummies(input_data)

    # Predict the result
    prediction = model.predict(input_data)

    st.write(f"Prediction: {'Yes' if prediction[0] == 1 else 'No'}")
    st.write(f"Accuracy: {accuracy:.2f}")


if __name__ == '__main__':
    main()

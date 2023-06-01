import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data():
    # Load the Iris dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    return X, y

def train_model(X, y):
    # Train a random forest classifier
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return clf, accuracy

def main():
    st.title("Iris Flower Classification")
    st.write("This app performs classification of Iris flower species using a Random Forest classifier.")

    # Load data
    X, y = load_data()

    # Train the model
    model, accuracy = train_model(X, y)

    # Display accuracy
    st.write(f"Model accuracy: {accuracy}")

    # Classification form
    st.sidebar.header("Classify Iris Flower")
    sepal_length = st.sidebar.slider("Sepal Length", float(X[:, 0].min()), float(X[:, 0].max()), float(X[:, 0].mean()))
    sepal_width = st.sidebar.slider("Sepal Width", float(X[:, 1].min()), float(X[:, 1].max()), float(X[:, 1].mean()))
    petal_length = st.sidebar.slider("Petal Length", float(X[:, 2].min()), float(X[:, 2].max()), float(X[:, 2].mean()))
    petal_width = st.sidebar.slider("Petal Width", float(X[:, 3].min()), float(X[:, 3].max()), float(X[:, 3].mean()))

    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)
    species = iris.target_names[prediction[0]]

    st.sidebar.markdown(f"Predicted species: **{species}**")

if __name__ == "__main__":
    main()

import streamlit as st
import joblib
import pandas as pd
import numpy as np
import warnings




# Provide the absolute path to the model file
model_path = r"C:\Users\pc\Desktop\bank-2\bank-additional\bank_model.pkl"
df_path = r"C:\Users\pc\Desktop\bank-2\bank-additional\filtered_df.csv"

# Load the model
model = joblib.load(model_path)

# Use the loaded model for prediction or other operations

df = pd.read_csv(df_path , delimiter=',')


model.predict(df[0:1])


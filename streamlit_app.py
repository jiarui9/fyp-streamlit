import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load your trained model
model = joblib.load('domain_rf_model.joblib')

# Define the structure of your web app
st.title('Domain Name Price Prediction')

# File uploader allows user to add their own CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

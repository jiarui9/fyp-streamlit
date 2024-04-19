import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np



# Load the model
# model = load_model('MLP_model.h5')

# Load your trained model
model = joblib.load('domain_rf_model.joblib')

# Define the structure of your web app
st.title('Domain Name Price Prediction')

# File uploader allows user to add their own CSV
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

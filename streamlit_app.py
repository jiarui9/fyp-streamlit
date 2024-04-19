import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np

# Load your trained model
model = load_model('MLP_model.h5')

# Define the structure of your web app
st.title('Domain Name Price Prediction')

import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np

# Load your trained model
model = load_model('MLP_model.h5')

# Define the structure of your web app
st.title('Domain Name Price Prediction')

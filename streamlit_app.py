import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np

# Load the model
model = load_model('path_to_your_directory/MLP_model.h5')

# Define the Streamlit app
def main():
    st.title("Domain Name Price Prediction")

    # Create inputs for each feature in the dataset
    # Make sure to match these input types and names to what the model expects
    SEO_Score = st.number_input("SEO Score", min_value=0, max_value=100, value=50)
    Domain_Age = st.number_input("Domain Age", min_value=0, value=10)
    TLD_Score = st.number_input("TLD Score", min_value=0, max_value=100, value=50)
    Search_Occurrences = st.number_input("Search Occurrences", min_value=0, value=100)
    Word_Composition_Score = st.number_input("Word Composition Score", min_value=0.0, max_value=100.0, value=50.0)
    Domain_Length_Score = st.number_input("Domain Length Score", min_value=0, max_value=100, value=50)

    # When the 'Predict' button is clicked, make the prediction and display it
    if st.button("Predict"):
        # Create the feature array
        features = np.array([[SEO_Score, Domain_Age, TLD_Score, Search_Occurrences,
                              Word_Composition_Score, Domain_Length_Score]])
        # Predict the price
        price = model.predict(features)
        # Display the prediction
        st.success(f"The predicted price of the domain is: ${price[0][0]:.2f}")

if __name__ == "__main__":
    main()

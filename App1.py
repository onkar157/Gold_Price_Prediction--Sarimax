
# Installing packages
import pickle
import pandas as pd
import numpy as np
import streamlit as st
from statsmodels.tsa.arima.model import ARIMA

# Title and sidebar
st.title("Model Deployment: SARIMAX")
st.sidebar.header("User input parameters")


# Input function
def user_input_features():
    fc_days = st.sidebar.number_input("Insert number of days to predict.")
    return int(fc_days)


prediction_days = user_input_features()


# Loading trained model and making predictions
loaded_model = pickle.load(open("C:/Users/onkar/Downloads/sarima-fitted-model.pickle", "rb"))
predictions = loaded_model.forecast(436 + prediction_days)


# Output predictions
st.subheader('Predicted Result')
st.write(predictions[436:].round(2))




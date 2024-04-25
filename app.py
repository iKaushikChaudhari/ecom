import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier

# Get the absolute path to the directory of this script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path to ecom.pkl
model_path = os.path.join(dir_path, "ecom.pkl")

# Check if ecom.pkl exists
if not os.path.exists(model_path):
    st.error("Error loading the model: ecom.pkl not found")
    st.stop()

# Load the model using the absolute path
try:
    predict = pickle.load(open(model_path, "rb"))
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

st.title('E-Commerce Shipping')
st.markdown('Product Shipment Delivered on time or not?')

st.header("Order Details")

# Getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Customer_care_calls = st.text_input('Customer_care_calls')

with col2:
    Customer_rating = st.text_input('Customer_rating')

with col3:
    Cost_of_the_Product = st.text_input('Cost_of_the_Product')

with col1:
    Prior_purchases = st.text_input('Prior_purchases')

with col2:
    Product_importance = st.text_input('Product_importance')

with col3:
    Discount_offered = st.text_input('Discount_offered')

with col1:
    Weight_in_gms = st.text_input('Weight_in_gms')

with col2:
    Mode_of_Shipment_0 = st.text_input('Mode_of_Shipment_0')

# Code for Prediction
Time_YN = ''

# Creating a button for Prediction
if st.button('Reached.on.Time_Y.N'):
    user_input = [Cost_of_the_Product, Customer_care_calls, Customer_rating, Prior_purchases,
                  Product_importance, Discount_offered, Weight_in_gms]
    
    # Convert user inputs to float values
    try:
        user_input = [float(x) for x in user_input]
    except ValueError:
        st.error("Error converting input to float")
        st.stop()

    Time_YN = predict([user_input])

    if Time_YN[0] == 1:
        Time_YN = 'The Product Will Reach On Time'
    else:
        Time_YN = 'The Product Will Not Reach On Time'

st.success(Time_YN)
st.markdown('Created By :- Kaushik Chaudhari')

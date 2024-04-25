import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier

# Print the current working directory
print("Current directory:", os.getcwd())

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

# Reading the CSV dataset
data = pd.read_csv("your_dataset.csv")  # Replace "your_dataset.csv" with the actual CSV filename

# Displaying the first few rows of the dataset
st.write("Sample Data:", data.head())

# Getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Customer_care_calls = st.selectbox('Customer_care_calls', data['Customer_care_calls'].unique())

with col2:
    Customer_rating = st.selectbox('Customer_rating', data['Customer_rating'].unique())

with col3:
    Cost_of_the_Product = st.selectbox('Cost_of_the_Product', data['Cost_of_the_Product'].unique())

with col1:
    Prior_purchases = st.selectbox('Prior_purchases', data['Prior_purchases'].unique())

with col2:
    Product_importance = st.selectbox('Product_importance', data['Product_importance'].unique())

with col3:
    Discount_offered = st.selectbox('Discount_offered', data['Discount_offered'].unique())

with col1:
    Weight_in_gms = st.selectbox('Weight_in_gms', data['Weight_in_gms'].unique())

# Code for Prediction
Time_YN = ''

# Creating a button for Prediction
if st.button('Predict'):
    user_input = [[Customer_care_calls, Customer_rating, Cost_of_the_Product, Prior_purchases,
                  Product_importance, Discount_offered, Weight_in_gms]]
    
    Time_YN = predict(user_input)

    if Time_YN[0] == 1:
        Time_YN = 'The Product Will Reach On Time'
    else:
        Time_YN = 'The Product Will Not Reach On Time'

st.success(Time_YN)
st.markdown('Created By :- Kaushik Chaudhari')

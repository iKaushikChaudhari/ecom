import streamlit as st
import pandas as pd
import numpy as np
#from prediction import predict
import pickle
from sklearn.ensemble import RandomForestClassifier

predict = pickle.load(open("ecom.pkl", "rb"))

st.title('E-Commerce Shipping')
st.markdown('Product Shipment Delivered on time or not?')

st.header("Plant Features")
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
if predict and st.button('Reached.on.Time_Y.N'):

    user_input = [Cost_of_the_Product,Customer_care_calls,Customer_rating,Prior_purchases ,Product_importance,Discount_offered,Weight_in_gms]
    #user_input = [float(x) for x in user_input]

    Time_YN = predict([user_input])

    if Time_YN[0] == 1:
        Time_YN = 'The Product Will Reach On Time'
    else:
        Time_YN = 'The Product Will Not Reach On Time'

st.success(Time_YN)
st.markdown(
    'Created By :- Kaushik Chaudhari')

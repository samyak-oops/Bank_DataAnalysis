import streamlit as st
import tensorflow as tf
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
import numpy as np

## Load the trained model
model = tf.keras.models.load_model('model.h5')

## load the scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

## load the encoder
with open('label_encoder_gender.pkl', 'rb') as f:
    encoder = pickle.load(f)

## load the one hot encoder
with open('one_hot_encoder_geography.pkl', 'rb') as f:
    one_hot_encoder = pickle.load(f)

## Streamlit app
st.title("Bank Customer Churn Prediction")

## Input fields
input_data = {}
input_data['CreditScore'] = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
input_data['Geography'] = st.selectbox("Geography", options=['France', 'Spain', 'Germany'])
input_data['Gender'] = st.selectbox("Gender", options=['Male', 'Female'])
input_data['Age'] = st.number_input("Age", min_value=18, max_value=100, value=30)
input_data['Tenure'] = st.number_input("Tenure", min_value=0, max_value=10, value=3)
input_data['Balance'] = st.number_input("Balance", min_value=0.0, value=10000.0)
input_data['NumOfProducts'] = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
input_data['HasCrCard'] = st.selectbox("Has Credit Card", options=[0, 1])
input_data['IsActiveMember'] = st.selectbox("Is Active Member", options=[0, 1])
input_data['EstimatedSalary'] = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)   

## one hot encode the Geography column
geography_encoded = one_hot_encoder.transform(
    [[input_data['Geography']]]
).toarray()

geography_encoded_df = pd.DataFrame(
    geography_encoded,
    columns=one_hot_encoder.get_feature_names_out(['Geography'])
)

## combine
input_df = pd.DataFrame([input_data])
input_df = pd.concat([input_df, geography_encoded_df], axis=1)
input_df.drop('Geography', axis=1, inplace=True)

## label encode Gender
input_df['Gender'] = encoder.transform([input_data['Gender']])[0]

## ensure correct column order
input_df = input_df[scaler.feature_names_in_]

## scale
input_scaled = scaler.transform(input_df)
## prediction
prediction = model.predict(input_scaled)
st.subheader("Churn Probability")
st.write(prediction[0][0])
st.subheader("Churn Prediction")
st.write(f'Churn Probability: {prediction[0][0]:.2f}')
if prediction[0][0] > 0.5:
    st.write("The customer is likely to churn.")
else:
    st.write("The customer is unlikely to churn.")

import streamlit as st
import pandas as pd
import joblib

st.title('Insurance Purchase Prediction v3')

# Read the dataset to fill values in the dropdown lists
df = pd.read_csv('C:\\Users\\Babu\\Data_Documents\\Python Class\\WIP_Hack\\train.csv')

# Create input fields
Gender = st.selectbox("Gender", ["Male", "Female"])
Age = st.number_input("Age", min_value=18, max_value=100, value=30)
Driving_License = st.selectbox("Driving_License", df['Driving_License'].unique())
Region_Code = st.selectbox("Region_Code", df['Region_Code'].unique())
Previously_Insured = st.selectbox("Previously_Insured", df['Previously_Insured'].unique())
Vehicle_Damage = st.selectbox("Vehicle_Damage", ["Yes", "No"])
Annual_Premium = st.number_input("Annual_Premium")
Policy_Sales_Channel = st.selectbox("Policy_Sales_Channel", df['Policy_Sales_Channel'].unique())
Vintage = st.number_input("Vintage")

# Convert input values into a dictionary
inputs = {
    "Gender": 1 if Gender == "Male" else 0,
    "Age": Age,
    "Driving_License": Driving_License,
    "Region_Code": Region_Code,
    "Previously_Insured": Previously_Insured,
    "Vehicle_Damage": 1 if Vehicle_Damage == "Yes" else 0,
    "Annual_Premium": Annual_Premium,
    "Policy_Sales_Channel": Policy_Sales_Channel,
    "Vintage": Vintage
}

# Click for prediction
if st.button('Predict'):
    model = joblib.load("C:\\Users\\Babu\\Data_Documents\\Python Class\\WIP_Hack\\jobchg_log_model.pkl")
    # Convert dictionary to DataFrame
    X_input = pd.DataFrame([inputs])
    # Model Prediction
    prediction = model.predict(X_input)
    # Display the prediction
    st.write("Prediction:", "Interested" if prediction[0] == 1 else "Not Interested")

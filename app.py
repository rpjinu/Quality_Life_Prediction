import streamlit as st
import pandas as pd
import numpy as np
import joblib  # Or use pickle depending on how you've saved the model

# Load the pre-trained pipeline model
model = joblib.load(r'C:\Users\Ranjan kumar pradhan\.vscode\project_vs\Quality_life_predict\pipeline_model.pkl') 

# Function to predict Quality of Life Value
def predict_quality_of_life(data):
    # The model is expecting a DataFrame, so convert user input into a DataFrame
    input_data = pd.DataFrame(data, index=[0])  # Convert input into DataFrame for prediction
    prediction = model.predict(input_data)
    return prediction[0]  # Return the predicted value

# Streamlit app
def app():
    st.title("Quality of Life Value Prediction")

    # Inputs from the user
    st.sidebar.header("Enter Your Data")

    # Collect all the input fields
    purchasing_power_value = st.number_input('Purchasing Power Value', value=0.0)
    purchasing_power_category = st.selectbox('Purchasing Power Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    safety_value = st.number_input('Safety Value', value=0.0)
    safety_category = st.selectbox('Safety Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    health_care_value = st.number_input('Health Care Value', value=0.0)
    health_care_category = st.selectbox('Health Care Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    climate_value = st.number_input('Climate Value', value=0.0)
    climate_category = st.selectbox('Climate Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    cost_of_living_value = st.number_input('Cost of Living Value', value=0.0)
    cost_of_living_category = st.selectbox('Cost of Living Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    property_price_to_income_value = st.number_input('Property Price to Income Value', value=0.0)
    property_price_to_income_category = st.selectbox('Property Price to Income Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    traffic_commute_time_value = st.number_input('Traffic Commute Time Value', value=0.0)
    traffic_commute_time_category = st.selectbox('Traffic Commute Time Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    pollution_value = st.number_input('Pollution Value', value=0.0)
    pollution_category = st.selectbox('Pollution Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    quality_of_life_category = st.selectbox('Quality of Life Category', ['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

    # Combine inputs into a dictionary
    input_data = {
        'Purchasing Power Value': purchasing_power_value,
        'Purchasing Power Category': purchasing_power_category,
        'Safety Value': safety_value,
        'Safety Category': safety_category,
        'Health Care Value': health_care_value,
        'Health Care Category': health_care_category,
        'Climate Value': climate_value,
        'Climate Category': climate_category,
        'Cost of Living Value': cost_of_living_value,
        'Cost of Living Category': cost_of_living_category,
        'Property Price to Income Value': property_price_to_income_value,
        'Property Price to Income Category': property_price_to_income_category,
        'Traffic Commute Time Value': traffic_commute_time_value,
        'Traffic Commute Time Category': traffic_commute_time_category,
        'Pollution Value': pollution_value,
        'Pollution Category': pollution_category,
        'Quality of Life Category': quality_of_life_category
    }

    # When the user clicks 'Predict', run the prediction
    if st.button('Predict'):
        prediction = predict_quality_of_life(input_data)
        st.write(f"Predicted Quality of Life Value: {prediction}")

if __name__ == "__main__":
    app()


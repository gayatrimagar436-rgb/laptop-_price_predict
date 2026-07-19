 Laptop Price Predictor Frontend

This project provides a Streamlit web application to predict laptop prices based on various specifications. It utilizes a trained Linear Regression model (`Lr_laptop.pkl`) and a scaler (`scaler.pkl`) to preprocess input data.

## Features

- **Laptop Price Prediction**: Predict the final price of a laptop based on its specifications.
- **Interactive Input**: Users can input various laptop features through a user-friendly interface.

## Setup and Run

### Prerequisites

Make sure you have Python installed. It's recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install the required libraries:

pip install streamlit pandas scikit-learn joblib
Project Structure
Your project directory should look something like this:

laptop_price_predictor/
├── streamlit_app.py
├── Lr_laptop.pkl
├── scaler.pkl
└── columns.pkl
Make sure to place the Lr_laptop.pkl, scaler.pkl, and columns.pkl files (generated from this notebook) in the same directory as your streamlit_app.py.

streamlit_app.py Content
import streamlit as st
import pandas as pd
import joblib

# Load the trained model, scaler, and columns
model = joblib.load('Lr_laptop.pkl')
scaler = joblib.load('scaler.pkl')
model_columns = joblib.load('columns.pkl')

st.title('Laptop Price Predictor')

st.write("Enter the specifications of the laptop to predict its price:")

# Create input fields for each feature
input_data = {}
for col in model_columns:
    if col == 'RAM':
        input_data[col] = st.number_input('RAM (GB)', min_value=4, max_value=128, value=8, step=4)
    elif col == 'Storage':
        input_data[col] = st.number_input('Storage (GB)', min_value=128, max_value=4000, value=512, step=128)
    elif col == 'Screen':
        input_data[col] = st.number_input('Screen Size (inches)', min_value=10.0, max_value=20.0, value=15.6, step=0.1)
    elif col.startswith('Laptop_'):
        input_data[col] = 0 # Placeholder for one-hot encoded 'Laptop' features
    elif col.startswith('Status_'):
        input_data[col] = 0 # Placeholder for one-hot encoded 'Status' features
    elif col.startswith('Brand_'):
        input_data[col] = 0 # Placeholder for one-hot encoded 'Brand' features
    elif col.startswith('Model_'):
        input_data[col] = 0 # Placeholder for one-hot encoded 'Model' features
    elif col.startswith('CPU_'):
        input_data[col] = 0 # Placeholder for one-hot encoded 'CPU' features
    elif col.startswith('Storage type_'):
        input_data[col] = 0 # Placeholder for one-hot encoded 'Storage type' features
    elif col.startswith('GPU_'):
        input_data[col] = 0 # Placeholder for one-hot encoded 'GPU' features
    elif col == 'Touch_Yes':
        input_data[col] = st.checkbox('Touchscreen', value=False)
    # Add more specific input widgets for other one-hot encoded features if needed


# Example of how to handle one-hot encoded categorical features (you'll need to adapt this)
# For simplicity, let's assume we allow user to select Brand and the rest are set to 0
selected_brand = st.selectbox('Brand', [col.replace('Brand_', '') for col in model_columns if col.startswith('Brand_')])
if selected_brand:
    input_data[f'Brand_{selected_brand}'] = 1

selected_status = st.selectbox('Status', [col.replace('Status_', '') for col in model_columns if col.startswith('Status_')])
if selected_status:
    input_data[f'Status_{selected_status}'] = 1

# This part needs careful handling as there are many unique values
# For simplicity, we are not adding direct dropdowns for Laptop, Model, CPU, GPU, Storage type
# You might want to implement search, dynamic dropdowns, or fewer features if the list is too long.


if st.button('Predict Price'):
    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])

    # Ensure all columns are present, fill missing with 0 for one-hot encoded features
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    # Reorder columns to match the training data
    input_df = input_df[model_columns]

    # Scale numerical features (assuming scaler was fitted on numerical features only)
    # If the scaler was fitted on the entire one-hot encoded dataframe, adjust accordingly
    # For this example, let's assume the scaler expects the same columns as the model
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]
    st.success(f"The predicted laptop price is: €{prediction:.2f}")

Running the Streamlit App
Navigate to the project directory in your terminal and run:

streamlit run streamlit_app.py
This will open the Streamlit application in your web browser.


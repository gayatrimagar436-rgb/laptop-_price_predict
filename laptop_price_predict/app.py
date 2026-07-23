"""import joblib 
import streamlit as st 
import pandas as pd 


model=joblib.load("laptop_price_prediction/Lr_laptop.pkl")
scaler=joblib.load("laptop_price_prediction/scaler.pkl")
columns=joblib.load("laptop_price_prediction/columns.pkl")"""
import os
import joblib
import streamlit as st
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


model = joblib.load(os.path.join(BASE_DIR, "Lr_laptop.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
columns = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))

st.set_page_config(page_title="laptop price predictor",
                   layout="centered")
st.title("laptop price prediction" )
st.write("Enter the specifications of the laptop to predict its price:")


ram=st.number_input("RAM",
                    min_value=5,
                    max_value=64,
                    value=8)
storage=st.number_input("Storage",
                        min_value=128,
                        max_value=1000,
                        value=256)
screen=st.number_input("Screen",
                       min_value=5,
                       max_value=15,
                       value=6)
brand=st.selectbox("Brand",["HP","Asus","Acer","Razer Book","MSI Katana","Lenova","Acer Aspire","MacBook"])
status=st.selectbox("Status",["new","Refurbished"])
cpu=st.selectbox("CPU",["Intel Core i5","Intel Celeron","Intel Core i3","Intel Core i7","AMD Ryzen 5","AMD Ryzen 7","AMD Ryzen 3"])
storage_type =st.selectbox("Storage Type",["SSD","eMMC"])
gpu=st.selectbox("GPU",["RTX 4060","RTX 3050","RTX 3060"])
touch=st.selectbox("Touch",["YES","NO"])

if st.button("Predict Price"):
    data={col: 0 for col in columns }
    data["RAM"]=ram 
    data["Storage"]=storage
    data["Screen"]=screen 

    data[f"brand_{brand}"]=1
    data[f"status_{status}"]=1
    data[f"cpu_{cpu}"]=1
    data[f"storage_{storage_type}"]=1
    data[f"gpu_{gpu}"]=1
    data[f"touch{touch}"]=1

    df=pd.DataFrame([data],columns=columns)
scaled_feature=scaler.transform(df)
price=model.predict(scaled_feature)[0]
st.success(f"predicted price :{price:.2f}")





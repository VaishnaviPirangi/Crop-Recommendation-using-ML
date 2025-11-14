import pandas as pd
import pickle as pkl
import streamlit as st

model=pkl.load(open("Crop_recommendation.pkl","rb"))

st.header=('Crop Recommendation')
data=pd.read_csv("crop_dataset.csv")

N=st.number_input('Enter Nitrogen (mg/kg)')
P=st.number_input('Enter Phosphorous (mg/kg)')
K=st.number_input('Enter Potassium (mg/kg)')
t=st.number_input('Enter Temperature (C)')
h=st.number_input('Enter Humidity (%)')
ph=st.number_input('Enter pH value')
r=st.number_input('Enter Rainfall (mm)')


input=pd.DataFrame([[N,P,K,t,h,ph,r]],columns=['nitrogen','phosphorous','potassium','temperature','humidity','ph','rainfall'])

if st.button("Recommend Crop"):
    output=model.predict(input)
    out_str='The recommended crop is '+str(output[0])
    st.success(out_str)



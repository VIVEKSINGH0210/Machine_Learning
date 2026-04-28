import streamlit as st
import pandas as pd
import joblib
expected_columns=joblib.load('columns.pkl')
scaler=joblib.load('scaler.pkl')
model=joblib.load('LR_heart.pkl')
st.title("Heart stroke prediction")
st.markdown("provide the following Details")
age=st.slider("Age",18,100,40)
sex=st.selectbox("Sex",['M','F'])
chest_pain=st.selectbox("Chest Pain Type",['ATA','NAP','TA','ASY'])
resting_BP=st.number_input("Rsting Blood Pressure(mm Hg)",80,200,120)
cholesterol=st.number_input("Cholesterol(mg/dL)",100,600,200)
fasting_BS=st.selectbox("Fasting Blood Sugar>120mg/dL",[0,1])
resting_ecg=st.selectbox("Resting ECG",["Normal","ST","LVH"])
maxHR=st.slider("Max Heart Rate",60,220,150)
ExerciseAgina=st.selectbox("Exercise-Induced Angina",["Y","N"])
OldPeak=st.slider("OldPeak (ST Depression)",0.0,6.0,1.0)
st_Slope=st.selectbox("ST Slope",["UP","FLAT","DOWN"])
if st.button("Predict"):
  raw_input={
    "Age":age,
    "RestingBP":resting_BP,
    "Cholesterol":cholesterol,
    "FastingBS":fasting_BS,
    "MaxHR":maxHR,
    "Oldpeak":OldPeak
  }
  raw_input[f"Sex{sex}"] = 1
  raw_input[f"ChestPainType{chest_pain}"] = 1
  raw_input[f"RestingECG{resting_ecg}"] = 1
  raw_input[f"ExerciseAngina{ExerciseAgina}"] = 1
  raw_input[f"ST_Slope{st_Slope}"] = 1 
  
  input_df=pd.DataFrame([raw_input])
  for col in expected_columns:
    if col not in input_df.columns:
      input_df[col]=0
  input_df=input_df[expected_columns]
  scaled_input=scaler.transform(input_df)
  st.write(input_df)
  prediction=model.predict(scaled_input)[0]
  if prediction==0:
    st.success("Low risk of Heart Disease")
  else:
    st.error("High risk of Heart Disease")
      

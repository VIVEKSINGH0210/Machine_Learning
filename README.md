❤️ Heart Stroke Prediction App

This project is a Machine Learning based web app built using Streamlit that predicts the risk of heart disease based on user input.

It uses real-world medical parameters and applies a trained ML model to give instant predictions.

🚀 Project Overview

The goal of this project is to:

Analyze heart disease data

Build multiple ML models

Select the best-performing model

Deploy it as an interactive web app

🧠 Machine Learning Workflow

The project follows a complete ML pipeline:

1. Data Analysis (EDA)

Checked distributions of features

Found patterns between health parameters and heart disease

2. Data Cleaning & Preprocessing

Handled missing/null values

Encoded categorical variables

Feature scaling applied using Standard Scaler

3. Model Building

Trained multiple models:

Logistic Regression ✅ (Best)

KNN

Decision Tree

SVM

Naive Bayes

👉 Logistic Regression gave the highest accuracy, so it was selected.

💾 Model Saving

The trained components were saved using Joblib:

LR_heart.pkl → Trained Logistic Regression model

scaler.pkl → Feature scaling object

columns.pkl → Final feature columns used during training

🌐 Web App Features

Built with Streamlit UI components:

Slider (Age, Max Heart Rate, OldPeak)

SelectBox (Sex, Chest Pain Type, ECG, etc.)

Number Input (BP, Cholesterol)

Button (Predict)

📊 User Inputs:

Age

Sex

Chest Pain Type

Resting Blood Pressure

Cholesterol

Fasting Blood Sugar

Resting ECG

Max Heart Rate

Exercise-Induced Angina

OldPeak

ST Slope

⚙️ How It Works

User enters health details

Data is converted into model format (one-hot encoding)

Missing columns are handled using columns.pkl

Data is scaled using scaler.pkl

Model predicts using LR_heart.pkl

🎯 Output

✅ Low Risk of Heart Disease

❌ High Risk of Heart Disease

🖥️ Run Locally

Step 1: Install dependencies

pip install streamlit pandas scikit-learn joblib

Step 2: Run the app

streamlit run app.py

📁 Project Structure
├── app.py
├── LR_heart.pkl
├── scaler.pkl
├── columns.pkl
├── heart.csv
└── README.md
📸 App Preview

⚠️ Important Note

This project is for educational purposes only.

It should not be used as a medical diagnosis tool.


Author: Vivek Kumar

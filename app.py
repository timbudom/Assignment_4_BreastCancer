import streamlit as st
import pandas as pd
import joblib
from sklearn.datasets import load_breast_cancer

# Load the dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Load the model, scaler, and selector
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')
selector = joblib.load('selector.pkl')

# Streamlit app
st.title('Breast Cancer Prediction')

st.write('### Dataset')
st.write(df.head())

st.write('### Make a Prediction')
user_input = st.text_area('Enter feature values separated by commas')

if st.button('Predict'):
    input_data = [float(i) for i in user_input.split(',')]
    input_scaled = scaler.transform([input_data])
    input_selected = selector.transform(input_scaled)
    prediction = model.predict(input_selected)
    st.write('Prediction:', 'Malignant' if prediction[0] else 'Benign')

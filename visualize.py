import streamlit as st
import requests
import numpy as np
from PIL import Image

st.title('Brain MRI Metastasis Segmentation')

uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        # Call your FAST API endpoint with the uploaded file
        response = requests.post("http://localhost:8000/predict", files={"file": uploaded_file})
        st.image(response.json(), caption='Predicted Segmentation', use_column_width=True)

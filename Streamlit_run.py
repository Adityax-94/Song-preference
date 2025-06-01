import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("spotify-recommender.pkl")

# Title of the app
st.title("🎧 Spotify Song Preference Predictor")

st.write("Enter the song features below to predict if you'll like the song.")

# Input fields for features
feature1 = st.number_input("Danceability", value=0.78)
feature2 = st.number_input("Energy", value=0.57)
feature3 = st.number_input("key", value=1)
feature4 = st.number_input("loudness", value=-7.51)
feature5 = st.number_input("mode", value=1)
feature6 = st.number_input("speechiness", value=0.22)
feature7 = st.number_input("acousticness", value=0.14)
feature8 = st.number_input("instrumentalness", value=0)
feature9 = st.number_input("liveness", value=0.07)
feature10 = st.number_input("valence", value=0.64)
feature11= st.number_input("tempo", value=155.11)
feature12 = st.number_input("duration in miliseconds", value=179413)
feature13 = st.number_input("time_signature", value=4)
# Add/remove fields as needed depending on your model

# When the Predict button is clicked
if st.button("Predict",):
    features = np.array([[feature1, feature2, feature3, feature4, feature5, feature6,
                        feature7, feature8, feature9, feature10, feature11, feature12, feature13]])
    prediction = model.predict(features)[0]
    
    if prediction < 0.5:
        st.error("Prediction: Not so popular Features ❌")
    else:
        st.success("Prediction: Highly Likable song ✅")

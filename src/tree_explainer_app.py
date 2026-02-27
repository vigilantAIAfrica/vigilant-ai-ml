import streamlit as st
import joblib
import numpy as np

st.title("Decision Tree Explainer")

model = joblib.load("models/tree_model.pkl")

message = st.text_input("Paste message")

if message:
    length_feature = np.array([[len(message)]])
    pred = model.predict(length_feature)

    st.write("Prediction:", "Scam" if pred[0] == 1 else "Safe")
    st.write("Explanation: Flagged based on message length pattern.")
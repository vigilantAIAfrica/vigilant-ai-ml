import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

st.title("Fraud Data Explorer - Vigilant AI")

try:
    df = pd.read_csv("data/synthetic_african_fraud_data.csv")
except FileNotFoundError:
    st.error("Dataset not found. Please generate data first.")
    st.stop()

st.subheader("Fraud Ratio")
fig, ax = plt.subplots()
df["is_fraud"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
st.pyplot(fig)

st.subheader("Common Words")
words = " ".join(df["message"]).split()
st.write(Counter(words).most_common(10))

st.subheader("Upload Your CSV")
uploaded = st.file_uploader("Upload CSV")

if uploaded:
    user_df = pd.read_csv(uploaded)
    st.write(user_df.head())
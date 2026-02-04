import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("customer_classification_model_lr.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))  # must exist

st.set_page_config(page_title="Consumer Complaint Classifier", layout="centered")

st.title("📄 Consumer Complaint Classification System")
st.write("Classify customer complaints into product categories")

# Text input
complaint_text = st.text_area("Enter complaint text")

if st.button("Predict"):
    if complaint_text.strip() == "":
        st.warning("Please enter a complaint")
    else:
        text_vec = vectorizer.transform([complaint_text])
        prediction = model.predict(text_vec)[0]
        confidence = max(model.predict_proba(text_vec)[0])

        st.success(f"Predicted Category: **{prediction}**")
        st.info(f"Confidence: **{confidence:.2f}**")

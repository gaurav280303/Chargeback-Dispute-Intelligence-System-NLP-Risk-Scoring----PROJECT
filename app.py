import streamlit as st
import joblib
import pandas as pd

# Load vectorizer
vectorizer = joblib.load("tfidf_vectorizer.joblib")

# Load trained model
model = joblib.load("customer_classification_model_lr.joblib")

st.set_page_config(
    page_title="Consumer Complaint Classification System",
    layout="centered"
)

st.title("📄 Consumer Complaint Classification System")
st.write(
    "This application classifies consumer complaints using a "
    "machine learning model trained on real-world data."
)

complaint_text = st.text_area(
    "Enter consumer complaint narrative:",
    height=200
)

if st.button("Predict Complaint Category"):
    if complaint_text.strip() == "":
        st.warning("Please enter a complaint.")
    else:
        text_vector = vectorizer.transform([complaint_text])
        prediction = model.predict(text_vector)[0]

        if hasattr(model, "predict_proba"):
            confidence = model.predict_proba(text_vector).max()
            st.success(f"**Predicted Category:** {prediction}")
            st.info(f"**Confidence:** {confidence:.2f}")
        else:
            st.success(f"**Predicted Category:** {prediction}")

st.markdown("---")
st.caption("NLP-based Consumer Complaint Classification | Streamlit App")

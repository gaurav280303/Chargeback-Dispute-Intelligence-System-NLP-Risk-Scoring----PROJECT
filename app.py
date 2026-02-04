import streamlit as st
import pickle
import pandas as pd

# --------------------------------------------------
# Load TF-IDF Vectorizer
# --------------------------------------------------
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# --------------------------------------------------
# Load Trained Model (Logistic Regression)
# --------------------------------------------------
with open("customer_classification_model_lr.pkl", "rb") as f:
    model = pickle.load(f)

# --------------------------------------------------
# Streamlit Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Consumer Complaint Classification System",
    layout="centered"
)

st.title("📄 Consumer Complaint Classification System")
st.write(
    "This application classifies consumer complaints into predefined categories "
    "using a machine learning model trained on real-world data."
)

# --------------------------------------------------
# User Input
# --------------------------------------------------
st.subheader("Enter Consumer Complaint Text")

complaint_text = st.text_area(
    "Paste or type the complaint narrative below:",
    height=200
)

# --------------------------------------------------
# Prediction Logic
# --------------------------------------------------
if st.button("Predict Complaint Category"):
    if complaint_text.strip() == "":
        st.warning("Please enter a complaint text before predicting.")
    else:
        # Vectorize input text
        text_vectorized = vectorizer.transform([complaint_text])

        # Predict category
        prediction = model.predict(text_vectorized)[0]

        # Predict confidence (if supported)
        if hasattr(model, "predict_proba"):
            confidence = model.predict_proba(text_vectorized).max()
            st.success(f"**Predicted Category:** {prediction}")
            st.info(f"**Confidence:** {confidence:.2f}")
        else:
            st.success(f"**Predicted Category:** {prediction}")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption(
    "Built as part of an NLP-based Consumer Complaint Classification Project "
    "using Streamlit and Scikit-learn."
)

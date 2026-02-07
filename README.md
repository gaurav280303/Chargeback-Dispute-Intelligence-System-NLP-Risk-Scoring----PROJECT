**# Chargeback-Dispute-Intelligence-System-NLP-Risk-Scoring----PROJECT**

**Project Idea: **

A compact, production-ready system that reads a raw consumer complaint (free-text), predicts the correct operational issue category, and returns a confidence score — so ops teams can route and resolve disputes faster, with less manual work.

**What I built :-**

An end-to-end pipeline that takes real complaint text and produces an operational category for routing.

A lightweight, deployable web interface (Streamlit) for single-text and batch predictions.

Safe, reproducible model artifacts (vectorizer + model) and a clear deployment recipe so the app runs reliably in production.

**Dataset :-**

I trained and validated the system on an authentic consumer-complaint dataset derived from the public complaint archive maintained by the Consumer Financial Protection Bureau.
This dataset contains real customer narratives plus historical issue labels, product metadata, company names and dates — everything needed to simulate a real intake workflow.

**Why this problem matters :-**

Organizations must triage thousands of complaints a day.

Manual tagging is slow and inconsistent.

Automating initial categorization reduces time-to-resolution, improves SLA compliance, and reduces chargeback risk.

**Techniques & tools used**

Exploratory Data Analysis (EDA): text length distribution, class imbalance, duplicate detection, missing-value audit.

Text preprocessing: basic normalization, removal of low-information texts, preserving raw text for audit.

Feature engineering: NLP (NATURAL LANGUAGE PROCESSING)  TF-IDF vectorization (fixed vocabulary size for predictable production behavior).

Models evaluated: Logistic Regression (chosen for deployment) and Support Vector Machine (comparison).

Model persistence: serialized with joblib for robust loading during inference.


**Deployment:-**

lightweight web app built with Streamlit for interactive demonstration.

Runtime libraries: scikit-learn (modeling), pandas/numpy (data), joblib (persistence).

What the app does (user flow)

Paste a complaint narrative (or upload a CSV for batch mode).

The app vectorizes the text using the saved TF-IDF artifact.

The model returns a predicted issue category and a confidence score.

The user can download the enriched CSV (text + predicted label + confidence) for downstream workflows.

Placeholder for live demo link: https://chargeback-dispute-intelligence-system-nlp-risk-scoring----pro.streamlit.app/

Important design choices (and why)

Predict historical “Issue” labels: Although the dataset contains labels, in real operations the label is not available at intake — the model simulates human triage, predicting the label from text at submission time.

Classical models (TF-IDF + LR/SVM) were selected for interpretability, speed, and reliability on small hardware — ideal for submission timelines and regulated environments.

Avoided label leakage: I explicitly removed/controlled any label information that appeared verbatim in the complaint text to prevent artificially perfect scores.

Problems faced & how I solved them

Label leakage (initially produced unrealistic 100% scores): fixed by identifying and removing label tokens and by ensuring the train/test split had no leakage. This turned a false “perfect” model into a realistic, trustworthy system.

Environment / pickle compatibility: loading pickleed sklearn models failed on deployment due to version mismatch. Resolved by:

Re-saving artifacts with joblib, and

Pinning the exact scikit-learn version in requirements.txt.

Colab runtime persistence: saving only the trained artifacts (vectorizer + model) and uploading them to the repo prevented re-running expensive steps on reconnect.

**Key results **

Baseline Logistic Regression performed best for deployment (balanced F1 across major classes).

Confidence scores are probabilistic — the app shows the model’s real uncertainty (this is desirable).

The system focuses on operational usefulness (routing & prioritization), not on exaggerated accuracy.

How to run (developer short guide)

Clone the repo to local machine or GitHub.

Ensure files present: app.py, requirements.txt, tfidf_vectorizer.joblib, customer_classification_model_lr.joblib.

Install dependencies:

pip install -r requirements.txt


Run locally:

streamlit run app.py


Or deploy on Streamlit Cloud by pointing it at the repository root (select app.py).

What to include in your final submission (recommendation)

Notebook with EDA & model experiments (for grading transparency).

The minimal production folder: app.py, requirements.txt, serialized artifacts (.joblib), and README.md.

Screenshots of the Streamlit UI and a short demo video (30–90s) showing single and batch predictions.

**Future improvements (nice-to-have)**

Add top-N suggestions and a manual-correction flow to continuously improve the model.

Integrate a confidence threshold that routes low-confidence cases to humans.

Enrich features with structured metadata (product, company, region) and time-based signals for better triage.

Add explainability (keyword highlights) to show which tokens influenced the prediction.

**A short human note**

This project isn’t just a classifier — it’s an ops accelerator. Think of it as a junior analyst that reads text 24/7, flags urgent cases, and hands off ambiguous ones to human experts. That hybrid model (machine + human) is where real operational value lies.

Attribution & contact

Code, artifacts, and the app are part of this repository.

App demo link: [Add your Streamlit URL here]

Questions / feedback: Gaurav Singh — include contact or LinkedIn in the repo.

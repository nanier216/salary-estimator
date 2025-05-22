import streamlit as st
import pandas as pd
import joblib
import re

@st.cache_data
def load_processed_data():
    return pd.read_parquet("data/processed/job_data.parquet")

@st.cache_resource
def load_model_and_vectorizer():
    model = joblib.load("data/processed/salary_model.joblib")
    vectorizer = joblib.load("data/processed/vectorizer.joblib")
    return model, vectorizer

st.set_page_config(page_title="Job Salary Estimator", layout="wide")
st.title("💼 Job Salary Estimator")

with st.spinner("Loading data and model..."):
    df = load_processed_data()
    model, vectorizer = load_model_and_vectorizer()

# Sidebar with instructions or info
with st.sidebar:
    st.header("How to use")
    st.write(
        """
        - Enter a detailed job description in the text box.
        - Click **Estimate Salary** to see the predicted median salary.
        - Try to be as specific as possible to improve prediction accuracy.
        """
    )
    st.markdown("---")
    st.subheader("Example job description")
    st.write(
        """
        * Software engineer with 5 years experience in Python, machine learning, and cloud computing.
        * Data scientist familiar with SQL, deep learning, and big data tools.
        """
    )

# Use columns to separate input and output nicely
col1, col2 = st.columns([2, 1])

with col1:
    job_description = st.text_area(
        "Enter job description:", 
        height=200,
        placeholder="Describe the job role, skills, experience, technologies, etc."
    )
    st.write("")  # spacer

    if st.button("Estimate Salary"):
        if job_description.strip():
            clean_desc = job_description.lower()
            clean_desc = re.sub(r"\n", " ", clean_desc)
            clean_desc = re.sub(r"[^a-zA-Z0-9 ]", "", clean_desc)
            X = vectorizer.transform([clean_desc])
            prediction = model.predict(X)
            st.success(f"💰 Estimated Median Salary: **${prediction[0]:,.2f}**")
        else:
            st.warning("Please enter a job description.")

with col2:
    st.markdown("### Recent Job Data Sample")
    st.dataframe(df.head(5), use_container_width=True)

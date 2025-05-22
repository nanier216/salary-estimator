
# 💼 Skill-Salary Dashboard

A data-driven dashboard that analyzes the relationship between skills and salaries in various job markets. This project uses machine learning to preprocess job posting data, trains a model to estimate salaries, and provides an interactive dashboard for insights.

---

## 🚀 Project Overview

This application provides insights on how different skills affect salaries across roles, using data science tools and techniques. It's built with:

- **Python** for data processing and modeling
- **scikit-learn** and **pandas** for ML & data handling
- **Streamlit / Flask** for the web app (based on your `app.py`)
- **Docker** for containerization

---

## 📁 Project Structure

```

skill-salary-dashboard/
│
├── data/                  # Raw and processed datasets (ignored in Git)
├── src/                   # Source code for model training and utilities
├── venv/                  # Virtual environment (ignored in Git)
│
├── .gitignore             # Specifies files/folders to ignore in Git
├── Dockerfile             # For containerizing the app
├── app.py                 # Streamlit/Flask dashboard application
├── preprocess\_and\_train.py # Data cleaning and model training pipeline
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## 🔍 Features

- Cleans and preprocesses job postings
- Extracts skill-related insights
- Trains salary prediction models
- Displays dashboard with visualizations

---

## 🧪 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/nanier216/salary-estimator.git
cd salary-estimator
````

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Dashboard

```bash
python app.py  # Or: streamlit run app.py (if using Streamlit)
```

---

## 🐳 Run with Docker

```bash
docker build -t skill-salary-dashboard .
docker run -p 8501:8501 skill-salary-dashboard
```

---

## 📊 Data

* **Not included in the repo** due to size
* Place raw CSV and Parquet files in `data/raw/` and `data/processed/`
* Add these to `.gitignore` to keep your repo clean

---

## 🙅 .gitignore (Important)

Make sure your `.gitignore` includes:

```
venv/
data/*.csv
data/*.parquet
```

---

## 📈 Future Improvements

* Add interactive filtering (by role, location, skills)
* Integrate more job boards
* Improve model accuracy using NLP on job descriptions

---

## 🧠 Credits

Developed by **Nanier216**
Inspired by real-world job market needs and machine learning applications.

---

## 📜 License

[MIT License](LICENSE)


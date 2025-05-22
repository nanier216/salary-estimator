from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib
import os

def train_salary_model(df):
    df = df.dropna(subset=['description_x', 'med_salary_x'])

    X = df['description_x']
    y = df['med_salary_x']

    vectorizer = TfidfVectorizer(max_features=500)
    X_vect = vectorizer.fit_transform(X)

    model = LinearRegression()
    model.fit(X_vect, y)

    joblib.dump(model, 'data/processed/salary_model.joblib')
    joblib.dump(vectorizer, 'data/processed/vectorizer.joblib')
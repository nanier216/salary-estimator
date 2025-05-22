import joblib
import pandas as pd

def predict_salary(title, location, skills):
    model, columns = joblib.load("model.joblib")
    data = pd.DataFrame({"title": [title], "location": [location], "skills_str": [' '.join(skills)]})
    data = pd.get_dummies(data)
    
    # Add missing columns
    for col in columns:
        if col not in data.columns:
            data[col] = 0

    data = data[columns]  # Ensure column order
    return model.predict(data)

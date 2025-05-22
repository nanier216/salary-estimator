import pandas as pd
import os
from your_module import train_salary_model  # If you saved your function in another file, otherwise put function here

def main():
    # Load your dataset here (adjust path & filename)
    df = pd.read_csv('data/raw/your_dataset.csv')

    # Ensure the output directory exists
    os.makedirs('data/processed', exist_ok=True)

    # Train and save the model and vectorizer
    train_salary_model(df)
    print("Model and vectorizer saved successfully.")

if __name__ == "__main__":
    main()

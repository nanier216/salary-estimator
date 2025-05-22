# preprocess_and_train.py

import pandas as pd
from src.data_loader import load_all_data
from src.data_cleaning import clean_text
from src.model_training import train_salary_model


# Load and merge all data
df = load_all_data()

# Make sure the merged data has rows
print("Merged DataFrame shape:", df.shape)

# Clean description
df["cleaned_description"] = df["description_x"].apply(clean_text)

# After saving the processed data, train the model if data is not empty
if not df.empty:
    train_salary_model(df)

# Save to Parquet only if non-empty
if not df.empty:
    df.to_parquet("data/processed/job_data.parquet")
    print("Saved processed data.")
else:
    print("DataFrame is empty! Check your CSV inputs.")

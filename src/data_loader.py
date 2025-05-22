import pandas as pd
import os

def load_all_data():
    base_path = "data/raw"

    postings = pd.read_csv(os.path.join(base_path, "postings.csv"))
    salaries = pd.read_csv(os.path.join(base_path, "salaries.csv"))
    job_skills = pd.read_csv(os.path.join(base_path, "job_skills.csv"))
    skills = pd.read_csv(os.path.join(base_path, "skills.csv"))
    job_industries = pd.read_csv(os.path.join(base_path, "job_industries.csv"))
    industries = pd.read_csv(os.path.join(base_path, "industries.csv"))
    companies = pd.read_csv(os.path.join(base_path, "companies.csv"))
    company_specialities = pd.read_csv(os.path.join(base_path, "company_specialities.csv"))
    company_industries = pd.read_csv(os.path.join(base_path, "company_industries.csv"))
    employee_counts = pd.read_csv(os.path.join(base_path, "employee_counts.csv"))
    benefits = pd.read_csv(os.path.join(base_path, "benefits.csv"))

    # Merge postings with salaries
    df = postings.merge(salaries, on='job_id', how='left')

    # Add industries
    df = df.merge(job_industries.merge(industries, on='industry_id', how='left'), on='job_id', how='left')

    # Add skills
    df = df.merge(job_skills.merge(skills, on='skill_abr', how='left'), on='job_id', how='left')

    # Add company data
    df = df.merge(companies, on='company_id', how='left')

    return df
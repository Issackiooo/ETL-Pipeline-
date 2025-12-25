import pandas as pd

BUCKET = "covid-etl-issackiooo"
RAW_DATA_PATH = f"s3://{BUCKET}/raw/"
PROCESSED_PATH = f"s3://{BUCKET}/processed/"

CSV_File = "covid19_patient_symptoms_diagnosis.csv"

df = pd.read_csv(RAW_DATA_PATH + CSV_File) 


print("Initial shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Normalize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("After cleaning:", df.shape)

# Write analytics-ready Parquet
df.to_parquet(
    PROCESSED_PATH + "covid_symptoms_clean.parquet",
    index=False
)

print("ETL pipeline completed successfully")
# COVID-19 ETL Pipeline on AWS

This project demonstrates an end-to-end ETL pipeline built on AWS to ingest, clean, transform, and analyze COVID-19 patient symptom data sourced from Kaggle. The pipeline stores raw and processed data in Amazon S3, converts data to Parquet format, and enables serverless SQL analytics using Amazon Athena.

## Data Source
Kaggle – COVID-19 Patient Symptoms and Diagnosis Dataset  
https://www.kaggle.com/datasets/miadul/covid-19-patient-symptoms-and-diagnosis-dataset

## Architecture
Kaggle → Local Download → Amazon S3 (raw) → Python ETL → Amazon S3 (processed, Parquet) → Amazon Athena

## Tools and Platforms
- Amazon Web Services (AWS)
  - S3 (data lake storage)
  - IAM (access and security)
  - Athena (serverless SQL queries)
- Python (Pandas, fsspec, s3fs)
- Parquet
- AWS CLI
- VS Code
- GitHub
- Kaggle API

## ETL Summary
- Extracted COVID-19 data from Kaggle and uploaded it to Amazon S3
- Cleaned and transformed the data using Python and Pandas
- Converted CSV data to Parquet for efficient analytics
- Stored processed data in S3 and queried it using Athena

## Athena Table Definition
```sql
CREATE EXTERNAL TABLE covid_symptoms (
  patient_id string,
  age int,
  gender string,
  fever int,
  cough int,
  fatigue int,
  breathing_difficulty int,
  diagnosis string
)
STORED AS PARQUET
LOCATION 's3://covid-etl-issackiooo/processed/';

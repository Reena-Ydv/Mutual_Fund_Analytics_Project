# Data Ingestion Script (Data Summary)

import pandas as pd
import os

raw_path = "data/raw_data"

files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]

print("=" * 80)
print("DATASET SUMMARY")
print("=" * 80)

for file in files:
    file_path = os.path.join(raw_path, file)

    try:
        df = pd.read_csv(file_path)

        print("\n")
        print("=" * 80)
        print(f"File: {file}")
        print("=" * 80)

        print("Shape:", df.shape)

        print("\nColumns:")
        print(list(df.columns))

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}: {e}")

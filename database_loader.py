import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("bluestock_mf.db")

print("Database connected successfully.")

# Load cleaned datasets
fund_df = pd.read_csv("Data/Processed/01_fund_master_cleaned.csv")
nav_df = pd.read_csv("Data/Processed/02_nav_history_cleaned.csv")
aum_df = pd.read_csv("Data/Processed/03_aum_by_fund_house_cleaned.csv")
spdf = pd.read_csv("Data/Processed/07_scheme_performance_cleaned.csv")
tdf = pd.read_csv("Data/Processed/08_investor_transactions_cleaned.csv")

# Load datasets into SQLite staging tables
fund_df.to_sql(
    "stg_fund_master",
    conn,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "stg_nav_history",
    conn,
    if_exists="replace",
    index=False
)

aum_df.to_sql(
    "stg_aum_by_fund_house",
    conn,
    if_exists="replace",
    index=False
)

spdf.to_sql(
    "stg_scheme_performance",
    conn,
    if_exists="replace",
    index=False
)

tdf.to_sql(
    "stg_investor_transactions",
    conn,
    if_exists="replace",
    index=False
)

print("\nAll cleaned datasets loaded successfully.\n")

# Verify row counts
tables = [
    "stg_fund_master",
    "stg_nav_history",
    "stg_aum_by_fund_house",
    "stg_scheme_performance",
    "stg_investor_transactions"
]

cursor = conn.cursor()

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table:<35} {count}")

conn.commit()
conn.close()

print("\nDatabase connection closed.")

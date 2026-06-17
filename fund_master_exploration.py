import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

print("\nTotal Schemes:")
print(df.shape[0])

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Risk Categories:")
print(df["risk_category"].unique())

print("\nPlan Types:")
print(df["plan"].unique())

print("\nAMFI CODE SAMPLE")
print(df[["amfi_code", "scheme_name"]].head(15))
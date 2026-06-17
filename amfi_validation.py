import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Extract unique AMFI codes
fund_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

# Find missing codes
missing_codes = fund_codes - nav_codes

print("=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

print("\nFund Master Codes:", len(fund_codes))
print("NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes from fund_master exist in nav_history")
else:
    print("\n❌ Missing Codes Found:")
    print(missing_codes)
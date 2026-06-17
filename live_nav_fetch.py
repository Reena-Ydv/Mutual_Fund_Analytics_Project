import requests
import pandas as pd

funds = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, amfi_code in funds.items():

    print(f"\nFetching: {fund_name}")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_path = f"data/raw/live_nav_{fund_name}.csv"

    nav_df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")
    print(f"Rows: {len(nav_df)}")

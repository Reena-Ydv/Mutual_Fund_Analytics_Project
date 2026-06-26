# Data Cleaning Report – Portfolio Holdings Dataset

## Dataset Information

* **Dataset Name:** 09_portfolio_holdings.csv
* **Source Folder:** Data/Raw/
* **Processed Output:** Data/Processed/09_portfolio_holdings_cleaned.csv

---

## Objective

The objective of this cleaning process was to prepare the Portfolio Holdings dataset for Exploratory Data Analysis by validating data quality, standardizing data types, and ensuring the dataset is ready for portfolio and sector-level analysis.

---

## Dataset Overview

| Attribute      |            Value |
| -------------- | ---------------: |
| Records        |              322 |
| Columns        |                8 |
| Portfolio Date | 31 December 2025 |

---

## Data Quality Assessment

### Missing Values

| Column            | Missing Values | Observation |
| ----------------- | -------------: | ----------- |
| amfi_code         |              0 | No issues   |
| stock_symbol      |              0 | No issues   |
| stock_name        |              0 | No issues   |
| sector            |              0 | No issues   |
| weight_pct        |              0 | No issues   |
| market_value_cr   |              0 | No issues   |
| current_price_inr |              0 | No issues   |
| portfolio_date    |              0 | No issues   |

---

## Duplicate Records

* Duplicate Rows Found: **0**
* No duplicate removal was required.

---

## Data Type Corrections

| Column         | Original Type | Final Type |
| -------------- | ------------- | ---------- |
| portfolio_date | Object        | Datetime   |

All remaining columns already contained appropriate numeric and categorical data types.

---

## Cleaning Operations Performed

1. Converted the **portfolio_date** column to datetime format.
2. Sorted the dataset by AMFI code and portfolio weight.
3. Verified duplicate records.
4. Verified missing values.
5. Exported the cleaned dataset to the Processed folder.

---

## Anomalies Identified

* No data quality anomalies were detected.
* The dataset required only data type standardization for the **portfolio_date** column.

---

## Final Validation

* Dataset successfully cleaned.
* No duplicate records remain.
* No missing values detected.
* Dataset is ready for sector allocation, portfolio composition, and holdings analysis.
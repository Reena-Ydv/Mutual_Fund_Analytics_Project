# Data Cleaning Report – Industry Folio Count Dataset

## Dataset Information

* **Dataset Name:** 06_industry_folio_count.csv
* **Source Folder:** Data/Raw/
* **Processed Output:** Data/Processed/06_industry_folio_count_cleaned.csv

---

## Objective

The objective of this cleaning process was to prepare the Industry Folio Count dataset for Exploratory Data Analysis by validating data quality, standardizing data types, and ensuring the dataset is analysis-ready.

---

## Dataset Overview

| Attribute  |                        Value |
| ---------- | ---------------------------: |
| Records    |                           21 |
| Columns    |                            6 |
| Date Range | January 2022 – December 2025 |

---

## Data Quality Assessment

### Missing Values

| Column              | Missing Values | Observation |
| ------------------- | -------------: | ----------- |
| month               |              0 | No issues   |
| total_folios_crore  |              0 | No issues   |
| equity_folios_crore |              0 | No issues   |
| debt_folios_crore   |              0 | No issues   |
| hybrid_folios_crore |              0 | No issues   |
| others_folios_crore |              0 | No issues   |

---

## Duplicate Records

* Duplicate Rows Found: **0**
* No duplicate removal was required.

---

## Data Type Corrections

| Column | Original Type | Final Type |
| ------ | ------------- | ---------- |
| month  | Object        | Datetime   |

All remaining columns already had appropriate numeric data types.

---

## Cleaning Operations Performed

1. Converted the **month** column to datetime format.
2. Sorted the dataset chronologically.
3. Verified duplicate records.
4. Verified missing values.
5. Exported the cleaned dataset to the Processed folder.

---

## Anomalies Identified

* No data quality anomalies were detected.
* Only the `month` column required data type standardization.

---

## Final Validation

* Dataset successfully cleaned.
* No duplicate records remain.
* No missing values detected.
* Dataset is ready for Exploratory Data Analysis.

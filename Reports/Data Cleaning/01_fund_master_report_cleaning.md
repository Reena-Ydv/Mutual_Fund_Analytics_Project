# Data Cleaning Report – Fund Master Dataset

## Dataset Information

* **Dataset Name:** 01_fund_master.csv
* **Source Folder:** Data/Raw/
* **Processed Output:** Data/Processed/01_fund_master_cleaned.csv

---

## Objective

The objective of this cleaning process was to prepare the Fund Master dataset for downstream SQL database design, Exploratory Data Analysis, and dashboard development by validating data quality and ensuring consistency across all scheme records.

---

## Dataset Overview

| Attribute | Value |
| --------- | ----: |
| Records   |    40 |
| Columns   |    15 |

---

## Data Quality Assessment

### Missing Values

No missing values were identified in any column.

### Duplicate Records

* Duplicate Rows Found: **0**
* No duplicate removal was required.

---

## Data Type Corrections

The dataset already contained appropriate data types. No data type conversions were required.

---

## Cleaning Operations Performed

1. Verified dataset structure and column names.
2. Checked for missing values.
3. Checked for duplicate records.
4. Validated AMFI codes for uniqueness.
5. Confirmed categorical fields such as fund house, category, plan, and risk category were consistent.
6. Exported the validated dataset to the Processed folder.

---

## Anomalies Identified

* No data quality anomalies were detected.
* The dataset was complete and required only validation before further analysis.

---

## Final Validation

* Dataset successfully validated.
* No duplicate records remain.
* No missing values detected.
* Dataset is ready for SQL database design and Exploratory Data Analysis.

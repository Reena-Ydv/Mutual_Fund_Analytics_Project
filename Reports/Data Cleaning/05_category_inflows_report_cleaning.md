# Data Cleaning Report – Category Inflows Dataset

## Dataset Information

* **Dataset Name:** 05_category_inflows.csv
* **Source Folder:** Data/Raw/
* **Processed Output:** Data/Processed/05_category_inflows_cleaned.csv

---

## Objective

The objective of this cleaning process was to prepare the Category Inflows dataset for Exploratory Data Analysis by validating data quality, correcting data types, and ensuring the dataset is ready for visualization and analysis.

---

## Dataset Overview

| Attribute  |                   Value |
| ---------- | ----------------------: |
| Records    |                     144 |
| Columns    |                       3 |
| Date Range | April 2024 – March 2025 |

---

## Data Quality Assessment

### Missing Values

| Column           | Missing Values | Observation |
| ---------------- | -------------: | ----------- |
| month            |              0 | No issues   |
| category         |              0 | No issues   |
| net_inflow_crore |              0 | No issues   |

---

## Duplicate Records

* Duplicate Rows Found: **0**
* No duplicate removal was required.

---

## Data Type Corrections

| Column | Original Type | Final Type |
| ------ | ------------- | ---------- |
| month  | Object        | Datetime   |

All remaining columns already contained appropriate data types.

---

## Cleaning Operations Performed

1. Converted the **month** column to datetime format.
2. Sorted records by month and category.
3. Verified duplicate records.
4. Verified missing values.
5. Exported the cleaned dataset to the Processed folder.

---

## Anomalies Identified

* No data quality anomalies were detected.
* The dataset required only data type standardization for the **month** column.

---

## Final Validation

* Dataset successfully cleaned.
* No duplicate records remain.
* No missing values detected.
* Dataset is ready for Exploratory Data Analysis.

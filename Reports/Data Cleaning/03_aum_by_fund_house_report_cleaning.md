# Data Cleaning Report – AUM by Fund House Dataset

## Dataset Information

* **Dataset Name:** 03_aum_by_fund_house.csv
* **Source Folder:** Data/Raw/
* **Processed Output:** Data/Processed/03_aum_by_fund_house_cleaned.csv

---

## Objective

The objective of this cleaning process was to prepare the Assets Under Management (AUM) dataset for trend analysis by validating data quality, standardizing date formats, and ensuring the dataset was suitable for visualization and reporting.

---

## Dataset Overview

| Attribute | Value |
| --------- | ----: |
| Records   |    90 |
| Columns   |     5 |

---

## Data Quality Assessment

### Missing Values

No missing values were identified in any column.

### Duplicate Records

* Duplicate Rows Found: **0**
* No duplicate removal was required.

---

## Data Type Corrections

| Column | Original Type | Final Type |
| ------ | ------------- | ---------- |
| date   | Object        | Datetime   |

All remaining columns already contained appropriate numeric data types.

---

## Cleaning Operations Performed

1. Converted the **date** column to datetime format.
2. Sorted records chronologically.
3. Verified duplicate records.
4. Verified missing values.
5. Validated AUM values and fund house names.
6. Exported the cleaned dataset to the Processed folder.

---

## Anomalies Identified

* No data quality anomalies were detected.
* Only the **date** column required data type standardization.

---

## Final Validation

* Dataset successfully cleaned.
* No duplicate records remain.
* No missing values detected.
* Dataset is ready for AUM trend analysis and visualization.

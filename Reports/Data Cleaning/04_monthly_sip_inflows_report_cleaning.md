# Data Cleaning Report – Monthly SIP Inflows Dataset

## Dataset Information

* **Dataset Name:** 04_monthly_sip_inflows.csv
* **Source Folder:** Data/Raw/
* **Processed Output:** Data/Processed/04_monthly_sip_inflows_cleaned.csv

---

## Objective

The objective of this cleaning process was to prepare the Monthly SIP Inflows dataset for Exploratory Data Analysis by validating data quality, correcting data types, and ensuring the dataset is analysis-ready while preserving all business information.

---

## Dataset Overview

| Attribute  |                        Value |
| ---------- | ---------------------------: |
| Records    |                           48 |
| Columns    |                            6 |
| Date Range | January 2022 – December 2025 |

---

## Data Quality Assessment

### Missing Values

| Column                    | Missing Values | Observation                                                                                                       |
| ------------------------- | -------------: | ----------------------------------------------------------------------------------------------------------------- |
| month                     |              0 | No issues                                                                                                         |
| sip_inflow_crore          |              0 | No issues                                                                                                         |
| active_sip_accounts_crore |              0 | No issues                                                                                                         |
| new_sip_accounts_lakh     |              0 | No issues                                                                                                         |
| sip_aum_lakh_crore        |              0 | No issues                                                                                                         |
| yoy_growth_pct            |             12 | Expected for the first year because Year-over-Year growth cannot be computed without data from the previous year. |

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

1. Converted the **month** column from object to datetime format.
2. Sorted the dataset chronologically.
3. Verified duplicate records.
4. Verified missing values.
5. Preserved expected missing values in **yoy_growth_pct**.
6. Exported the cleaned dataset to the Processed folder.

---

## Anomalies Identified

* The **yoy_growth_pct** column contains 12 missing values corresponding to January–December 2022.
* These are expected business-rule values rather than data quality issues because no prior-year observations exist for Year-over-Year calculations.

---

## Final Validation

* Dataset successfully cleaned.
* No duplicate records remain.
* No unexpected missing values were found.
* Dataset is ready for Exploratory Data Analysis and visualization.

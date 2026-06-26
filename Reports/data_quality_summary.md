# Data Quality Assessment Report

# Mutual Fund Analytics Project – Day 1 (Data Ingestion & Validation)

## 1. Introduction

The objective of this phase was to ingest, understand, and validate the datasets provided for the Mutual Fund Analytics Project. A detailed review was conducted on all available datasets to assess their structure, completeness, consistency, and suitability for further analysis. The assessment focused on schema validation, data type verification, identification of missing values, consistency of AMFI scheme codes, and detection of potential data quality issues.

---

## 2. Dataset Inventory

The following datasets were successfully loaded and examined:

| Dataset                      | Description                                                |
| ---------------------------- | ---------------------------------------------------------- |
| 01_fund_master.csv           | Master reference table containing scheme-level information |
| 02_nav_history.csv           | Historical NAV records for mutual fund schemes             |
| 03_aum_by_fund_house.csv     | Assets Under Management by fund house                      |
| 04_monthly_sip_inflows.csv   | Monthly SIP inflow statistics                              |
| 05_category_inflows.csv      | Category-wise inflow and outflow information               |
| 06_industry_folio_count.csv  | Industry folio count trends                                |
| 07_scheme_performance.csv    | Performance and risk metrics of schemes                    |
| 08_investor_transactions.csv | Investor transaction records                               |
| 09_portfolio_holdings.csv    | Scheme portfolio holdings data                             |

---

## 3. Dataset-Wise Observations

### Dataset: 01_fund_master.csv

**Records:** 40 rows × 15 columns

#### Important Columns

* amfi_code
* fund_house
* scheme_name
* category
* sub_category
* launch_date
* expense_ratio_pct
* risk_category

#### Observations

* Dataset loaded successfully without structural issues.
* `launch_date` is currently stored as object datatype and should be converted to datetime format during preprocessing.
* AMFI codes appear unique and suitable for use as a primary reference key.
* Categories and sub-categories appear standardized.

#### Identified Issue

| Column      | Issue                                |
| ----------- | ------------------------------------ |
| launch_date | Stored as object instead of datetime |

---

### Dataset: 02_nav_history.csv

**Records:** 46,000 rows × 3 columns

#### Important Columns

* amfi_code
* date
* nav

#### Observations

* Historical NAV information is available for all schemes.
* Dataset has a clean and compact structure.
* Suitable for time-series analysis and return calculations.

#### Identified Issue

| Column | Issue                                |
| ------ | ------------------------------------ |
| date   | Stored as object instead of datetime |

---

### Dataset: 03_aum_by_fund_house.csv

**Records:** 90 rows × 5 columns

#### Important Columns

* date
* fund_house
* aum_lakh_crore
* aum_crore

#### Observations

* Dataset contains quarterly/periodic AUM information.
* No structural anomalies detected.

#### Identified Issue

| Column | Issue                                |
| ------ | ------------------------------------ |
| date   | Stored as object instead of datetime |

---

### Dataset: 04_monthly_sip_inflows.csv

**Records:** 48 rows × 6 columns

#### Important Columns

* month
* sip_inflow_crore
* active_sip_accounts_crore
* yoy_growth_pct

#### Observations

* Dataset provides monthly SIP trend information.
* Year-over-Year growth percentages are available.

#### Identified Issues

| Column         | Issue                                |
| -------------- | ------------------------------------ |
| month          | Stored as object instead of datetime |
| yoy_growth_pct | Contains missing values (NaN)        |

#### Explanation

The missing values observed in `yoy_growth_pct` are expected because year-over-year growth cannot be computed for the earliest periods where no historical comparison data exists.

---

### Dataset: 05_category_inflows.csv

**Records:** 144 rows × 3 columns

#### Important Columns

* month
* category
* net_inflow_crore

#### Identified Issue

| Column | Issue                                |
| ------ | ------------------------------------ |
| month  | Stored as object instead of datetime |

---

### Dataset: 06_industry_folio_count.csv

**Records:** 21 rows × 6 columns

#### Important Columns

* month
* total_folios_crore
* equity_folios_crore
* debt_folios_crore

#### Identified Issue

| Column | Issue                                |
| ------ | ------------------------------------ |
| month  | Stored as object instead of datetime |

---

### Dataset: 07_scheme_performance.csv

**Records:** 40 rows × 19 columns

#### Important Columns

* alpha
* beta
* sharpe_ratio
* sortino_ratio
* std_dev_ann_pct
* max_drawdown_pct
* risk_grade

#### Observations

* Dataset contains advanced risk and performance metrics.
* No missing structural fields were identified during initial inspection.
* Suitable for risk-return analytics and performance benchmarking.

#### Identified Issues

No major anomalies identified.

---

### Dataset: 08_investor_transactions.csv

**Records:** 32,778 rows × 13 columns

#### Important Columns

* investor_id
* transaction_date
* transaction_type
* amount_inr
* annual_income_lakh

#### Observations

* Largest transactional dataset in the project.
* Contains investor demographic and transaction information.

#### Identified Issue

| Column           | Issue                                |
| ---------------- | ------------------------------------ |
| transaction_date | Stored as object instead of datetime |

#### Additional Validation Required

* Duplicate transaction detection
* Outlier analysis for transaction amounts
* Missing value assessment

---

### Dataset: 09_portfolio_holdings.csv

**Records:** 322 rows × 8 columns

#### Important Columns

* stock_symbol
* stock_name
* sector
* weight_pct
* market_value_cr
* portfolio_date

#### Observations

* Portfolio composition data appears consistent.
* Useful for sector exposure and concentration analysis.

#### Identified Issue

| Column         | Issue                                |
| -------------- | ------------------------------------ |
| portfolio_date | Stored as object instead of datetime |

---

## 4. Fund Master Exploration Summary

### Unique Fund Houses Identified

A total of 10 fund houses were identified:

* SBI Mutual Fund
* HDFC Mutual Fund
* ICICI Prudential MF
* Nippon India MF
* Kotak Mahindra MF
* Axis Mutual Fund
* Aditya Birla Sun Life MF
* UTI Mutual Fund
* Mirae Asset MF
* DSP Mutual Fund

### Categories

* Equity
* Debt

### Sub-Categories

* Large Cap
* Mid Cap
* Small Cap
* Flexi Cap
* Value
* ELSS
* Index
* Index/ETF
* Liquid
* Gilt
* Short Duration
* Large & Mid Cap

### Risk Categories

* Low
* Moderate
* Moderately High
* High
* Very High

### Plan Types

* Regular
* Direct

---

## 5. AMFI Code Validation

A validation exercise was conducted between:

* 01_fund_master.csv
* 02_nav_history.csv

The objective was to confirm that every AMFI scheme code present in the master dataset also exists in the NAV history dataset.

### Result

All AMFI codes from the Fund Master dataset were successfully found in the NAV History dataset.

### Conclusion

No scheme mapping inconsistencies were detected.

---

## 6. Overall Assessment

The datasets are structurally sound and suitable for further analysis. No critical data integrity issues were identified during the ingestion stage. The primary preprocessing requirements involve:

1. Date conversion from object to datetime.
2. Handling expected missing values in `yoy_growth_pct`.
3. Validation of duplicate records.
4. Standardization checks for categorical variables.
5. Transaction-level quality checks on investor data.

Overall data quality is assessed as **Good**, and the datasets are ready for preprocessing, exploratory analysis, and dashboard development.

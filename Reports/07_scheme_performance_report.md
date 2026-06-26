# Dataset: 07_scheme_performance.csv

## Objective

The objective of cleaning the scheme performance dataset was to validate the integrity of performance-related metrics before loading the data into the analytical database.

## Cleaning and Validation Steps Performed
Verified that all return-related columns (return_1yr_pct, return_3yr_pct, return_5yr_pct, and benchmark_3yr_pct) were stored as numeric (float64) values.
Checked for missing values across all columns. No missing values were detected.
Analysed the distribution of return percentages to identify unusually high or low values. All observed values were within reasonable ranges for mutual fund performance.
Validated that expense_ratio_pct satisfied the business rule of 0.1%–2.5%. All schemes complied with this requirement.
Confirmed that the dataset was consistent and suitable for database loading without requiring any data modifications.

## Anomalies Observed
No missing values were found.
No non-numeric return values were detected.
No abnormal return percentages were observed.
No expense ratio values outside the acceptable range were identified.

## Result
The dataset successfully passed all validation checks and was saved as:
Data/Processed/07_scheme_performance_cleaned.csv
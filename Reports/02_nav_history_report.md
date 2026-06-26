# Dataset: 02_nav_history.csv

## Objective:
To ensure that historical NAV data is complete, consistent, and suitable for time-series analysis and database loading.

## Cleaning Steps Performed:

Converted the date column from string (object) to datetime64[ns].
Sorted the dataset by amfi_code and date to maintain chronological order for each mutual fund scheme.
Checked for missing NAV values. No missing values were found; therefore, forward-filling was not required.
Checked for duplicate records. No duplicate rows were detected.
Validated that all NAV values were greater than zero. The validation passed successfully.

## Anomalies Observed:

A maximum NAV value of 4268.5497 was identified. This was reviewed and retained, as such values are valid for long-established growth mutual funds.
No missing values, duplicate records, or invalid NAV values were detected.

## Result:
The dataset passed all validation checks and was saved as 02_nav_history_cleaned.csv for subsequent database loading and analysis.
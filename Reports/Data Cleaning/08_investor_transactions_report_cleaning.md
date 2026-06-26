# Dataset: 08_investor_transactions.csv

## Objective:
To validate and standardize investor transaction records for accurate transaction analysis and database loading.

## Cleaning Steps Performed
Converted the transaction_date column from object to datetime64[ns].
Verified that the transaction_type column contained only the standardized categories: SIP, Lumpsum, and Redemption.
Validated that all transaction amounts (amount_inr) were greater than zero.
Verified that the kyc_status column contained only valid enumeration values (Verified and Pending).
Checked for missing values across all columns. No missing values were found.

## Anomalies Observed
No missing values were detected.
No invalid transaction types were found.
No invalid transaction amounts (≤ 0) were detected.
No unexpected KYC status values were present.

## Result
The dataset passed all validation checks and was saved as:
Data/Processed/08_investor_transactions_cleaned.csv
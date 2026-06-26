# Query 8: Transaction Type Distribution

## Objective

Analyse the distribution of transactions based on transaction type.

## Business Importance

Helps understand investor preferences for SIP, Lumpsum, and Redemption transactions.

## SQL Used

```sql
SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM stg_investor_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;
```

## Results

transaction_type	total_transactions	total_amount
SIP	                19716           	217233491.0
Lumpsum	            8095            	2059821448.0
Redemption	        4967    	        1244525491.0
...                 ...                 ...

## Observation

The query summarizes transaction counts and investment amounts by transaction type.

## Conclusion

The analysis highlights the most preferred investment mode among investors.
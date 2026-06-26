# Query 4: Transactions by State

## Objective

The objective of this query is to analyze the distribution of mutual fund transactions across different states in India. It helps identify regions with the highest investor participation and transaction activity.

## Business Importance

Understanding the geographical distribution of transactions enables Asset Management Companies (AMCs) to identify high-performing markets, target underperforming regions, and plan region-specific marketing and customer acquisition strategies.

## SQL Used

```sql
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM stg_investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;
```

## Results

state	        total_transactions   total_transactions_amount
Punjab	        2965	            315780459.0
Madhya Pradesh	2931	            308312493.0
Tamil Nadu	    2806	            315177237.0
Gujarat	        2780	            298358940.0
...             ...                 ...

## Observation

The query summarizes both the total number of transactions and the total investment amount for each state. States with higher transaction counts indicate greater investor participation, while higher transaction amounts highlight regions contributing larger investment volumes.

## Conclusion

The analysis provides valuable insights into regional investment behaviour and helps identify key geographical markets for mutual fund companies.
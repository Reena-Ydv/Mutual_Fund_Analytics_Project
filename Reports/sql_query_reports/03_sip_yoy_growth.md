# Query 3: SIP Year-over-Year (YoY) Growth

## Objective

The objective of this query is to calculate the total amount invested through Systematic Investment Plans (SIPs) for each year. This helps evaluate the yearly growth in SIP investments and understand investor participation over time.

## Business Importance

SIP is one of the most popular investment methods in mutual funds due to its disciplined investment approach. Analysing annual SIP investments enables Asset Management Companies (AMCs) to measure investor confidence, identify growth trends, and assess the increasing adoption of systematic investing.

## SQL Used

```sql
SELECT
    strftime('%Y', transaction_date) AS year,
    ROUND(SUM(amount_inr), 2) AS total_sip_amount
FROM stg_investor_transactions
WHERE transaction_type = 'SIP'
GROUP BY strftime('%Y', transaction_date)
ORDER BY year;
```

## Results

year	total_sip_amount
2024	153233052.0
2025	64000439.0

## Observation

The query summarizes the total SIP investment amount for each year. Comparing annual investment values helps identify whether SIP contributions are increasing, decreasing, or remaining stable over time.

## Conclusion

Year-over-Year SIP analysis provides valuable insights into long-term investor behaviour and the overall growth of systematic investments in the mutual fund industry.
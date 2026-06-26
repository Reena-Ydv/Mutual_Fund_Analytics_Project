# Query 6: Top 10 Performing Funds (5-Year Return)

## Objective

Identify the top 10 mutual fund schemes based on their 5-year returns.

## Business Importance

Helps investors identify consistently high-performing mutual fund schemes for long-term investment decisions.

## SQL Used

```sql
SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM stg_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;
```

## Results

scheme_name	                            fund_house	                return_5yr_pct
ABSL Small Cap Fund - Regular - Growth	Aditya Birla Sun Life MF	23.8
...                                     ...                         ...

## Observation

The query ranks mutual fund schemes according to their 5-year returns, highlighting the best-performing funds.

## Conclusion

The analysis helps investors compare long-term fund performance and identify schemes delivering higher historical returns.
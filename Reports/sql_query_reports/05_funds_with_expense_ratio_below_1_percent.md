# Query 5: Funds with Expense Ratio Less Than 1%

## Objective

The objective of this query is to identify mutual fund schemes with an expense ratio below 1%. Since the expense ratio represents the annual fee charged by Asset Management Companies (AMCs), lower expense ratios can help investors maximize long-term returns.

## Business Importance

Expense ratio is an important factor while selecting mutual funds, especially for long-term investments. Funds with lower expense ratios reduce investment costs and can generate better net returns over time. This analysis helps investors identify cost-efficient mutual fund schemes.

## SQL Used

```sql
SELECT
    scheme_name,
    fund_house,
    category,
    plan,
    expense_ratio_pct
FROM stg_scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;
```

## Results

scheme_name	                                            fund_house	        category	    plan	    expense_ratio_pct
Nippon India Gilt Securities Fund - Regular - Growth	Nippon India MF	    Gilt	        Regular	    0.55
HDFC Short Term Debt Fund - Regular - Growth	        HDFC Mutual Fund	Short Duration	Regular	    0.56
Kotak Liquid Fund - Regular - Growth	                Kotak Mahindra MF	Liquid	        Regular	    0.6
...                                                     ...                 ...             ...         ...

## Observation

The query lists all mutual fund schemes whose expense ratio is less than 1%. Most of these schemes are expected to be Direct Plans, which generally have lower management expenses compared to Regular Plans.

## Conclusion

The analysis highlights cost-efficient mutual fund schemes that may be more attractive to long-term investors seeking to minimize annual investment expenses.
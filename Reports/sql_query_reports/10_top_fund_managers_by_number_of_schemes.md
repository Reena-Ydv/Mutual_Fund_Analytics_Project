# Query 10: Top Fund Managers by Average 5-Year Return

## Objective

Identify fund managers with the highest average 5-year returns.

## Business Importance

Helps evaluate fund manager performance based on long-term scheme returns.

## SQL Used

```sql
SELECT
    fm.fund_manager,
    ROUND(AVG(sp.return_5yr_pct), 2) AS average_return
FROM stg_fund_master fm
JOIN stg_scheme_performance sp
ON fm.amfi_code = sp.amfi_code
GROUP BY fm.fund_manager
ORDER BY average_return DESC;
```

## Results

fund_manager	average_return
Mircea Ciobanu	23.8
Anupam Tiwari	22.62
Samir Rachh	    21.88
R. Srinivasan	21.25
Vinit Sambre	19.8
Jinesh Gopani	18.94
...             ...

## Observation

The query ranks fund managers according to the average 5-year returns of the schemes they manage.

## Conclusion

The analysis helps identify consistently high-performing fund managers.
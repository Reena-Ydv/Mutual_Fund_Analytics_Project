# Query 2: Average NAV per Month

## Objective

The objective of this query is to calculate the average Net Asset Value (NAV) for each month across all mutual fund schemes. This helps identify overall market trends and understand how fund values have changed over time.

## Business Importance

NAV is one of the most important indicators of mutual fund performance. Analysing the monthly average NAV enables investors and fund managers to observe long-term growth patterns, identify market fluctuations, and evaluate the overall performance of mutual fund portfolios.

## SQL Used

```sql
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM stg_nav_history
GROUP BY strftime('%Y-%m', date)
ORDER BY month;
```

## Results

month	average_nav
2022-01	207.06
2022-02	207.72
2022-03	209.69
2022-04	211.83
2022-05	212.73
2022-06	213.86
...     ...

## Observation

The query calculates the average NAV for every month in the dataset. By grouping daily NAV values into monthly averages, it becomes easier to identify overall trends while reducing the impact of day-to-day market fluctuations.

## Conclusion

Monthly average NAV analysis provides a clear view of the overall movement in mutual fund values and can be used to study long-term investment trends and market performance.
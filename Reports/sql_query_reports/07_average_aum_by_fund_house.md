# Query 7: Category-wise Average Returns

## Objective

Calculate the average 5-year return for each mutual fund category.

## Business Importance

Helps compare the long-term performance of different fund categories.

## SQL Used

```sql
SELECT
    category,
    ROUND(AVG(return_5yr_pct), 2) AS average_return
FROM stg_scheme_performance
GROUP BY category
ORDER BY average_return DESC;
```

## Results

category	    average_return
Small Cap	    21.9
Mid Cap	        17.52
Large & Mid Cap	15.68
Flexi Cap	    14.64
...             ...

## Observation

The query compares average returns across mutual fund categories.

## Conclusion

The analysis helps identify categories that have delivered stronger long-term performance.
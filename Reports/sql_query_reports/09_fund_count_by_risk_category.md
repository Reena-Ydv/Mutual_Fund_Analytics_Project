# Query 9: Average Investment Amount by Age Group

## Objective

Calculate the average investment amount across different age groups.

## Business Importance

Helps understand investment behaviour among different investor age groups.

## SQL Used

```sql
SELECT
    age_group,
    ROUND(AVG(amount_inr), 2) AS average_investment
FROM stg_investor_transactions
GROUP BY age_group
ORDER BY average_investment DESC;
```

## Results

age_group	average_investment
18-25	    108144.71
26-35	    107821.45
46-55	    107278.77
36-45	    107003.13
56+	        105613.11

## Observation

The query compares average investment amounts across different age groups.

## Conclusion

The analysis helps identify age groups contributing higher investment amounts.
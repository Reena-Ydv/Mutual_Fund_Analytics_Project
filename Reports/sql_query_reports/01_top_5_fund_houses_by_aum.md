# Query 1: Top 5 Fund Houses by AUM

## Objective

The objective of this query is to identify the top five mutual fund houses based on their highest recorded Assets Under Management (AUM). AUM is one of the most important indicators of the size and market presence of an Asset Management Company (AMC).

## Business Importance

A higher AUM generally reflects greater investor confidence, stronger market reputation, and a larger customer base. Analysing the top fund houses helps investors understand which AMCs dominate the mutual fund industry and provides useful insights for competitive benchmarking and market share analysis.

## SQL Used

```sql
select
    fund_house,
    MAX(aum_crore) AS max_aum_crore
FROM stg_aum_by_fund_house
GROUP BY fund_house
ORDER BY max_aum_crore DESC
LIMIT 5;
```

## Results

fund_house	        max_aum_crore
SBI Mutual Fund	    1250000
ICICI Prudential MF	1074000
HDFC Mutual Fund	930000
Nippon India MF	    700000
Kotak Mahindra MF	580000

## Observation

The analysis shows that **SBI Mutual Fund** manages the highest Assets Under Management (₹12,50,000 crore), making it the market leader in the dataset. **ICICI Prudential Mutual Fund** and **HDFC Mutual Fund** occupy the second and third positions respectively, indicating their strong presence in the Indian mutual fund industry.

The significant difference between the AUM of the top three fund houses and the remaining fund houses highlights the concentration of investor assets among a few leading Asset Management Companies. These organizations are likely to benefit from stronger investor trust, wider product portfolios, and greater operational scale.

## Conclusion

The query successfully identifies the leading mutual fund houses by AUM and provides a quick overview of market leadership. Such analysis can assist investors, analysts, and business stakeholders in understanding industry trends and evaluating the relative strength of different Asset Management Companies.
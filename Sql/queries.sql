-- Query1: top 5 fund houses by maximum AUM in crores
select
    fund_house,
    MAX(aum_crore) AS max_aum_crore
FROM stg_aum_by_fund_house
GROUP BY fund_house
ORDER BY max_aum_crore DESC
LIMIT 5;



---- Query 2: Average NAV per Month

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM stg_nav_history
GROUP BY strftime('%Y-%m', date)
ORDER BY month;



-- Query 3: SIP Year-over-Year (YoY) Growth

SELECT
    strftime('%Y', transaction_date) AS year,
    ROUND(SUM(amount_inr), 2) AS total_sip_amount
FROM stg_investor_transactions
WHERE transaction_type = 'SIP'
GROUP BY strftime('%Y', transaction_date)
ORDER BY year;


-- Query 4: Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM stg_investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;



-- Query 5: Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    fund_house,
    category,
    plan,
    expense_ratio_pct
FROM stg_scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;



-- Query 6: Top 10 Performing Funds (5-Year Return)

SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM stg_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;



-- Query 7: Category-wise Average 5-Year Returns

SELECT
    category,
    ROUND(AVG(return_5yr_pct), 2) AS average_return
FROM stg_scheme_performance
GROUP BY category
ORDER BY average_return DESC;



-- Query 8: Transaction Type Distribution

SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM stg_investor_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;



-- Query 9: Average Investment by Age Group

SELECT
    age_group,
    ROUND(AVG(amount_inr), 2) AS average_investment
FROM stg_investor_transactions
GROUP BY age_group
ORDER BY average_investment DESC;



-- Query 10: Top Fund Managers by Average 5-Year Return

SELECT
    fm.fund_manager,
    ROUND(AVG(sp.return_5yr_pct), 2) AS average_return
FROM stg_fund_master fm
JOIN stg_scheme_performance sp
ON fm.amfi_code = sp.amfi_code
GROUP BY fm.fund_manager
ORDER BY average_return DESC;

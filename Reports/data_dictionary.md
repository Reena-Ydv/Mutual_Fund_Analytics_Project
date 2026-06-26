# Data Dictionary

## Dataset 1: 01_fund_master.csv

| Column             | Data Type | Business Definition                                    |
| ------------------ | --------- | ------------------------------------------------------ |
| amfi_code          | INTEGER   | Unique identifier assigned to each mutual fund scheme. |
| fund_house         | TEXT      | Name of the Asset Management Company (AMC).            |
| scheme_name        | TEXT      | Name of the mutual fund scheme.                        |
| category           | TEXT      | Primary category of the mutual fund.                   |
| sub_category       | TEXT      | Specific category within the primary category.         |
| plan               | TEXT      | Indicates whether the scheme is Direct or Regular.     |
| launch_date        | DATE      | Date on which the scheme was launched.                 |
| benchmark          | TEXT      | Benchmark index used for comparison.                   |
| expense_ratio_pct  | REAL      | Annual expense ratio charged by the AMC.               |
| exit_load_pct      | REAL      | Exit load charged on redemption.                       |
| min_sip_amount     | INTEGER   | Minimum amount required for SIP investment.            |
| min_lumpsum_amount | INTEGER   | Minimum amount required for lump sum investment.       |
| fund_manager       | TEXT      | Fund manager responsible for the scheme.               |
| risk_category      | TEXT      | Risk level assigned to the scheme.                     |
| sebi_category_code | TEXT      | SEBI classification code.                              |



## Dataset 2: 02_nav_history.csv

| Column    | Data Type | Business Definition                         |
| --------- | --------- | ------------------------------------------- |
| amfi_code | INTEGER   | Unique fund identifier.                     |
| date      | DATE      | NAV valuation date.                         |
| nav       | REAL      | Net Asset Value of the scheme on that date. |



## Dataset 3: 03_aum_by_fund_house.csv

| Column         | Data Type | Business Definition                          |
| -------------- | --------- | -------------------------------------------- |
| date           | DATE      | Reporting date for AUM.                      |
| fund_house     | TEXT      | Name of the Asset Management Company.        |
| aum_lakh_crore | REAL      | Assets Under Management in lakh crore.       |
| aum_crore      | INTEGER   | Assets Under Management in crore.            |
| num_schemes    | INTEGER   | Number of schemes managed by the fund house. |



## Dataset 4 : 04_monthly_sip_inflows_cleaned.csv

| Column                    | Data Type | Business Definition                                      |
| ------------------------- | --------- | -------------------------------------------------------- |
| month                     | DATE      | Reporting month for SIP statistics.                      |
| sip_inflow_crore          | INTEGER   | Total monthly SIP inflows in crore rupees.               |
| active_sip_accounts_crore | REAL      | Total active SIP accounts in crore.                      |
| new_sip_accounts_lakh     | REAL      | Number of new SIP accounts registered (in lakh).         |
| sip_aum_lakh_crore        | REAL      | SIP Assets Under Management in lakh crore.               |
| yoy_growth_pct            | REAL      | Year-over-Year percentage growth in monthly SIP inflows. |



## Dataset 5: 05_category_inflows.csv

| Column              | Data Type | Business Definition                                      |
| ------------------- | --------- | -------------------------------------------------------- |
| month               | DATE      | Reporting month for industry folio statistics.           |
| total_folios_crore  | REAL      | Total mutual fund folios across the industry (in crore). |
| equity_folios_crore | REAL      | Number of equity mutual fund folios (in crore).          |
| debt_folios_crore   | REAL      | Number of debt mutual fund folios (in crore).            |
| hybrid_folios_crore | REAL      | Number of hybrid mutual fund folios (in crore).          |
| others_folios_crore | REAL      | Number of folios in other mutual fund categories.        |



## Dataset 6: 06_industry_folio_count.csv

| Column              | Data Type | Business Definition                                      |
| ------------------- | --------- | -------------------------------------------------------- |
| month               | DATE      | Reporting month for industry folio statistics.           |
| total_folios_crore  | REAL      | Total mutual fund folios across the industry (in crore). |
| equity_folios_crore | REAL      | Number of equity mutual fund folios (in crore).          |
| debt_folios_crore   | REAL      | Number of debt mutual fund folios (in crore).            |
| hybrid_folios_crore | REAL      | Number of hybrid mutual fund folios (in crore).          |
| others_folios_crore | REAL      | Number of folios in other mutual fund categories.        |



## Dataset 7: 07_scheme_performance.csv

| Column             | Data Type | Business Definition                   |
| ------------------ | --------- | ------------------------------------- |
| amfi_code          | INTEGER   | Unique mutual fund identifier.        |
| scheme_name        | TEXT      | Name of the mutual fund scheme.       |
| fund_house         | TEXT      | Name of the Asset Management Company. |
| category           | TEXT      | Mutual fund category.                 |
| plan               | TEXT      | Direct or Regular plan.               |
| return_1yr_pct     | REAL      | One-year annualized return.           |
| return_3yr_pct     | REAL      | Three-year annualized return.         |
| return_5yr_pct     | REAL      | Five-year annualized return.          |
| benchmark_3yr_pct  | REAL      | Three-year benchmark return.          |
| alpha              | REAL      | Risk-adjusted excess return.          |
| beta               | REAL      | Measure of market volatility.         |
| sharpe_ratio       | REAL      | Risk-adjusted return measure.         |
| sortino_ratio      | REAL      | Downside risk-adjusted return.        |
| std_dev_ann_pct    | REAL      | Annualized standard deviation.        |
| max_drawdown_pct   | REAL      | Maximum observed loss.                |
| aum_crore          | INTEGER   | Assets Under Management in crore.     |
| expense_ratio_pct  | REAL      | Annual expense ratio.                 |
| morningstar_rating | INTEGER   | Morningstar rating (1–5).             |
| risk_grade         | TEXT      | Overall risk grade.                   |



## Dataset 8: 08_investor_transactions.csv
| Column             | Data Type | Business Definition                   |
| ------------------ | --------- | ------------------------------------- |
| investor_id        | TEXT      | Unique investor identifier.           |
| transaction_date   | DATE      | Date of transaction.                  |
| amfi_code          | INTEGER   | Mutual fund identifier.               |
| transaction_type   | TEXT      | SIP, Lumpsum or Redemption.           |
| amount_inr         | REAL      | Transaction amount in Indian Rupees.  |
| state              | TEXT      | Investor's state.                     |
| city               | TEXT      | Investor's city.                      |
| city_tier          | TEXT      | Classification of the city (T30/B30). |
| age_group          | TEXT      | Investor age group.                   |
| gender             | TEXT      | Investor gender.                      |
| annual_income_lakh | REAL      | Annual income in lakh rupees.         |
| payment_mode       | TEXT      | Mode of payment.                      |
| kyc_status         | TEXT      | Investor KYC verification status.     |



## Dataset 9: 09_portfolio_holdings.csv

| Column            | Data Type | Business Definition                                     |
| ----------------- | --------- | ------------------------------------------------------- |
| amfi_code         | INTEGER   | Unique AMFI code identifying the mutual fund scheme.    |
| stock_symbol      | TEXT      | NSE/BSE stock ticker symbol.                            |
| stock_name        | TEXT      | Name of the company held in the mutual fund portfolio.  |
| sector            | TEXT      | Business sector to which the company belongs.           |
| weight_pct        | REAL      | Percentage weight of the holding in the fund portfolio. |
| market_value_cr   | REAL      | Market value of the holding in crore rupees.            |
| current_price_inr | REAL      | Current market price of the stock in Indian Rupees (₹). |
| portfolio_date    | DATE      | Date on which the portfolio holdings were reported.     |


-- Query 1: Top 5 Funds by AUM
SELECT
    f.scheme_name,
    f.fund_house,
    p.aum_crore
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;


-- Query 2: Average NAV per Month
SELECT
    strftime('%Y', date) AS year,
    strftime('%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY year, month
ORDER BY year, month;


-- Query 3: SIP Year-over-Year Growth
WITH yearly_sip AS (
    SELECT
        strftime('%Y', transaction_date) AS year,
        SUM(amount_inr) AS sip_amount
    FROM fact_transactions
    WHERE transaction_type = 'SIP'
    GROUP BY year
)
SELECT
    year,
    ROUND(sip_amount, 2) AS sip_amount,
    ROUND(
        (sip_amount - LAG(sip_amount) OVER (ORDER BY year))
        * 100.0
        / LAG(sip_amount) OVER (ORDER BY year),
        2
    ) AS yoy_growth_pct
FROM yearly_sip
ORDER BY year;


-- Query 4: Transactions by State
SELECT
    state,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;


-- Query 5: Funds with Expense Ratio Below 1%
SELECT
    f.scheme_name,
    f.fund_house,
    p.expense_ratio_pct
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
WHERE p.expense_ratio_pct < 1
ORDER BY p.expense_ratio_pct ASC;


-- Query 6: Transaction Type Analysis
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_amount,
    ROUND(AVG(amount_inr), 2) AS average_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;


-- Query 7: 3-Year Fund Performance vs Benchmark
SELECT
    f.scheme_name,
    f.fund_house,
    p.return_3yr_pct,
    p.benchmark_3yr_pct,
    ROUND(
        p.return_3yr_pct - p.benchmark_3yr_pct,
        2
    ) AS performance_difference
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
WHERE p.return_3yr_pct > p.benchmark_3yr_pct
ORDER BY performance_difference DESC;


-- Query 8: Transactions by City Tier
SELECT
    city_tier,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount,
    ROUND(AVG(amount_inr), 2) AS average_transaction_amount
FROM fact_transactions
GROUP BY city_tier
ORDER BY average_transaction_amount DESC;


-- Query 9: Fund Distribution by Risk Grade
SELECT
    risk_grade,
    COUNT(*) AS fund_count,
    ROUND(AVG(return_1yr_pct), 2) AS average_1yr_return,
    ROUND(AVG(return_3yr_pct), 2) AS average_3yr_return
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;


-- Query 10: Top 5 Funds by 1-Year Return
SELECT
    f.scheme_name,
    f.fund_house,
    p.return_1yr_pct,
    p.return_3yr_pct,
    p.risk_grade
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
ORDER BY p.return_1yr_pct DESC
LIMIT 5;

-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Fund
SELECT amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- 3. Total Transactions by Type
SELECT transaction_type,
COUNT(*) AS total_transactions
FROM fact_transaction
GROUP BY transaction_type;

-- 4. Total Investment by State
SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transaction
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Top 10 Investors by Investment Amount
SELECT investor_id,
SUM(amount_inr) AS invested_amount
FROM fact_transaction
GROUP BY investor_id
ORDER BY invested_amount DESC
LIMIT 10;

-- 6. Transaction Count by KYC Status
SELECT kyc_status,
COUNT(*) AS total
FROM fact_transaction
GROUP BY kyc_status;

-- 7. Highest Sharpe Ratio Funds
SELECT scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 8. Highest 3-Year Return Funds
SELECT scheme_name,
return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;

-- 9. Average Alpha and Beta
SELECT
AVG(alpha) AS avg_alpha,
AVG(beta) AS avg_beta
FROM fact_performance;

-- 10. Fund Count by Category
SELECT category,
COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category
ORDER BY fund_count DESC;
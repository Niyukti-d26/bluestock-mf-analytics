# Bluestock Mutual Fund Analytics - Data Dictionary

## Dataset: dim_fund

| Column Name | Data Type | Description |
|-------------|------------|-------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | Asset Management Company |
| scheme_name | TEXT | Name of mutual fund scheme |
| category | TEXT | Equity, Debt, Hybrid, etc. |
| sub_category | TEXT | Large Cap, Mid Cap, Small Cap, etc. |
| plan | TEXT | Direct or Regular Plan |
| expense_ratio | REAL | Expense ratio percentage |
| risk_grade | TEXT | Low, Moderate, High, Very High |

---

## Dataset: fact_nav

| Column Name | Data Type | Description |
|-------------|------------|-------------|
| amfi_code | TEXT | Scheme identifier |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## Dataset: fact_transaction

| Column Name | Data Type | Description |
|-------------|------------|-------------|
| investor_id | TEXT | Unique Investor ID |
| transaction_date | DATE | Transaction Date |
| amfi_code | TEXT | Scheme Code |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| city | TEXT | Investor City |
| city_tier | TEXT | T30/B30 Classification |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Investor Gender |
| annual_income_lakh | REAL | Annual Income |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | VERIFIED/PENDING |

---

## Dataset: fact_performance

| Column Name | Data Type | Description |
|-------------|------------|-------------|
| amfi_code | TEXT | Scheme Code |
| scheme_name | TEXT | Scheme Name |
| fund_house | TEXT | AMC Name |
| return_1yr_pct | REAL | 1 Year Return (%) |
| return_3yr_pct | REAL | 3 Year Return (%) |
| return_5yr_pct | REAL | 5 Year Return (%) |
| alpha | REAL | Alpha Metric |
| beta | REAL | Beta Metric |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual Volatility |
| max_drawdown_pct | REAL | Maximum Drawdown |
| aum_crore | REAL | Assets Under Management |
| expense_ratio_pct | REAL | Expense Ratio |
| risk_grade | TEXT | Risk Category |

---

## Data Sources

1. AMFI India
2. mfapi.in
3. NSE India
4. BSE India
5. Bluestock Provided Datasets

---

## Last Updated

Day 2 - Data Cleaning & Database Design
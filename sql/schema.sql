-- DIMENSION TABLES

CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    expense_ratio_pct REAL,
    risk_grade TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER,
    is_weekday INTEGER
);

-- Fact Tables

CREATE TABLE fact_nav (
    amfi_code TEXT,
    nav_date DATE,
    nav REAL,
    daily_return_pct REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
    amfi_code TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    aum_crore REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_portfolio (
    amfi_code TEXT,
    stock_symbol TEXT,
    weight_pct REAL,
    sector TEXT,
    holding_date DATE,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
    fund_house TEXT,
    report_date DATE,
    aum_crore REAL,
    num_schemes INTEGER
);

CREATE TABLE fact_sip_industry (
    report_month DATE,
    sip_inflow_crore REAL,
    sip_accounts_crore REAL
);
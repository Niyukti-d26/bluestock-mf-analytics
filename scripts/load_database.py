import pandas as pd
import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("bluestock_mf.db")
print("Connected to SQLite Database")

# Load CSV Files
fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)
clean_nav = pd.read_csv(
    "data/processed/clean_nav.csv"
)
clean_transaction = pd.read_csv(
    "data/processed/clean_transaction.csv"
)
clean_performance = pd.read_csv(
    "data/processed/clean_performance.csv"
)

# Create Dimension Table
dim_fund = fund_master[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "plan",
        "expense_ratio_pct",
        "risk_category"
    ]
]

dim_fund.to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

clean_nav.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

clean_transaction.to_sql(
    "fact_transaction",
    conn,
    if_exists="replace",
    index=False
)

clean_performance.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully!")

# Verify Row Counts
tables = [
    "dim_fund",
    "fact_nav",
    "fact_transaction",
    "fact_performance"
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) as total FROM {table}",
        conn
    )

    print(
        f"{table}:",
        count["total"][0],
        "rows"
    )

conn.close()

print("\nDatabase created successfully!")
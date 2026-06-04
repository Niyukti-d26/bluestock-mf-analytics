import pandas as pd
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check missing values
print("\nMissing Values:")
print(df[numeric_cols].isnull().sum())

# Negative Sharpe Ratios
negative_sharpe = df[
    df["sharpe_ratio"] < 0
]

print("\nFunds with Negative Sharpe Ratio:")
print(
    negative_sharpe[
        ["scheme_name", "sharpe_ratio"]
    ]
)

# Expense Ratio Validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nFunds with Invalid Expense Ratio:")
print(
    invalid_expense[
        ["scheme_name", "expense_ratio_pct"]
    ]
)

# Remove duplicates
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)
df = df.drop_duplicates()

# Save Clean File
df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)
print("\nClean Shape:", df.shape)

print("\nclean_performance.csv created successfully")
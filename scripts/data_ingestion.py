import pandas as pd
import os

DATA_FOLDER = "data/raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

report = []

print("\nStarting Data Ingestion Process...\n")

for file in files:

    file_path = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 100)
    print(f"Loading Dataset: {file}")
    print("=" * 100)

    try:
        df = pd.read_csv(file_path)

        print(f"\nShape: {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

        report.append({
            "file_name": file,
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": df.isnull().sum().sum()
        })

    except Exception as e:
        print(f"\nError reading {file}")
        print(e)
        
report_df = pd.DataFrame(report)

report_path = "reports/day1_data_quality_report.csv"

report_df.to_csv(report_path, index=False)

print("\n" + "=" * 100)
print("Data Ingestion Completed Successfully")
print("=" * 100)

print("\nSummary Report Saved At:")
print(report_path)

print("\nReport Preview:")
print(report_df)
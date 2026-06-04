import pandas as pd

#loading the data
df=pd.read_csv("data/raw/08_investor_transactions.csv")
print("Original shape: " , df.shape)

#convert and fix the transcation dates
df["transaction_date"]=pd.to_datetime(
    df["transaction_date"],
    format="mixed",
    errors="coerce"
)

#remove invalid entries
df = df.dropna(subset=["transaction_date"])

#standardize transaction types
df["transaction_type"]=(
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)
valid_types=["Sip","Lumpsum","Redemption"]

#amount validation
df=df[df["amount_inr"]>0]

#standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

print("\nKYC Status Distribution:")
print(df["kyc_status"].value_counts())

#remove duplicates
duplicates_before = df.duplicated().sum()
print("\nDuplicate Rows Found:", duplicates_before)
df=df.drop_duplicates()

#final output
print("\nClean shape: ",df.shape)

#saving
df.to_csv("data/processed/clean_transaction.csv",index=False)

print("clean_transactions.csv created successfully")
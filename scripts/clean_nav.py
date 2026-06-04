import pandas as pd
#Loading the data 
df=pd.read_csv("data/raw/02_nav_history.csv")
print("Original Shape: ",df.shape)

# convert date column
df["date"] = pd.to_datetime(
    df["date"],
    format="mixed",
    errors="coerce"
)

# Check for invalid dates
print("Invalid dates:", df["date"].isna().sum())

#sorting data
df=df.sort_values(["amfi_code" , "date"])

#remove duplicates
df=df.drop_duplicates()

# Forward fill NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

#remove invalid entries in NAV
df=df[df["nav"]>0]
print("clean shape:",df.shape)

#saving
df.to_csv("data/processed/clean_nav.csv", index=False)
print("clean_nav.csv created successfully")

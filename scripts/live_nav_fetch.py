import requests
import pandas as pd
import os
import time

os.makedirs("data/raw", exist_ok=True)

funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in funds.items():

    print("\n" + "="*60)
    print(f"Downloading {fund_name}")
    print("="*60)

    try:

        url = f"https://api.mfapi.in/mf/{scheme_code}"

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=20
        )

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("Failed to fetch data")
            continue

        try:
            data = response.json()

        except Exception:
            print("Response is not valid JSON")
            print(response.text[:300])
            continue

        if "data" not in data:
            print("No NAV data found")
            continue

        nav_df = pd.DataFrame(data["data"])

        filename = f"data/raw/{fund_name}_NAV.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved Successfully -> {filename}")
        print(f"Rows Downloaded: {len(nav_df)}")

        time.sleep(1)

    except Exception as e:
        print("Error:")
        print(e)

print("\nAll downloads completed.")
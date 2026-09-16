import requests
import pandas as pd
from pathlib import Path

# Five key mutual fund schemes
schemes = {
    119551: "SBI Bluechip",
    120503: "ICICI Bluechip",
    118632: "Nippon Large Cap",
    119092: "Axis Bluechip",
    120841: "Kotak Bluechip"
}

# Folder where raw data will be saved
output_path = Path("data/raw")
output_path.mkdir(parents=True, exist_ok=True)

# Fetch NAV for each scheme
for scheme_code, scheme_label in schemes.items():

    print(f"\nFetching: {scheme_label} ({scheme_code})")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    meta = data["meta"]
    nav_data = data["data"]

    df = pd.DataFrame(nav_data)

    # Add scheme information
    df["scheme_code"] = scheme_code
    df["scheme_name"] = meta["scheme_name"]
    df["fund_house"] = meta["fund_house"]

    # Save each scheme separately
    file_path = output_path / f"live_nav_{scheme_code}.csv"

    df.to_csv(file_path, index=False)

    print(f"Scheme: {meta['scheme_name']}")
    print(f"Records: {len(df)}")
    print(f"Saved to: {file_path}")

print("\nAll five schemes fetched successfully.")
"""
Fetch live NAV data for selected mutual fund schemes.

The capstone dataset contains historical AMFI codes. The script
validates the MFAPI response before saving live NAV data.
"""

from pathlib import Path
import requests
import pandas as pd


SCHEMES = {
    119551: "SBI Bluechip Fund - Regular Plan - Growth",
    120503: "ICICI Pru Bluechip Fund - Regular - Growth",
    118632: "Nippon India Large Cap Fund - Regular - Growth",
    119092: "Axis Bluechip Fund - Regular - Growth",
    120841: "Kotak Bluechip Fund - Regular - Growth",
}

OUTPUT_PATH = Path("data/raw")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def fetch_nav(scheme_code, expected_name):
    """Fetch NAV data and verify the returned scheme name."""

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()
    meta = data["meta"]
    nav_data = data["data"]

    actual_name = meta["scheme_name"]

    expected_keywords = expected_name.lower().split()

    if not all(
        keyword in actual_name.lower()
        for keyword in expected_keywords[:3]
    ):
        print(
            f"WARNING: MFAPI returned a different scheme for "
            f"{scheme_code}."
        )
        print(f"Expected: {expected_name}")
        print(f"Received: {actual_name}")
        print("Skipping this scheme to avoid incorrect data.\n")
        return

    df = pd.DataFrame(nav_data)

    df["scheme_code"] = scheme_code
    df["scheme_name"] = actual_name
    df["fund_house"] = meta["fund_house"]

    output_file = OUTPUT_PATH / f"live_nav_{scheme_code}.csv"
    df.to_csv(output_file, index=False)

    print(f"Saved {len(df)} records to {output_file}")


def main():
    """Fetch NAV data for all configured schemes."""

    for scheme_code, scheme_name in SCHEMES.items():
        print(f"Fetching {scheme_name} ({scheme_code})...")
        fetch_nav(scheme_code, scheme_name)

    print("Live NAV fetch completed.")


if __name__ == "__main__":
    main()
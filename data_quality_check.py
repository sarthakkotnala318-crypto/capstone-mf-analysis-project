import pandas as pd
from pathlib import Path

# Location of raw data
raw_path = Path("data/raw")

# Load Fund Master
fund_master = pd.read_csv(
    next(raw_path.glob("*01_fund_master.csv"))
)

# Load NAV History
nav_history = pd.read_csv(
    next(raw_path.glob("*02_nav_history.csv"))
)

# Get unique AMFI codes
fund_master_codes = set(fund_master["amfi_code"].unique())
nav_history_codes = set(nav_history["amfi_code"].unique())

# Find codes missing from NAV History
missing_codes = fund_master_codes - nav_history_codes

# Find extra codes in NAV History
extra_codes = nav_history_codes - fund_master_codes

print("AMFI CODE VALIDATION")
print("=" * 50)

print(f"Fund Master AMFI codes: {len(fund_master_codes)}")
print(f"NAV History AMFI codes: {len(nav_history_codes)}")

print("\nCodes in Fund Master but missing from NAV History:")
print(missing_codes)

print("\nCodes in NAV History but not in Fund Master:")
print(extra_codes)

print("\nData Quality Summary:")

if not missing_codes and not extra_codes:
    print("All AMFI codes are consistent between Fund Master and NAV History.")
else:
    print("There are differences between Fund Master and NAV History AMFI codes.")
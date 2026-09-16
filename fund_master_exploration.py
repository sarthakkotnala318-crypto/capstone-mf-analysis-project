import pandas as pd
from pathlib import Path

# Location of raw data
raw_path = Path("data/raw")

# Load Fund Master
fund_master = pd.read_csv(
    next(raw_path.glob("*01_fund_master.csv"))
)

print("FUND MASTER EXPLORATION")
print("=" * 60)

# Unique Fund Houses
print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

# Unique Categories
print("\nUnique Categories:")
print(fund_master["category"].unique())

# Unique Sub-Categories
print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())

# Unique Risk Categories
print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

# AMFI Codes
print("\nAMFI Codes:")
print(fund_master["amfi_code"].unique())

# Counts
print("\nCOUNTS")
print("=" * 60)

print(f"Number of Fund Houses: {fund_master['fund_house'].nunique()}")
print(f"Number of Categories: {fund_master['category'].nunique()}")
print(f"Number of Sub-Categories: {fund_master['sub_category'].nunique()}")
print(f"Number of Risk Categories: {fund_master['risk_category'].nunique()}")
print(f"Number of AMFI Codes: {fund_master['amfi_code'].nunique()}")
import pandas as pd
from pathlib import Path

# Project folder containing the raw CSV files
raw_data_path = Path("data/raw")

# Find all CSV files in the raw data folder
csv_files = list(raw_data_path.glob("*.csv"))

print(f"Total CSV files found: {len(csv_files)}")
print("=" * 60)

# Load and inspect each CSV file
# Change in code
for file in csv_files:

    print(f"\nFile: {file.name}")

    # Load the CSV file
    df = pd.read_csv(file)

    # Print number of rows and columns
    print(f"Shape: {df.shape}")

    # Print column names and data types
    print("\nData Types:")
    print(df.dtypes)

    # Print first 5 rows
    print("\nFirst 5 Rows:")
    print(df.head())

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Check duplicate rows
    print(f"\nDuplicate Rows: {df.duplicated().sum()}")

    print("=" * 60)
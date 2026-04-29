import pandas as pd
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parents[1]

# File paths
raw_file = BASE_DIR / "data" / "raw" / "petroleum_data.csv"
processed_file = BASE_DIR / "data" / "processed" / "clean_petroleum_data.csv"

# Load raw data
df = pd.read_csv(raw_file)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing numeric values with 0
numeric_cols = ["production_barrels", "water_cut", "active_wells", "oil_price"]
df[numeric_cols] = df[numeric_cols].fillna(0)

# Create new useful columns
df["production_per_well"] = df["production_barrels"] / df["active_wells"]
df["estimated_oil_value"] = df["production_barrels"] * df["oil_price"]

# Save cleaned data
df.to_csv(processed_file, index=False)

print("Data transformed successfully!")
print(df.head())
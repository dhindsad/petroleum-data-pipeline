import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

processed_file = BASE_DIR / "data" / "processed" / "clean_petroleum_data.csv"

df = pd.read_csv(processed_file)

print("Running data validation checks...")

# Check 1: Missing values
missing_values = df.isnull().sum()
print("\nMissing values:")
print(missing_values)

# Check 2: Duplicate rows
duplicate_count = df.duplicated().sum()
print("\nDuplicate rows:", duplicate_count)

# Check 3: Negative production values
negative_production = df[df["production_barrels"] < 0]
print("\nNegative production records:", len(negative_production))

# Check 4: Water cut should be between 0 and 1
invalid_water_cut = df[(df["water_cut"] < 0) | (df["water_cut"] > 1)]
print("\nInvalid water cut records:", len(invalid_water_cut))

# Check 5: Active wells should be greater than 0
invalid_wells = df[df["active_wells"] <= 0]
print("\nInvalid active well records:", len(invalid_wells))

if (
    missing_values.sum() == 0
    and duplicate_count == 0
    and len(negative_production) == 0
    and len(invalid_water_cut) == 0
    and len(invalid_wells) == 0
):
    print("\nValidation passed. Data is clean and ready for reporting.")
else:
    print("\nValidation completed. Please review data quality issues above.")
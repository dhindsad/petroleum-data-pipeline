import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

processed_file = BASE_DIR / "data" / "processed" / "clean_petroleum_data.csv"
database_file = BASE_DIR / "outputs" / "petroleum_database.db"
summary_file = BASE_DIR / "outputs" / "summary_report.csv"

# Load cleaned data
df = pd.read_csv(processed_file)

# Save to SQLite database
conn = sqlite3.connect(database_file)
df.to_sql("petroleum_production", conn, if_exists="replace", index=False)

# Create summary report
summary = df.groupby("province").agg({
    "production_barrels": "sum",
    "active_wells": "mean",
    "oil_price": "mean",
    "estimated_oil_value": "sum"
}).reset_index()

summary.to_csv(summary_file, index=False)

conn.close()

print("Data loaded successfully!")
print("Database created:", database_file)
print("Summary report created:", summary_file)
print(summary)
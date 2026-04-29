
import pandas as pd
from pathlib import Path

# Get project root
BASE_DIR = Path(__file__).resolve().parents[1]

# Path to your CSV file
file_path = BASE_DIR / "data" / "raw" / "petroleum_data.csv"

# Load data
df = pd.read_csv(file_path)

# Show data
print("Data loaded successfully!")
print(df.head())


import pandas as pd
import numpy as np

# Load the file
file_path = "/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon.xlsx"
df = pd.read_excel(file_path, sheet_name="wealthsmart_portfolio")  # Replace with actual sheet name

# Corrected risk ranges
risk_ranges = {
    "Low": (0, 3),
    "Moderate": (3.01, 6),
    "High": (6.01, 8),
    "Very High": (8.01, 10)
}

# Function to assign random float within the appropriate range
def assign_risk_level_number(risk_level):
    low, high = risk_ranges.get(risk_level, (np.nan, np.nan))
    return np.round(np.random.uniform(low, high), 2) if not np.isnan(low) else np.nan

# Apply to column
df['risk_level_number'] = df['risk_level'].apply(assign_risk_level_number)

# Save updated file
df.to_excel("/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon_risk_final.xlsx", index=False)

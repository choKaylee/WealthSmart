import pandas as pd

# Load the file
file_path = "/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")  # Update if needed

# Convert to datetime first (if not already)
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors='coerce')
df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')

# Strip time values, keep only date
df['purchase_date'] = df['purchase_date'].dt.date
df['sale_date'] = df['sale_date'].dt.date

# Save cleaned output
df.to_excel("/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon_dates_cleaned.xlsx", index=False)

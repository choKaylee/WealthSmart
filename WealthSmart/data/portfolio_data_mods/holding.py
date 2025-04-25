import pandas as pd

# Load the Excel file
file_path = "/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon.xlsx"
df = pd.read_excel(file_path, sheet_name="wealthsmart_portfolo")

# Convert purchase and sale dates to datetime
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors='coerce')
df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')

# Compute holding duration in days
df['holding_duration'] = (df['sale_date'] - df['purchase_date']).dt.days

# Optional: save the updated file
df.to_excel("/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon_updated.xlsx", index=False)

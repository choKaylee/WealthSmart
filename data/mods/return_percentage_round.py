import pandas as pd

# Load the Excel file
file_path = "/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon.xlsx"
df = pd.read_excel(file_path, sheet_name="wealthsmart_portfolio")  # Update if needed

# Ensure numeric types (in case of string formatting issues)
df['purchase_price'] = pd.to_numeric(df['purchase_price'], errors='coerce')
df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')

# Recalculate return_percentage
df['return_percentage'] = ((df['sale_price'] - df['purchase_price']) / df['purchase_price']) * 100

# Round to 2 decimal places
df['return_percentage'] = df['return_percentage'].round(2)

# Save updated file
df.to_excel("/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon_returns_fixed.xlsx", index=False)

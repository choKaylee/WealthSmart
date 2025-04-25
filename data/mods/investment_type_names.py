import pandas as pd

# Load the file
file_path = "/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")  # Confirmed sheet name

# Apply clearer name mapping
rename_map = {
    "Stocks": "Stocks",
    "Government_Bonds": "Gov Bonds",
    "Corporate_Bonds": "Corp Bonds",
    "Municipal_Bonds": "Muni Bonds",
    "Derivatives": "Derivatives",
    "Alternative Investments": "Alt Investments",
    "Treasury_Securities": "T-Bills",
    "Balanced Mutual Funds": "Balanced Funds",
    "Real Estate Investment Trusts": "REITs",
    "Mutual_Funds": "Mutual Funds",
    "ETFs": "ETFs",
    "Cryptocurrenciess": "Crypto",
    "NFTs": "NFTs",
    "Options": "Options"
}

df['investment_type'] = df['investment_type'].replace(rename_map)

# Save cleaned output
df.to_excel("/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon_names_readable.xlsx", index=False)

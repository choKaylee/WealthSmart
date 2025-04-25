import pandas as pd

# Load the data
file_path = "/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon.xlsx"
df = pd.read_excel(file_path, sheet_name="wealthsmart_portfolo")

# Define risk level mapping
risk_mapping = {
    "Stocks": "High",
    "Government_Bonds": "Low",
    "Corporate_Bonds": "Moderate",
    "Municipal_Bonds": "Moderate",
    "Derivatives": "High",
    "Alternative Investments": "High",
    "Treasury_Securities": "Low",
    "Balanced Mutual Funds": "Moderate",
    "Real Estate Investment Trusts": "High",
    "Mutual_Funds": "Moderate",
    "ETFs": "Moderate",
    "Cryptocurrenciess": "Very High",  # Note: Typo in original column?
    "NFTs": "Very High",
    "Options": "Very High"
}

# Apply risk level mapping
df['risk_level'] = df['investment_type'].map(risk_mapping).fillna(df['risk_level'])

# Optional: Save updated version
df.to_excel("/Users/alexhuynh/Documents/AACUW/wealthsmart_portfolo_jon_risk_updated.xlsx", index=False)

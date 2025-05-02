# train_satisfaction_model.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

# --- Load Data ---
user_df = pd.read_csv("data/synthetic_user_data.csv")
portfolio_df = pd.read_excel("data/portfolio_data.xlsx")

# --- Generate User-Portfolio Combinations ---
rows = []
for _, user in user_df.iterrows():
    for _, port in portfolio_df.iterrows():
        row = {**user.to_dict(), **port.to_dict()}

        # Match scores
        return_match = max(0, 10 - abs(user['expected_return_score'] - port['return_percentage'] / 100))
        risk_match = max(0, 10 - abs(user['risk_tolerance'] - port['risk_level_number']))
        hold_match = max(0, 10 - abs(user['holding_period_response'] - port['holding_duration'] / 365))

        # Weighted satisfaction score
        satisfaction_score = (
            user['factor_weight_return_score'] * return_match +
            user['factor_weight_risk_tolerance'] * risk_match +
            user['factor_weight_holding_period'] * hold_match
        ) / (
            user['factor_weight_return_score'] +
            user['factor_weight_risk_tolerance'] +
            user['factor_weight_holding_period']
        )

        # Final row
        rows.append({
            'user_id': user['user_id'],
            'portfolio_id': port['portfolio_id'],
            'return_match': return_match,
            'risk_match': risk_match,
            'hold_match': hold_match,
            'expected_return_score': user['expected_return_score'],
            'risk_tolerance': user['risk_tolerance'],
            'holding_period_response': user['holding_period_response'],
            'return_percentage': port['return_percentage'],
            'risk_level_number': port['risk_level_number'],
            'holding_duration': port['holding_duration'],
            'satisfaction_score': satisfaction_score,
            'is_satisfied': int(satisfaction_score >= 7)
        })

# --- Create Merged DataFrame ---
merged_df = pd.DataFrame(rows)
merged_df.to_csv("user_portfolio_merged.csv", index=False)

# --- Prepare Training Data ---
X = merged_df[[
    'return_match', 'risk_match', 'hold_match',
    'expected_return_score', 'risk_tolerance', 'holding_period_response',
    'return_percentage', 'risk_level_number', 'holding_duration']]

y_score = merged_df['satisfaction_score']
y_class = merged_df['is_satisfied']

# --- Train/Test Split ---
X_train, X_test, y_train_score, y_test_score = train_test_split(X, y_score, test_size=0.2, random_state=42)
_, _, y_train_class, y_test_class = train_test_split(X, y_class, test_size=0.2, random_state=42)

# --- Train Models ---
lr_model = LinearRegression().fit(X_train, y_train_score)
log_model = LogisticRegression().fit(X_train, y_train_class)

# --- Save models if needed (optional) ---
# from joblib import dump
# dump(lr_model, "linear_regression_model.joblib")
# dump(log_model, "logistic_regression_model.joblib")

print("Models trained successfully. Merged data and features ready.")

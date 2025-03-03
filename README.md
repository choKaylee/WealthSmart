## Sample Input Data (JSON Format)

Below is the sample input data in JSON format, representing different users' investment goals, risk tolerance, product preferences, and more.

```json
[
    {
      "user_id": 1,
      "investment_goal_weights": {
        "long_term_growth": 0.40,
        "stable_income": 0.10,
        "balanced_approach": 0.40,
        "high_risk_high_reward": 0.05,
        "short_term_trading": 0.05
      },
      "risk_tolerance": 7.50,
      "holding_period": {
        "response": 6.67,
        "reaction_strength": 7.00
      },
      "expected_return_score": 8.50,
      "product_preference": {
        "equities": 40,
        "government_bonds": 20,
        "corporate_bonds": 15,
        "municipal_bonds": 5,
        "savings_bonds": 5,
        "derivatives": 10,
        "alternative_investments": 5
      },
      "factor_weights": {
        "investment_goals": 25,
        "risk_tolerance": 20,
        "holding_period": 15,
        "return_score": 15,
        "product_preference": 15,
        "allocation_strength": 10
      }
    },
    {
      "user_id": 2,
      "investment_goal_weights": {
        "long_term_growth": 0.70,
        "stable_income": 0.10,
        "balanced_approach": 0.10,
        "high_risk_high_reward": 0.05,
        "short_term_trading": 0.05
      },
      "risk_tolerance": 6.25,
      "holding_period": {
        "response": 10.00,
        "reaction_strength": 8.50
      },
      "expected_return_score": 7.25,
      "product_preference": {
        "equities": 50,
        "government_bonds": 10,
        "corporate_bonds": 10,
        "municipal_bonds": 5,
        "savings_bonds": 5,
        "derivatives": 10,
        "alternative_investments": 10
      },
      "factor_weights": {
        "investment_goals": 30,
        "risk_tolerance": 20,
        "holding_period": 20,
        "return_score": 10,
        "product_preference": 10,
        "allocation_strength": 10
      }
    },
    {
      "user_id": 3,
      "investment_goal_weights": {
        "long_term_growth": 0.10,
        "stable_income": 0.10,
        "balanced_approach": 0.20,
        "high_risk_high_reward": 0.50,
        "short_term_trading": 0.10
      },
      "risk_tolerance": 8.75,
      "holding_period": {
        "response": 3.33,
        "reaction_strength": 5.00
      },
      "expected_return_score": 9.00,
      "product_preference": {
        "equities": 30,
        "government_bonds": 15,
        "corporate_bonds": 15,
        "municipal_bonds": 10,
        "savings_bonds": 10,
        "derivatives": 15,
        "alternative_investments": 15
      },
      "factor_weights": {
        "investment_goals": 20,
        "risk_tolerance": 25,
        "holding_period": 15,
        "return_score": 20,
        "product_preference": 10,
        "allocation_strength": 10
      }
    }
]

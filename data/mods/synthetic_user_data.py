import csv
import random

def random_dirichlet_exact(n, total=1.0):
    """
    n: we want to generate n random numbers
    total: at the end we want the values to be normalized and sum to 1
    This function creates a list of n random values that sum to given total.
    Used when we generate five investment goal weights.
    """
    nums = [random.random() for _ in range(n)]
    s = sum(nums)
    values = [x/s * total for x in nums]
    values = [round(v, 2) for v in values]
    diff = round(total - sum(values), 2)  # calculate rounding error
    values[0] = round(values[0] + diff, 2)  # adjust first element to resolve error
    return values

def random_allocation(n, total=100):
    """
    n: we want to generate n random numbers
    total: at the end we want the values to be normalized and sum to total
    This function generates a list of n random numbers that sum to total.
    Used when generating product preferences and factor weights.
    """
    nums = [random.random() for _ in range(n)]
    s = sum(nums)
    values = [x/s * total for x in nums]
    values = [round(v, 2) for v in values]
    diff = round(total - sum(values), 2)
    values[0] = round(values[0] + diff, 2)
    return values

fieldnames = [
    "user_id",
    "investment_goal_long_term_growth",
    "investment_goal_stable_income",
    "investment_goal_balanced_approach",
    "investment_goal_high_risk_high_reward",
    "investment_goal_short_term_trading",
    "risk_tolerance",
    "holding_period_response",
    "holding_period_reaction_strength",
    "expected_return_score",
    "product_preference_savings_bonds",
    "product_preference_treasury_securities",
    "product_preference_government_bonds",
    "product_preference_municipal_bonds",
    "product_preference_corporate_bonds",
    "product_preference_balanced_mutual_funds",
    "product_preference_etfs",
    "product_preference_stocks",
    "product_preference_reits",
    "product_preference_alternative_investments",
    "product_preference_derivatives",
    "product_preference_options",
    "product_preference_cryptocurrencies",
    "product_preference_nfts",
    "factor_weight_investment_goals",
    "factor_weight_risk_tolerance",
    "factor_weight_holding_period",
    "factor_weight_return_score",
    "factor_weight_product_preference"
]

with open("synthetic_user_data.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for user_id in range(1, 1001):
        ig_weights = random_dirichlet_exact(5, total=1.0)
        
        risk_tolerance = round(random.uniform(1, 10), 2)
        holding_response = random.choice([1.00, 3.33, 6.67, 10.00])
        holding_reaction = round(random.uniform(1, 10), 2)
        expected_return = round(random.uniform(1, 10), 2)
        
        product_pref = random_allocation(14, total=100)
        
        factor_w = random_allocation(5, total=100)
        
        writer.writerow({
            "user_id": user_id,
            "investment_goal_long_term_growth": ig_weights[0],
            "investment_goal_stable_income": ig_weights[1],
            "investment_goal_balanced_approach": ig_weights[2],
            "investment_goal_high_risk_high_reward": ig_weights[3],
            "investment_goal_short_term_trading": ig_weights[4],
            "risk_tolerance": risk_tolerance,
            "holding_period_response": holding_response,
            "holding_period_reaction_strength": holding_reaction,
            "expected_return_score": expected_return,
            "product_preference_savings_bonds": product_pref[0],
            "product_preference_treasury_securities": product_pref[1],
            "product_preference_government_bonds": product_pref[2],
            "product_preference_municipal_bonds": product_pref[3],
            "product_preference_corporate_bonds": product_pref[4],
            "product_preference_balanced_mutual_funds": product_pref[5],
            "product_preference_etfs": product_pref[6],
            "product_preference_stocks": product_pref[7],
            "product_preference_reits": product_pref[8],
            "product_preference_alternative_investments": product_pref[9],
            "product_preference_derivatives": product_pref[10],
            "product_preference_options": product_pref[11],
            "product_preference_cryptocurrencies": product_pref[12],
            "product_preference_nfts": product_pref[13],
            "factor_weight_investment_goals": factor_w[0],
            "factor_weight_risk_tolerance": factor_w[1],
            "factor_weight_holding_period": factor_w[2],
            "factor_weight_return_score": factor_w[3],
            "factor_weight_product_preference": factor_w[4]
        })

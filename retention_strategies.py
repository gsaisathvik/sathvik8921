
import pandas as pd

def get_retention_strategy(customer_segment):
    strategies = {
        # High Risk Segments
        "High Risk - Auto": "Offer premium discount on auto insurance, personalized follow-up call.",
        "High Risk - Home": "Provide home security system upgrade, loyalty bonus.",
        "High Risk - Life": "Review policy benefits, offer financial planning consultation.",
        "High Risk - Health": "Introduce wellness programs, telemedicine access.",

        # Medium Risk Segments
        "Medium Risk - Auto": "Send targeted email campaign with new auto features, offer multi-policy discount.",
        "Medium Risk - Home": "Suggest home maintenance tips, offer smart home device integration.",
        "Medium Risk - Life": "Provide educational content on life insurance benefits, offer policy review.",
        "Medium Risk - Health": "Share health tips, offer preventive care reminders.",

        # Low Risk Segments (general engagement)
        "Low Risk - Auto": "Newsletter with safe driving tips, annual policy review.",
        "Low Risk - Home": "Seasonal home care guides, community engagement events.",
        "Low Risk - Life": "Financial literacy webinars, client appreciation events.",
        "Low Risk - Health": "Health and fitness challenges, healthy recipe sharing."
    }
    return strategies.get(customer_segment, "General engagement communication.")

def apply_retention_strategies(segmented_data_path='segmented_customers.csv'):
    df = pd.read_csv(segmented_data_path)
    df["recommended_strategy"] = df["customer_segment"].apply(get_retention_strategy)
    return df

if __name__ == '__main__':
    df_with_strategies = apply_retention_strategies()
    df_with_strategies.to_csv('customers_with_strategies.csv', index=False)
    print('Generated customers_with_strategies.csv with recommended retention strategies.')



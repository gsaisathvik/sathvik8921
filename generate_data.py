
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_customer_data(num_customers=1000):
    np.random.seed(42)
    random.seed(42)

    customer_ids = [f'CUST{i:04d}' for i in range(1, num_customers + 1)]
    ages = np.random.randint(20, 70, num_customers)
    genders = np.random.choice(['Male', 'Female'], num_customers)
    regions = np.random.choice(['North', 'South', 'East', 'West'], num_customers)
    policy_types = np.random.choice(['Auto', 'Home', 'Life', 'Health'], num_customers)
    premiums = np.random.randint(500, 5000, num_customers)
    claims_last_year = np.random.randint(0, 5, num_customers)
    satisfaction_scores = np.random.randint(1, 6, num_customers)
    contract_length_months = np.random.randint(12, 60, num_customers)
    customer_since = [datetime.now() - timedelta(days=random.randint(365, 365*10)) for _ in range(num_customers)]

    # Simulate churn based on some factors
    churn_probability = (
        (ages < 30) * 0.15 +  # Younger customers more likely to churn
        (satisfaction_scores < 3) * 0.2 +  # Low satisfaction leads to churn
        (claims_last_year > 2) * 0.1 +  # High claims might lead to churn
        (premiums > 3000) * 0.05 + # High premiums might lead to churn
        (contract_length_months < 24) * 0.1 # Shorter contracts more likely to churn
    )
    churn_probability = np.clip(churn_probability, 0.05, 0.8)
    churn = [1 if random.random() < p else 0 for p in churn_probability]

    data = {
        'customer_id': customer_ids,
        'age': ages,
        'gender': genders,
        'region': regions,
        'policy_type': policy_types,
        'premium': premiums,
        'claims_last_year': claims_last_year,
        'satisfaction_score': satisfaction_scores,
        'contract_length_months': contract_length_months,
        'customer_since': customer_since,
        'churn': churn
    }

    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    df = generate_customer_data()
    df.to_csv('customer_data.csv', index=False)
    print('Generated customer_data.csv with', len(df), 'rows.')



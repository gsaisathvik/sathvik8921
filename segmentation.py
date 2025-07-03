
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

def segment_customers(data_path='customer_data.csv', model_path='churn_model.joblib'):
    df = pd.read_csv(data_path)
    model = joblib.load(model_path)

    # Preprocessing for prediction (similar to training)
    df_processed = df.copy()
    for column in ['gender', 'region', 'policy_type']:
        le = LabelEncoder()
        # Fit and transform on the combined data to ensure all categories are handled
        # In a real system, you'd save and load these encoders
        df_processed[column] = le.fit_transform(df_processed[column])

    df_processed['customer_since'] = pd.to_datetime(df_processed['customer_since'])
    df_processed['years_as_customer'] = (pd.to_datetime('2025-01-01') - df_processed['customer_since']).dt.days / 365.25

    X_predict = df_processed.drop(columns=['customer_since', 'customer_id', 'churn'])

    # Predict churn probability
    df['churn_probability'] = model.predict_proba(X_predict)[:, 1]

    # Segment based on churn probability and policy type
    def assign_churn_risk(prob):
        if prob >= 0.7:
            return 'High Risk'
        elif prob >= 0.4:
            return 'Medium Risk'
        else:
            return 'Low Risk'

    df['churn_risk_segment'] = df['churn_probability'].apply(assign_churn_risk)

    # Combine with policy type for more granular segmentation
    df['customer_segment'] = df['churn_risk_segment'] + ' - ' + df['policy_type']

    return df

if __name__ == '__main__':
    segmented_df = segment_customers()
    segmented_df.to_csv('segmented_customers.csv', index=False)
    print('Generated segmented_customers.csv with customer segments.')



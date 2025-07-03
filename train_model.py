import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

def train_churn_model(data_path='customer_data.csv', model_path='churn_model.joblib'):
    df = pd.read_csv(data_path)

    # Preprocessing
    # Convert categorical features to numerical using Label Encoding
    for column in ['gender', 'region', 'policy_type']:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

    # Convert 'customer_since' to numerical feature (e.g., years as customer)
    df['customer_since'] = pd.to_datetime(df['customer_since'])
    df['years_as_customer'] = (pd.to_datetime('2025-01-01') - df['customer_since']).dt.days / 365.25

    # Drop original 'customer_since' and 'customer_id' columns
    df = df.drop(columns=['customer_since', 'customer_id'])

    X = df.drop('churn', axis=1)
    y = df['churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train RandomForestClassifier model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print('Classification Report:')
    print(classification_report(y_test, y_pred))

    # Save the model
    joblib.dump(model, model_path)
    print(f'Model saved to {model_path}')

if __name__ == '__main__':
    train_churn_model()



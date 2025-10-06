import pandas as pd
from tensorflow.keras.models import load_model
import joblib
import mysql.connector

# Load trained model & scaler ONCE (for performance)
model = load_model("traffic_model.keras", compile=False)
scaler = joblib.load("scaler.save")

# Function to get a MySQL database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='komalvarale@#$',
        database='traffic_db'
    )

# Preprocess live traffic dataframe and scale features
def preprocess_live_data(df):
    if df.empty:
        return None
    df.rename(columns={'junction': 'Junction'}, inplace=True)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['hour'] = df['datetime'].dt.hour
    df['day'] = df['datetime'].dt.day
    df['month'] = df['datetime'].dt.month
    df['weekday'] = df['datetime'].dt.weekday
    df['is_weekend'] = (df['weekday'] >= 5).astype(int)
    print(df.columns.tolist())
    X = df[['Junction', 'hour', 'day', 'month', 'weekday', 'is_weekend']]
    print(X.columns.tolist())
    X_scaled = scaler.transform(X)
    return X_scaled



# Predict vehicle counts using the pretrained model
def predict_vehicles(X_scaled):
    if X_scaled is None:
        return []
    preds = model.predict(X_scaled)
    return preds.flatten()

# Main function
def fetch_and_predict():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM traffic_live ORDER BY datetime DESC LIMIT 20;", conn)

    if df.empty:
        print("No live traffic data available.")
        conn.close()
        return []

    X_scaled = preprocess_live_data(df)
    predictions = predict_vehicles(X_scaled)
    df['predicted_vehicles'] = predictions

    # Save predictions to traffic_predictions table (add id if your table needs it)
    cursor = conn.cursor()
    for index, row in df.iterrows():
       cursor.execute("""
    INSERT INTO traffic_predictions (id, junction, datetime, predicted_vehicles)
    VALUES (%s, %s, %s, %s)
    """, (int(row['id']), int(row['Junction']), row['datetime'], float(row['predicted_vehicles'])))

    conn.commit()
    cursor.close()
    conn.close()

    return df.to_dict(orient='records')

# Safe test run: will not error if table is empty
if __name__ == "__main__":
    results = fetch_and_predict()
    for r in results:
        print(r)

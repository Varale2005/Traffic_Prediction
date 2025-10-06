from flask import Flask, render_template, request
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

app = Flask(__name__)

# Load model and scaler
model = load_model("traffic_model.keras", compile=False)
scaler = joblib.load("scaler.save")

@app.route('/')
def home():
    return render_template('form.html')  

@app.route('/predict', methods=['POST'])
def predict():
  
    junction = int(request.form['junction'])
    hour = int(request.form['hour'])
    day = int(request.form['day'])
    month = int(request.form['month'])

   
    from datetime import datetime
    date = datetime(2025, month, day, hour)
    weekday = date.weekday()
    is_weekend = 1 if weekday >= 5 else 0

   
    input_df = pd.DataFrame([[junction, hour, day, month, weekday, is_weekend]],
                            columns=['Junction', 'hour', 'day', 'month', 'weekday', 'is_weekend'])
    X_scaled = scaler.transform(input_df)
    prediction = model.predict(X_scaled)[0][0]

    rounded_prediction = int(round(prediction))
    
    if hour == 0:
      hour_display = "12:00 AM"
    elif hour == 12:
      hour_display = "12:00 PM"
    elif hour > 12:
      hour_display = f"{hour-12}:00 PM"
    else:
      hour_display = f"{hour}:00 AM"



    return render_template('result.html', prediction= rounded_prediction,
                           junction=junction, hour=hour_display, day=day, month=month)

if __name__ == "__main__":
    app.run(debug=True)




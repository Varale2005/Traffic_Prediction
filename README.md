# Real-Time Traffic Prediction System

A traffic congestion prediction system that uses machine learning and live sensor data to provide real-time traffic forecasts. Built with Python, Flask, MySQL, and TensorFlow/Keras.

---

## Features

- Real-time traffic prediction for multiple road junctions  
- Web interface for user inputs and prediction display  
- Database backend with MySQL for live data storage and prediction results  
- Machine Learning model trained on historical traffic data  

---

## Project Structure
```
├── src/
│ ├── app.py # Main Flask application
│ ├── realtime_predict.py # Real-time prediction script
│ ├── templates/ # HTML files
│ ├── static/ # CSS, JS, and images
│ └── schema.sql # Database schema definition
├── traffic.csv # Sample traffic data
├── traffic_model.keras # Trained ML model
├── scaler.save # Scaler used for input features
├── requirements.txt # Python dependencies
└── README.md # This documentation
 ```


## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
   pip install -r requirements.txt
   Set up MySQL database










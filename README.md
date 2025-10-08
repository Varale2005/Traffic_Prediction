Real-Time Traffic Prediction System

A traffic congestion prediction system that uses machine learning and live sensor data to provide real-time traffic forecasts. Built with Python, Flask, MySQL, and TensorFlow/Keras.

Features:
Real-time traffic prediction for multiple road junctions
Web interface for user inputs and prediction display
Database backend with MySQL for live data storage and prediction results
Machine Learning model trained on historical traffic data


Project Structure

│
├── src/
│   ├── app.py                  # Main Flask application
│   ├── realtime_predict.py     # Real-time prediction script
│   ├── templates/              # HTML files
│   ├── static/                 # CSS, JS and images
│
├── schema.sql                  # Database schema definition
├── traffic.csv                 # Sample traffic data
├── traffic_model.keras         # Trained ML model
├── scaler.save                 # Scaler used for input features
├── requirements.txt            # Python dependencies
└── README.md                   # This documentation



Setup Instructions

Clone the repository
git clone <your_repo_url_here>
cd <your_repository_folder>

Create and activate a virtual environment
python -m venv venv
source venv/bin/activate            # For Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt
Set up MySQL database

Start MySQL on your machine
Create the database and tables using schema.sql:
mysql -u your_mysql_user -p

CREATE DATABASE traffic_db;
USE traffic_db;
SOURCE schema.sql;

Explanation of the Database Schema
traffic_live table stores raw traffic sensor observations:
id: Unique record identifier.
junction: Road junction identifier.
datetime: Timestamp of the observation.
vehicles: Vehicle count measured.
processed: Flag indicating whether this row has been processed by the prediction script.

traffic_predictions table stores predicted traffic volumes:
id: Unique prediction record.
junction: Related junction.
datetime: Timestamp corresponding to prediction.
predicted_vehicles: Predicted number of vehicles by the ML model.

This structure separates raw input data from model output, supporting clean, scalable queries and real-time updates.

Import sample data (optional)
Use traffic.csv or your own data for demo/testing.

Configure database credentials
Edit database connection details in src/app.py or use environment variables.

Run the Flask app
python src/app.py
Open your browser to http://127.0.0.1:5000/ and start predicting traffic!

Usage
Input junction number and date/time details to get predicted vehicle counts.
Predictions are based on saved ML models and scaler.

Notes
Do not commit your database passwords or sensitive data.
You may import sample data from traffic.csv for testing.
The ML model files are pre-trained and saved for inference.


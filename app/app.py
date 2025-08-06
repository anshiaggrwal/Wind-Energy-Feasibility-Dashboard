from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
import os
from datetime import datetime

app = Flask(__name__) #initializing flask

base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'wind_speed_model.pkl')
model = joblib.load(model_path)

def suzlon_s66_power_output(wind_speed):
    if wind_speed < 4:
        return 0
    elif wind_speed < 5:
        return 50
    elif wind_speed < 6:
        return 100
    elif wind_speed < 7:
        return 200
    elif wind_speed < 8:
        return 350
    elif wind_speed < 9:
        return 550
    elif wind_speed < 10:
        return 800
    elif wind_speed < 11:
        return 1000
    elif wind_speed < 12:
        return 1150
    elif wind_speed < 13:
        return 1225
    elif wind_speed < 25:
        return 1250
    else:
        return 0 
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])

def predict():
    try:
        # Get the input values from the form
        station = int(request.form['STATION']) 
        latitude = float(request.form['LATITUDE'])
        longitude = float(request.form['LONGITUDE'])
        elevation = float(request.form['ELEVATION'])
        date_str = request.form['DATE']
        wind_direction_deg = float(request.form['wind_direction_deg'])
        tmp_deg = float(request.form['tmp_deg'])

        dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
        dt = dt.replace(second=0)

        date = pd.to_datetime(date_str)
        hour = date.hour
        month = date.month
        day = date.day
        week_day = date.weekday()
        season = (month % 12 + 3) // 3  # 1: Spring, 2: Summer, 3: Fall, 4: Winter
        temp_wind_interaction = tmp_deg * wind_direction_deg
        hour_season_interaction = hour * season

        features = np.array([[station, latitude, longitude, elevation, wind_direction_deg, tmp_deg, hour, month, day, week_day, season, temp_wind_interaction, hour_season_interaction]])

        speed_prediction = model.predict(features)[0]
        speed_prediction = round(speed_prediction, 2)

        power_generated = suzlon_s66_power_output(speed_prediction)
        print(request.form)
        return render_template('index.html', prediction_text = f"Estimated Wind speed is {speed_prediction} m/s and estimated Power by suzlon_s66 is {power_generated} kW", form_values = request.form)
        
    except Exception as e:
        print(request.form)
        return render_template('index.html', prediction_text = f"Error: {str(e)} Please check your input values", form_values = request.form)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port, debug = True, use_reloader=False)




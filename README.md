# 🌬️ Wind Energy Feasibility Dashboard

This project presents a **Wind Energy Feasibility Dashboard** designed to forecast wind speed and estimate power generation potential based on user-input parameters. It integrates machine learning for wind prediction, a power curve simulation for energy estimation, and an interactive Tableau dashboard for visualization.

## 🔗 Live Demo

🚀 [Click here to visit the deployed site on Render](https://wind-energy-feasibility-dashboard.onrender.com)

📊 [Interactive Tableau Dashboard](https://public.tableau.com/app/profile/anshi.agarwal1902/viz/WindEnergyFeasibilityDasboard/Dashboard1)

---

## 📊 Features

- **Wind Speed Forecasting** using random forest regressor
- **Energy Output Estimation** using discrete power curve (Suzlon S66 turbine)
- **User Input Interface** via Flask + HTML
- **Interactive Dashboard** in Tableau
- **Deployable Web App** hosted on Render

---

## 🔍 Data Acquisition

- **Source**: National Oceanic and Atmospheric Administration (NOAA)
- **Format**: CSV files
- **Attributes**:
  - **Attributes**:
  - `STATION`: Unique identifier for the weather station
  - `NAME`: Descriptive name of the station
  - `LATITUDE`: North-south geographic coordinate
  - `LONGITUDE`: East-west geographic coordinate
  - `ELEVATION`: Altitude above sea level (meters)
  - `DATE`: Timestamp of data collection
  - `SOURCE`: Data provider or origin code
  - `REPORT_TYPE`: Type of meteorological report
  - `CALL_SIGN`: Station call sign identifier
  - `QUALITY_CONTROL`: Data quality flags or codes
  - `MA1`: Additional measurement or metadata field
  - `TMP`: Air temperature
  - `WND`: Wind direction and speed info
- *Note*: Data was manually downloaded, not fetched via API.

---

## 🧹 Data Preprocessing

- Removed irrelevant columns and standardized formats
- Handled missing values with known codes like 9, 99.9, 9999 etc.
- handled outliers
- Converted wind direction and temperature values to numeric
- Final cleaned dataset saved for model training

---

## 🛠️ Feature Engineering

- Extracted useful features:
  - `Hour`, `Month`, `Day`, `Season` from `DATE`
  - Averaged multiple wind speed readings
  - Converted wind direction to degrees if needed
- Correlation analysis performed to select final predictors

---

## 🤖 Model Training

- **Algorithm**: Randon Forest Regressor
- **Libraries**: Scikit-learn
- **Train-Test Split**: 80/20
- **Model Saved As**: `wind_speed_model.pkl`

The model predicts wind speed based on selected weather features. This prediction is then used to estimate energy output.

---

## 🧮 Wind Energy Estimation

- Based on **Suzlon S66 Power Curve** (discrete approximation)
- Maps predicted wind speed to power output (in kW)
- Edge cases (cut-in/cut-out wind speeds) handled appropriately

---

## 🌐 Flask Web Application

- Built with **Flask**
- Loads trained model and power curve function
- Takes user inputs like temperature, pressure, wind direction, etc.
- Returns:
  - Predicted wind speed
  - Estimated power output

---

## 💻 Frontend (HTML + CSS)

- Simple and clean UI (`index.html`)
- Background wind image for aesthetics
- Form to submit user input
- Output displayed below the form with forecast results

---

## 📊 Dashboard (Tableau)

- Created using Tableau Public
- Displays:
  - Wind speed distribution
  - Energy output trends
  - Date-wise wind patterns
- Embedded link to Flask app for direct usage

---

## 🚀 Deployment

- Code hosted on **GitHub**
- App deployed on **Render**
  - Flask port configured via environment variable
  - Requirements specified in `requirements.txt`

---

## 📌 Future Enhancements

- Integrate real-time data fetching from NOAA API
- Include multiple turbine models (S88, Vestas, etc.)
- Add historical energy savings analysis

---

## 📚 References

- NOAA: [https://www.noaa.gov](https://www.noaa.gov)
- Pandas: [https://pandas.pydata.org](https://pandas.pydata.org)
- Scikit-learn: [https://scikit-learn.org](https://scikit-learn.org)
- Flask: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
- Tableau: [https://www.tableau.com](https://www.tableau.com)
- Suzlon S66 documentation (for power curve reference)

---

## 👩‍💻 Author

**Anshi Agarwal**   
[GitHub Profile](https://github.com/anshiaggrwal)

---

## License

This project is protected under **All Rights Reserved**.

You are free to view and explore this repository, but **reuse, reproduction, or modification of any part of the code, content, or design is strictly prohibited** without written permission from the author.

© 2025 Anshi Agarwal




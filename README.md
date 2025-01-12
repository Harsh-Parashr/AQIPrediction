# AQIPrediction
This is a micro project on analysing different pollutants such as PM2.5, PM10, NO,etc. to predict AQI level of Indian City.

# Air Quality Analysis and Prediction in Amravati

## Project Overview
This project focuses on analyzing and predicting air quality in the city of Amravati using historical pollution data. The project employs data visualization and machine learning techniques to explore trends in pollutant concentrations and predict the Air Quality Index (AQI).

## Objectives
- Analyze trends in air pollutant levels (e.g., PM2.5, PM10) over time.
- Visualize the relationship between various pollutants and AQI.
- Build a predictive model to estimate AQI based on pollutant levels.
- Provide actionable insights through clear visualizations and metrics.

## Dataset
The dataset contains air quality data for multiple cities, including:

- **Date**: Date of observation.
- **City**: Name of the city.
- **Pollutants**: PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene.
- **AQI**: Air Quality Index.
- **AQI_Bucket**: AQI category (e.g., Good, Moderate).

**Source**: [https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india?select=city_hour.csv]

## Tools and Libraries
The project is implemented using the following tools:

- **Python**: Programming language.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Data visualization.
- **Scikit-learn**: Machine learning for AQI prediction.

## Methodology

### Data Preprocessing
1. **Filtering Data**: The dataset was filtered to include only records for Amravati.
2. **Date Parsing**: Converted the `Date` column into datetime format for time-series analysis.
3. **Missing Values**: Handled missing data using forward fill.
4. **Feature Selection**: Selected key pollutants as features for AQI prediction.

### Data Analysis and Visualization
- **Trends in PM2.5**: Line plots to observe changes in PM2.5 levels over time.
- **AQI Trends**: Line plots of AQI to understand air quality variations.
- **Correlation Analysis**: Heatmap to identify relationships between pollutants and AQI.

### Predictive Modeling
1. **Model**: Random Forest Regressor was used for AQI prediction.
2. **Training and Testing**:
   - Features: PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene.
   - Target: AQI.
   - Split: 80% training, 20% testing.
3. **Evaluation**:
   - Mean Squared Error (MSE): Evaluated the model's accuracy.

### Enhanced Visualization
- Overlayed real AQI values (line plot) with predicted AQI (scatter plot) over time for clear comparison.

## Results
- **Trend Analysis**: Provided insights into pollutant level changes over time.
- **Prediction Accuracy**: Model achieved a Mean Squared Error (MSE) of X.XX (example).
- **Visual Comparison**: Highlighted alignment between real and predicted AQI values.

## How to Use
1. Clone the repository:
   ```bash
   git clone [https://github.com/Harsh-Parashr/AQIPrediction]
   ```
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
3. Run the script:
   ```bash
   python air_quality_analysis.py
   ```

## Future Work
- Incorporate more advanced models (e.g., XGBoost, LSTM).
- Analyze seasonal variations in pollution.
- Extend analysis to other cities.

## Conclusion
This project demonstrates how data analysis and machine learning can provide valuable insights into air quality trends and predictions. By understanding pollution dynamics, policymakers can implement targeted measures to improve air quality.

## Contact
For any questions or suggestions, feel free to reach out:

- **Name**: [Harsh Parashar]
- **Email**: [h4harshparashar@gmail.com]
- **LinkedIn**: [Harsh Parashar](https://www.linkedin.com/in/harsh-parashar-588363289/)

  



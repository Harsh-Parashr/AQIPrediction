# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# reading csv file
df = pd.read_csv('Amravati.csv')
df

# Sorting dataset as of dates
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df.sort_values(by='Date', inplace=True)

# Plotting different pollutants with respect to dates
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['PM2.5'], label='PM2.5', color='blue')
plt.xlabel('Year-Month format')
plt.ylabel('PM2.5 Levels')
plt.title('PM2.5 Levels Over Time in Amravati')
plt.legend()
plt.show()


plt.figure(figsize=(10,5))
plt.plot(df['Date'],df['AQI'], label='AQI', color='green')
plt.xlabel('Year-Month format')
plt.ylabel('AQI Levels')
plt.title('AQI Levels Over time in Amravati')
plt.legend()
plt.show()


plt.figure(figsize=(10,5))
plt.plot(df['Date'],df['PM10'], label='PM 10', color='red')
plt.xlabel('Year-Month Date format')
plt.ylabel('PM10 levels')
plt.title('PM10 levels over 3 years time')
plt.legend()
plt.show()

# Naming different pollutants in features
features = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
X = df[features]
y = df['AQI']

# Splitting the dataset in train and test data
X_train, X_test, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

import numpy as np

# Add the predicted AQI to the dataset for visualization
df['Predicted_AQI'] = np.nan  
df.loc[X_test.index, 'Predicted_AQI'] = y_pred  

# Plot real vs predicted AQI over time
plt.figure(figsize=(12, 6))
plt.scatter(df['Date'], df['Predicted_AQI'], label='Predicted AQI', color='purple', alpha=1)
plt.plot(df['Date'], df['AQI'], label='Real AQI', color='green', linewidth=1)

plt.xlabel('Date')
plt.ylabel('AQI')
plt.title('Real vs Predicted AQI Over Time in Amravati')
plt.legend()
plt.show()





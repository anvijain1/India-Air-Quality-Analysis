import pandas as pd
import matplotlib.pyplot as plt

#--------------------------------------------------------------
# Load CSV files
#--------------------------------------------------------------
df_delhi = pd.read_csv('csv data/delhi_2018.csv')
df_jpr = pd.read_csv('csv data/jaipur_2018.csv')

#--------------------------------------------------------------
# Convert Date column
#--------------------------------------------------------------
df_delhi['Date'] = pd.to_datetime(df_delhi['Date'])
df_jpr['Date'] = pd.to_datetime(df_jpr['Date'])

#--------------------------------------------------------------
# Extract Month
#--------------------------------------------------------------
df_delhi['Month'] = df_delhi['Date'].dt.month
df_jpr['Month'] = df_jpr['Date'].dt.month

#--------------------------------------------------------------
# Monthly average AQI
#--------------------------------------------------------------
monthly_avg_delhi = (
    df_delhi.groupby('Month')['AQI']
    .mean()
    .reset_index()
)

monthly_avg_ahm = (
    df_jpr.groupby('Month')['AQI']
    .mean()
    .reset_index()
)

#--------------------------------------------------------------
# Plot
#--------------------------------------------------------------
plt.figure(figsize=(10, 5))

plt.plot(
    monthly_avg_delhi['Month'],
    monthly_avg_delhi['AQI'],
    marker='o',
    label='Delhi'
)

plt.plot(
    monthly_avg_ahm['Month'],
    monthly_avg_ahm['AQI'],
    marker='o',
    label='Jaipur'
)

plt.xlabel('Month')
plt.ylabel('Average AQI')
plt.title('Monthly Average AQI Comparison (2018)')
plt.legend()
plt.grid(True)
plt.show()

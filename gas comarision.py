import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#--------------------------------------------------------------
# 1. Load cleaned dataset
#--------------------------------------------------------------
df = pd.read_csv('csv data/city_day_cleaned.csv')

#--------------------------------------------------------------
# 2. Select required columns
#--------------------------------------------------------------
pollutant_cols = [
    'AQI', 'PM2.5', 'PM10', 'NO', 'NO2', 'NOx',
    'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene'
]

#--------------------------------------------------------------
# Keep only available columns (safe check)
#--------------------------------------------------------------
pollutant_cols = [col for col in pollutant_cols if col in df.columns]

df_pollutants = df[pollutant_cols]

#--------------------------------------------------------------
# 3. Drop rows with missing values
#--------------------------------------------------------------
df_pollutants = df_pollutants.dropna()

#--------------------------------------------------------------
# 4. Compute correlation matrix
#--------------------------------------------------------------
corr_matrix = df_pollutants.corr()

#--------------------------------------------------------------
# 5. Plot heatmap
#--------------------------------------------------------------
plt.figure(figsize=(12, 8))

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title('Correlation Heatmap: AQI vs Pollutants')
plt.tight_layout()
plt.show()


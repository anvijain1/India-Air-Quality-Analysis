import pandas as pd
import matplotlib.pyplot as plt 

# Load the cleaned AQI dataset
df = pd.read_csv('csv data/city_day_cleaned.csv')

# Convert Date column and extract year
df['year'] = pd.to_datetime(df['Date']).dt.year

# Filter data for the year 2020
df_year = df[df['year'] == 2020]

# Calculate average AQI for each city in 2020
yearly_avg = df_year.groupby('City')['AQI'].mean().reset_index()

# Plot bar chart of average AQI by city
plt.figure(figsize=(10, 5))

plt.bar(
    yearly_avg['City'],     # X-axis: City names
    yearly_avg['AQI'],      # Y-axis: Average AQI
    color='orange',
    label='2020 AQI'
)

# Chart labels and formatting
plt.xlabel('Cities')
plt.ylabel('Average AQI')
plt.title('Average AQI by City in 2020')
plt.xticks(rotation=45)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

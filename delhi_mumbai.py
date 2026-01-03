import pandas as pd 
import matplotlib.pyplot as plt 

# Load the cleaned AQI dataset
df = pd.read_csv('csv data/city_day_cleaned.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract Month and Year from Date
df['Month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year 

# Filter only Delhi and Mumbai
cities = ['Delhi', 'Mumbai']
df = df[df['City'].isin(cities)]

# Calculate monthly average AQI
# grouped by City, Year, and Month
monthly_avg = (
    df.groupby(['City', 'year', 'Month'])['AQI']
      .mean()
      .reset_index()
)

# Define years to be plotted
years = [2018, 2019, 2020]

# Create subplot canvas
# Rows = Cities, Columns = Years
fig, ax = plt.subplots(
    len(cities),
    len(years),
    figsize=(20, 8),
    sharey=True
)

# Plot monthly AQI trends
for row, city in enumerate(cities):
    for col, year in enumerate(years):

        # Filter data for specific city and year
        data = monthly_avg[
            (monthly_avg['City'] == city) &
            (monthly_avg['year'] == year)
        ]

        # Plot Month vs Average AQI
        ax[row, col].plot(
            data['Month'],
            data['AQI'],
            marker='o'
        )

        # Set subplot title and labels
        ax[row, col].set_title(f'{city} - {year}')
        ax[row, col].set_xlabel('Month')
        ax[row, col].grid(True)

# Set Y-axis labels for cities
ax[0, 0].set_ylabel('Delhi\nAverage AQI')
ax[1, 0].set_ylabel('Mumbai\nAverage AQI')

# Add main title to the figure
fig.suptitle(
    'Monthly Average AQI Comparison: Mumbai vs Delhi (2015–2020)',
    fontsize=16,
    fontweight='bold'
)

# Adjust layout and display plot
plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.show()

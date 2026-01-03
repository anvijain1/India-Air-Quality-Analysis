import pandas as pd 

# Read the original AQI dataset
df = pd.read_csv('csv data/city_day.csv')

# Count how many AQI values are missing (NaN) in the dataset
aqi = df['AQI'].isna().sum()       # 4681 missing AQI values
print("Missing AQI values before cleaning:", aqi)

# Remove rows where AQI value is missing
df_clean = df.dropna(subset=['AQI'])

# Reset index after removing rows to keep it clean and continuous
df_clean = df_clean.reset_index(drop=True)

# Check missing AQI values after cleaning (should be 0)
print("Missing AQI values after cleaning:", df_clean['AQI'].isna().sum())

# Display dataset size before and after cleaning
print("\nOriginal dataset size:", df.shape)
print("Cleaned dataset size:", df_clean.shape)

# Save the cleaned dataset to a new CSV file
df_clean.to_csv('city_day_cleaned.csv', index=False)

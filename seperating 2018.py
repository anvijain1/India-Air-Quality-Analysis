import pandas as pd

# 1. Load cleaned dataset
df = pd.read_csv('csv data\city_day_cleaned.csv')

# 2. Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# 3. Filter year 2018
df_2018 = df[df['Date'].dt.year == 2018]

# 4. Separate city-wise data
delhi_2018 = df_2018[df_2018['City'] == 'Delhi']
jaipur_2018 = df_2018[df_2018['City'] == 'Jaipur']

# 5. Save to CSV files
delhi_2018.to_csv('csv data\delhi_2018.csv', index=False)
jaipur_2018.to_csv('csv data\jaipur_2018.csv', index=False)

# 6. Confirmation
print("CSV files created successfully:")
print("→ delhi_2018.csv")
print("→ jaipur_2018.csv")

import os
import re
import pandas as pd

# Directory that contains all the temperature data files
data_directory = 'temperature_data' 

# Regular expression to match filenames like 'stations_group_YYYY.csv'
file_pattern = r"stations_group_\d{4}\.csv"  

# List all files and filter only CSV files matching the pattern
all_files = os.listdir(data_directory)
csv_files = [file for file in all_files if re.match(file_pattern, file)]

# Combine all DataFrames from the CSV files into one
dfs = []
for file in csv_files:
    file_path = os.path.join(data_directory, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)
print(df_all.head())

# Define seasonal groupings based on months
seasons = {
    'Spring': ['September', 'October', 'November'],
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August']
}

# Function to calculate seasonal average temperatures for each row
def calculate_seasonal_avg(df, seasons):
    seasonal_avg = {}
    for season, months in seasons.items():
        seasonal_avg[season] = df[months].mean(axis=1)  
    return seasonal_avg

# Compute seasonal averages and add them to the DataFrame
seasonal_avg_all = calculate_seasonal_avg(df_all, seasons)
for season, avg_temps in seasonal_avg_all.items():
    df_all[season] = avg_temps
    
# Calculate overall seasonal averages across all years
seasonal_avg_across_years = {season: df_all[season].mean() for season in seasonal_avg_all.keys()}

# Write seasonal average temperatures to a text file
with open('average_temp.txt', 'w') as f:
    for season, avg_temp in seasonal_avg_across_years.items():
        f.write(f"{season} Average Temperature: {avg_temp:.2f}°C\n")

# Calculate temperature range for each station
df_all['Temp_Range'] = df_all.iloc[:, 4:16].max(axis=1) - df_all.iloc[:, 4:16].min(axis=1)

# Find the station(s) with the largest temperature range
largest_temp_range_station = df_all.loc[df_all['Temp_Range'] == df_all['Temp_Range'].max()]

# Write the stations with the largest temperature range to a text file
with open('largest_temp_range_station.txt', 'w') as f:
    f.write("Station(s) with largest temperature range:\n")
    for _, row in largest_temp_range_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Temperature Range: {row['Temp_Range']:.2f}°C)\n")

# Calculate the maximum and minimum temperatures for each station
df_all['Max_Temperature'] = df_all.iloc[:, 4:16].max(axis=1)
df_all['Min_Temperature'] = df_all.iloc[:, 4:16].min(axis=1)

# Identify the warmest and coolest stations
warmest_station = df_all.loc[df_all['Max_Temperature'] == df_all['Max_Temperature'].max()]
coolest_station = df_all.loc[df_all['Min_Temperature'] == df_all['Min_Temperature'].min()]

# Write the warmest and coolest stations to a text file
with open('warmest_and_coolest_station.txt', 'w') as f:
    f.write("Warmest Station(s):\n")
    for _, row in warmest_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Max Temperature: {row['Max_Temperature']:.2f}°C)\n")
    
    f.write("\nCoolest Station(s):\n")
    for _, row in coolest_station.iterrows():
        f.write(f"{row['STATION_NAME']} (Min Temperature: {row['Min_Temperature']:.2f}°C)\n")

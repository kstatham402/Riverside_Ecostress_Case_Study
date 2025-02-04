import pandas as pd
from datetime import datetime


# Read the CSV files
daily_data = pd.read_csv('DailyAvgTempStats.csv')
hot_days_data = pd.read_csv('ConsecutiveHotDays.csv')

# Convert the 'DATE', 'Start', and 'End' columns to datetime objects
daily_data['DATE'] = pd.to_datetime(daily_data['DATE'])
hot_days_data['Start'] = pd.to_datetime(hot_days_data['Start'])
hot_days_data['End'] = pd.to_datetime(hot_days_data['End'])

# Prepare a list to hold the result data
results = []

# Loop through each row in the ConsecutiveHotDays dataframe
for _, hot_day_row in hot_days_data.iterrows():
    start_date = hot_day_row['Start']
    end_date = hot_day_row['End']

    # Filter the daily data for the date range
    date_range = daily_data[(daily_data['DATE'] >= start_date) & (daily_data['DATE'] <= end_date)]

    # Calculate the average for TAVG, TMAX, and TMIN
    avg_tavg = date_range['TAVG'].mean()
    avg_tmax = date_range['TMAX'].mean()
    avg_tmin = date_range['TMIN'].mean()

    # Calculate the duration of the date range
    duration = (end_date - start_date).days + 1  # +1 to include both start and end dates

    # Add the results to the list
    results.append([start_date, end_date, duration, avg_tavg, avg_tmax, avg_tmin])

# Create a new DataFrame from the results
results_df = pd.DataFrame(results, columns = ['Start', 'End', 'Duration', 'Avg_TAVG', 'Avg_TMAX',
                                              'Avg_TMIN'])

# Sort the results first by 'Duration' (descending), then by 'Avg_TAVG' (descending)
results_df = results_df.sort_values(by = ['Duration', 'Avg_TAVG'], ascending = [False, False])

# Write the results to a new CSV file
results_df.to_csv('DateGroupsWithStats.csv', index = False)

print("CSV file 'DateGroupsWithStats.csv' created with the sorted date ranges.")

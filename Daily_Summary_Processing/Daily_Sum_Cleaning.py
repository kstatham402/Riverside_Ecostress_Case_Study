import pandas as pd


def remove_stations_with_missing_data(input_csv, output_csv, threshold = 20):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)

    # Identify the temperature columns
    temp_columns = ['TAVG', 'TMAX', 'TMIN', 'TOBS']

    # Calculate the percentage of missing temperature data for each station
    df['missing_temp_count'] = df[temp_columns].isna().sum(axis = 1)
    df['total_temp_count'] = len(temp_columns)

    # Group by 'STATION' and calculate the sum of missing and total counts
    station_missing_data = df.groupby('STATION').agg(
        missing_temp_count = ('missing_temp_count', 'sum'),
        total_temp_count = ('total_temp_count', 'sum')
    ).reset_index()

    # Calculate the missing percentage
    station_missing_data['missing_percentage'] = (station_missing_data['missing_temp_count'] /
                                                  station_missing_data['total_temp_count']) * 100

    # Optionally, rename the columns if needed (to match your original output structure)
    station_missing_data = station_missing_data[['STATION', 'missing_percentage']]

    # Identify stations to keep (missing percentage < threshold)
    stations_to_keep = station_missing_data[station_missing_data['missing_percentage'] < threshold][
        'STATION']

    # Filter the original dataframe to keep only the desired stations
    filtered_df = df[df['STATION'].isin(stations_to_keep)]

    # Drop helper columns
    filtered_df = filtered_df.drop(columns = ['missing_temp_count', 'total_temp_count'],
                                   errors = 'ignore')

    # Save the filtered data to a new CSV file
    filtered_df.to_csv(output_csv, index = False)
    print(f"Filtered data saved to {output_csv}")


# Example usage
input_csv = input(
    "Enter the path to the input CSV file (default: DailySummaries.csv): ") or "DailySummaries.csv"
output_csv = input(
    "Enter the path to the output CSV file (default: DailySummaries_Cleaned.csv): ") or "DailySummaries_Cleaned.csv"

remove_stations_with_missing_data(input_csv, output_csv, threshold = 20)

import pandas as pd
import os

def process_temperature_data(input_directory):
    # Create an empty list to store dataframes for each file
    all_data = []

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a CSV
        if filename.endswith('.csv'):
            input_file_path = os.path.join(input_directory, filename)
            print(f"Processing file: {input_file_path}")

            # Load the data into a DataFrame
            df = pd.read_csv(input_file_path)

            # Ensure that the 'DATE' column is in datetime format
            df['DATE'] = pd.to_datetime(df['DATE'])

            # Calculate the daily average and max temperature for each station
            daily_stats = df.groupby('DATE').agg(
                avg_station_max=('TMP', 'mean'),   # Average temperature per station
                overall_max=('TMP', 'max')         # Maximum temperature overall
            ).reset_index()

            # Append the results to the list
            all_data.append(daily_stats)

    # Concatenate all the dataframes into one
    combined_data = pd.concat(all_data, ignore_index=True)

    # Remove any duplicate entries by DATE and keep the highest temperature
    final_data = combined_data.groupby('DATE').agg(
        avg_station_max=('avg_station_max', 'mean'),
        overall_max=('overall_max', 'max')
    ).reset_index()

    return final_data

def save_daily_averages(final_data, output_file):
    # Save the final data to a CSV file
    final_data.to_csv(output_file, index=False)
    print(f"Daily averages and max temperatures saved to: {output_file}")

def main():
    # Define the input directory and output file
    input_directory = 'HourlySummaryColumnFiltered'
    output_file = 'DailyTempStats.csv'

    # Process the temperature data and get the daily stats
    final_data = process_temperature_data(input_directory)

    # Save the results to a CSV file
    save_daily_averages(final_data, output_file)

if __name__ == "__main__":
    # Run the main function
    main()

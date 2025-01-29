import os
import pandas as pd


def calculate_daily_avg_temperatures(input_directory: str, output_file: str):
    """
    Reads multiple station CSV files from the given directory, calculates the daily
    average of TAVG, TMAX, TMIN, and TOBS across all stations, and saves the result to a CSV file.

    Parameters:
        input_directory (str): Path to the folder containing station CSV files.
        output_file (str): Path to save the output CSV file.
    """
    all_data = []

    # Read each CSV file in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_directory, filename)
            df = pd.read_csv(file_path, usecols = ["DATE", "TAVG", "TMAX", "TMIN", "TOBS"])
            all_data.append(df)

    # Combine all data into a single DataFrame
    combined_df = pd.concat(all_data, ignore_index = True)

    # Convert DATE column to datetime format
    combined_df["DATE"] = pd.to_datetime(combined_df["DATE"])

    # Group by date and calculate the mean for temperature columns
    daily_avg = combined_df.groupby("DATE").mean(numeric_only = True)

    # Ensure a complete date range from 2020-01-01 to 2023-12-31
    date_range = pd.date_range(start = "2020-01-01", end = "2023-12-31")
    daily_avg = daily_avg.reindex(date_range).reset_index()
    daily_avg.rename(columns = {"index": "DATE"}, inplace = True)

    daily_avg = daily_avg.round(4)

    # Save the result to a CSV file
    daily_avg.to_csv(output_file, index = False)

    print(f"Daily averages saved to {output_file}")


# Example usage
calculate_daily_avg_temperatures("CleanedStationDailySummaries", "DailyAvgTempStats.csv")

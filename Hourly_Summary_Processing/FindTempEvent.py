import pandas as pd

def filter_high_avg_station_max(input_file, output_file, threshold=30):
    """
    Filters out rows where avg_station_max is less than the threshold.

    Parameters:
    - input_file (str): Path to the input CSV file.
    - output_file (str): Path to save the filtered CSV file.
    - threshold (float): The minimum avg_station_max value to keep.

    Returns:
    - None
    """
    # Load the CSV file
    df = pd.read_csv(input_file, parse_dates=["DATE"])

    # Filter the data
    df_filtered = df[df["avg_station_max"] >= threshold]

    # Save the filtered data
    df_filtered.to_csv(output_file, index=False)

    print(f"Filtered data saved to '{output_file}'.")

def main():
    filter_high_avg_station_max("DailyTempStats.csv", "OverThresholdDays.csv")


if __name__ == "__main__":
    # Run the main function
    # 2022-08-31 00:00:00 to 2022-09-07 00:00:00 (8 days)
    # August 31, 2022, to September 7, 2022
    main()

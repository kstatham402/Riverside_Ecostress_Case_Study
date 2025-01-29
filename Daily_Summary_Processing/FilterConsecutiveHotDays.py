import pandas as pd


def find_consecutive_hot_days(input_file: str, output_file: str):
    """
    Reads a CSV file with temperature data, identifies consecutive days where TAVG >= 86,
    and outputs a summary CSV file with date ranges and counts of consecutive hot days.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the output CSV file.
    """
    # Read the CSV file
    df = pd.read_csv(input_file, parse_dates = ["DATE"])

    # Filter rows where TAVG >= 86
    hot_days = df[df["TAVG"] >= 86].reset_index(drop = True)

    # If no hot days, exit early
    if hot_days.empty:
        print("No days with TAVG >= 86 found.")
        return

    # Identify consecutive date ranges
    hot_days["Gap"] = hot_days["DATE"].diff().dt.days.ne(1).cumsum()

    # Group by consecutive sequences
    grouped = hot_days.groupby("Gap")["DATE"]
    results = grouped.agg(Start = "first", End = "last", Count = "count").reset_index(drop = True)

    # Save to CSV
    results.to_csv(output_file, index = False)

    # Find the longest span
    longest_span = results.loc[results["Count"].idxmax()]
    print(
        f"Longest span of TAVG >= 86: {longest_span['Start']} to {longest_span['End']} ({longest_span['Count']} days)")


# Example usage
find_consecutive_hot_days("DailyAvgTempStats.csv", "ConsecutiveHotDays.csv")

import csv
import os

def clean_csv_files(input_dir, output_dir, threshold=80):
    insert_files = 0
    delete_files = 0
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get all the CSV files in the input directory
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    # Loop through each file and process it
    for csv_file in csv_files:
        input_file = os.path.join(input_dir, csv_file)
        valid_data = True

        # Open the current CSV file to check TMAX data
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            total_rows = 0
            valid_TMAX_rows = 0

            # Count total rows and valid TMAX rows
            for row in reader:
                total_rows += 1
                if row['TMAX']:  # Check if TMAX is not empty
                    valid_TMAX_rows += 1

            # Calculate the percentage of rows with valid TMAX data
            TMAX_percentage = (valid_TMAX_rows / total_rows) * 100 if total_rows > 0 else 0

            # If TMAX data is 80% or more, move to the output directory
            if TMAX_percentage >= threshold:
                # Move the file to the CleanedStationDailySummaries directory
                output_file = os.path.join(output_dir, csv_file)
                os.rename(input_file, output_file)
                insert_files += 1
                # print(f"{csv_file} moved to {output_dir}.")
            else:
                delete_files += 1
                # print(f"{csv_file} does not meet the 80% TMAX threshold.")
    print(f"Total insert files: {insert_files}")
    print(f"Total delete files: {delete_files}")
# Example usage
input_dir = 'StationDailySummaries'  # Directory where the split files are stored
output_dir = 'CleanedStationDailySummaries'  # Directory to store cleaned files

clean_csv_files(input_dir, output_dir, threshold=80)

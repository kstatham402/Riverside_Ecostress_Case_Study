import csv
import os


def split_csv_by_station(input_file):
    # Create the directory if it doesn't exist
    output_dir = 'StationDailySummaries'
    os.makedirs(output_dir, exist_ok = True)

    # Open the input CSV file for reading
    with open(input_file, 'r', newline = '', encoding = 'utf-8') as infile:
        reader = csv.DictReader(infile)

        # Dictionary to store file writers for each station
        station_writers = {}

        # Process each row in the CSV file
        for row in reader:
            station = row['STATION']
            station_name = row['NAME']

            # If we haven't written to this station's file yet, create a new writer
            if station not in station_writers:
                # Output file path for the current station
                output_file = os.path.join(output_dir, f"{station_name}.csv")

                # Open the output file for this station
                outfile = open(output_file, 'w', newline = '', encoding = 'utf-8')
                writer = csv.DictWriter(outfile, fieldnames = reader.fieldnames)

                # Write the header to the output file
                writer.writeheader()

                # Store the writer in the dictionary
                station_writers[station] = writer
                station_writers[
                    station].outfile = outfile  # Store the file reference for closing later

            # Write the current row to the appropriate file
            station_writers[station].writerow(row)

    # Close all the output files
    for writer in station_writers.values():
        writer.outfile.close()

    print(f"Splitting completed. Files are saved in the '{output_dir}' directory.")


# Example usage
input_csv = "DailySummaries.csv"  # Replace with your actual input file path
split_csv_by_station(input_csv)

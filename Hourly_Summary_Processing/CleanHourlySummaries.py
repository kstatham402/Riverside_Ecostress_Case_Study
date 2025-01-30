import pandas as pd
import os


def convert_tmp_to_celsius(tmp_value):
    # tmp_value is in the format like "+0161,5"
    # Split by comma and remove the "+" sign
    temp_in_tenths = int(tmp_value.split(',')[0][1:])
    return temp_in_tenths / 10  # Convert tenths to full degrees Celsius


def filter_columns(data):
    # Define the columns to keep
    columns_to_keep = ['STATION', 'DATE', 'NAME', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'TMP']

    # Load the data into a DataFrame
    df = pd.read_csv(data)

    # Select only the columns specified
    df_filtered = df[columns_to_keep]

    # Convert TMP to Celsius
    df_filtered['TMP'] = df_filtered['TMP'].apply(convert_tmp_to_celsius)

    return df_filtered


def process_directory(input_directory, output_directory):
    # Make sure the output directory exists, if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through all files in the specified input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a CSV
        if filename.endswith('.csv'):
            input_file_path = os.path.join(input_directory, filename)
            print(f"Processing file: {input_file_path}")

            # Call the filter_columns function on each CSV file
            filtered_data = filter_columns(input_file_path)

            # Define the output file path
            output_filename = f"filtered_{filename}"
            output_file_path = os.path.join(output_directory, output_filename)

            # Save the filtered data to the new directory
            filtered_data.to_csv(output_file_path, index = False)
            print(f"Saved filtered data to: {output_file_path}")


def main():
    # Define the paths to the input and output directories
    input_directory = 'HourlySummaryRaws'
    output_directory = 'HourlySummaryColumnFiltered'

    # Process all CSV files in the input directory and save to the output directory
    process_directory(input_directory, output_directory)


if __name__ == "__main__":
    # Run the main function
    main()

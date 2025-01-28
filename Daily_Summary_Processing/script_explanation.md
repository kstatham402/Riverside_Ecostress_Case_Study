# Python Script to Remove Stations with Missing Temperature Data

This script processes a CSV file containing weather station data and removes stations that have 20% or more missing temperature data. It uses the Pandas library for efficient data manipulation and analysis.

## How the Code Works

### Importing Required Libraries
```python
import pandas as pd
```
- The Pandas library is imported to handle data processing. Pandas is well-suited for working with tabular data like CSV files, allowing easy data manipulation.

### Function Definition
```python
def remove_stations_with_missing_data(input_csv, output_csv, threshold=20):
```
- A function named `remove_stations_with_missing_data` is defined to encapsulate the logic.
- Parameters:
  - `input_csv`: Path to the input CSV file containing weather station data.
  - `output_csv`: Path to the output CSV file to save the filtered data.
  - `threshold`: Percentage of missing data allowed before removing a station (default is 20%).

### Reading the Input CSV
```python
    df = pd.read_csv(input_csv)
```
- The input CSV file is read into a Pandas DataFrame, which provides a structured and flexible way to work with the data.

### Identifying Temperature Columns
```python
    temp_columns = ['TAVG', 'TMAX', 'TMIN', 'TOBS']
```
- These columns represent average, maximum, minimum, and observed temperatures. They are analyzed for missing values.

### Calculating Missing Data
```python
    df['missing_temp_count'] = df[temp_columns].isna().sum(axis=1)
    df['total_temp_count'] = len(temp_columns)
```
- `missing_temp_count`: The number of missing values across the temperature columns for each row.
- `total_temp_count`: The total number of temperature columns.

### Grouping by Station
```python
    station_missing_data = (
        df.groupby('STATION')
        .apply(lambda x: x['missing_temp_count'].sum() / (x['total_temp_count'].sum()) * 100)
        .reset_index(name='missing_percentage')
    )
```
- The data is grouped by the `STATION` column.
- The percentage of missing temperature data is calculated for each station.

### Filtering Stations
```python
    stations_to_keep = station_missing_data[station_missing_data['missing_percentage'] < threshold]['STATION']
```
- Stations with less than the specified `threshold` of missing data are identified and retained.

### Filtering the Original DataFrame
```python
    filtered_df = df[df['STATION'].isin(stations_to_keep)]
```
- The original data is filtered to include only the stations identified in the previous step.

### Cleaning Up and Saving
```python
    filtered_df = filtered_df.drop(columns=['missing_temp_count', 'total_temp_count'], errors='ignore')
    filtered_df.to_csv(output_csv, index=False)
```
- Helper columns (`missing_temp_count` and `total_temp_count`) are removed.
- The filtered DataFrame is saved to a new CSV file specified by `output_csv`.

### Example Usage
```python
input_csv = input("Enter the path to the input CSV file (default: input.csv): ") or "input.csv"
output_csv = input("Enter the path to the output CSV file (default: filtered_output.csv): ") or "filtered_output.csv"

remove_stations_with_missing_data(input_csv, output_csv, threshold=20)
```
- The script prompts the user for input and output file paths, with default values provided if the user presses Enter.
- The `remove_stations_with_missing_data` function is called with the specified file paths and threshold.

## Key Features
- **Flexibility**: The threshold for missing data can be adjusted.
- **Default Values**: Input and output file paths have default values for ease of use.
- **Efficient Data Handling**: The Pandas library ensures fast and intuitive data processing.

## Output
The script generates a new CSV file containing only the stations with less than 20% missing temperature data, ensuring a cleaner dataset for further analysis.
input_csv = 'input.csv'  # Replace with the path to your input CSV
output_csv = 'filtered_output.csv'  # Replace with the path to your output CSV
remove_stations_with_missing_data(input_csv, output_csv, threshold=20)

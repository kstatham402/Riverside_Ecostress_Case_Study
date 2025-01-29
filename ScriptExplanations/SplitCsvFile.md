# Splitting a CSV File by Station Using Python

## Overview
This Python script processes a CSV file containing weather data and splits it into separate files based on the station names. Each station's data is saved in its own CSV file.

## How It Works
The script reads an input CSV file (`DailySummaries.csv`), extracts the station and station name from each row, and writes the corresponding data into separate files.

### Step-by-Step Breakdown

1. **Create an Output Directory**
   - The script ensures that the `StationDailySummaries` directory exists, where the split files will be stored.
   ```python
   output_dir = 'StationDailySummaries'
   os.makedirs(output_dir, exist_ok=True)
   ```

2. **Read the Input CSV File**
   - The script opens the CSV file in read mode using `csv.DictReader`, which reads each row as a dictionary where column names are the keys.
   ```python
   with open(input_file, 'r', newline='', encoding='utf-8') as infile:
       reader = csv.DictReader(infile)
   ```

3. **Initialize a Dictionary for Station Writers**
   - This dictionary keeps track of file writers for each station to prevent opening and closing files multiple times.
   ```python
   station_writers = {}
   ```

4. **Iterate Through Each Row**
   - The script extracts the `STATION` and `NAME` values from each row.
   - If a station hasn't been processed yet, a new CSV file is created for it.
   ```python
   station = row['STATION']
   station_name = row['NAME']
   ```

5. **Create and Manage CSV Writers**
   - If the station does not already have an associated writer, a new file is created.
   - The header row is written once to the new file.
   ```python
   if station not in station_writers:
       output_file = os.path.join(output_dir, f"{station_name}.csv")
       outfile = open(output_file, 'w', newline='', encoding='utf-8')
       writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
       writer.writeheader()
       station_writers[station] = writer
       station_writers[station].outfile = outfile
   ```

6. **Write Data to the Appropriate File**
   - The current row is written to the corresponding station file.
   ```python
   station_writers[station].writerow(row)
   ```

7. **Close All Open Files**
   - Once all rows are processed, all open files are closed to prevent memory leaks.
   ```python
   for writer in station_writers.values():
       writer.outfile.close()
   ```

8. **Print Completion Message**
   - A message is displayed to indicate that the splitting process is finished.
   ```python
   print(f"Splitting completed. Files are saved in the '{output_dir}' directory.")
   ```

## Example Usage
Simply call the function with the path to your input CSV file:
```python
input_csv = "DailySummaries.csv"  # Replace with your actual input file path
split_csv_by_station(input_csv)
```

## Key Concepts for Python Beginners
- **File Handling:** Opening, reading, writing, and closing files properly.
- **Dictionaries:** Used to store file handlers efficiently.
- **CSV Processing:** Using `csv.DictReader` and `csv.DictWriter` to handle structured data.
- **Conditional Logic:** Checking if a station exists before creating a new file.

By understanding this script, you can learn how to efficiently process and manage large datasets in Python!


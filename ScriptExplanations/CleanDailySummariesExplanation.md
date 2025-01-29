# Cleaning and Filtering CSV Files in Python

## Overview
This script processes CSV files from a directory, checks if they contain sufficient valid temperature data (TMAX), and moves files meeting the threshold into a new directory. It provides a practical example of file handling, data filtering, and directory management in Python.

## How It Works

### 1. **Setting Up Directories**
```python
os.makedirs(output_dir, exist_ok=True)
```
- The script creates the output directory (`CleanedStationDailySummaries`) if it does not already exist.

### 2. **Reading CSV Files**
```python
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
```
- The script scans the `input_dir` (`StationDailySummaries`) for all CSV files.
- It stores file names in a list for processing.

### 3. **Processing Each CSV File**
The script loops through each CSV file to check the percentage of valid `TMAX` values.
```python
for csv_file in csv_files:
    input_file = os.path.join(input_dir, csv_file)
```
- It constructs the full file path for each CSV file.

### 4. **Reading and Counting Valid Rows**
```python
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    total_rows = 0
    valid_TMAX_rows = 0
```
- The script reads each CSV file using `csv.DictReader`, which allows accessing column values by their headers.
- `total_rows` counts the number of records.
- `valid_TMAX_rows` counts rows where `TMAX` is not empty.

### 5. **Calculating Valid Data Percentage**
```python
TMAX_percentage = (valid_TMAX_rows / total_rows) * 100 if total_rows > 0 else 0
```
- If there are records in the file, the script calculates the percentage of rows with valid `TMAX` values.

### 6. **Filtering and Moving Files**
```python
if TMAX_percentage >= threshold:
    output_file = os.path.join(output_dir, csv_file)
    os.rename(input_file, output_file)
    insert_files += 1
else:
    delete_files += 1
```
- If at least `threshold`% (default 80%) of rows contain `TMAX`, the file is moved to `CleanedStationDailySummaries`.
- Otherwise, it is not moved, effectively filtering out files with too much missing data.

### 7. **Tracking Processed Files**
```python
print(f"Total insert files: {insert_files}")
print(f"Total delete files: {delete_files}")
```
- The script counts how many files were moved (`insert_files`) and how many were ignored (`delete_files`).

## Example Usage
To run the script:
```python
input_dir = 'StationDailySummaries'
output_dir = 'CleanedStationDailySummaries'
clean_csv_files(input_dir, output_dir, threshold=80)
```
- This will process all files in `StationDailySummaries` and move only those meeting the 80% `TMAX` threshold to `CleanedStationDailySummaries`.

## Learning Takeaways
- **File handling:** Reading, moving, and managing CSV files.
- **Data filtering:** Checking for missing values and applying thresholds.
- **Directory management:** Using `os.makedirs` and `os.rename` for organizing files.
- **Basic statistics:** Calculating percentages from a dataset.

This script is a useful introduction to working with CSV files in Python and implementing data cleaning techniques!


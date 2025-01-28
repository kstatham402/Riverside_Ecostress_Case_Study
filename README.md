# Finding the Station Data for Riverside County, CA

To obtain hourly temperature data for Riverside County in a CSV format similar to your example, you can utilize the National Centers for Environmental Information's (NCEI) Climate Data Online (CDO) platform. Here's a step-by-step guide:

1. **Access Climate Data Online (CDO):**
   - Navigate to the CDO portal: ([ncei.noaa.gov](https://www.ncei.noaa.gov/cdo-web/?utm_source=chatgpt.com))

2. **Search for Stations in Riverside County:**
   - Use the "Search Tool" to locate weather stations:
     - Enter "Daily Summaries" in the "Select Weather Observation Type/Dataset" field.
     - Enter your desired date range in the "Select Date Range" field.
     - Enter "Counties" in the "Search For" field.
     - Enter "Riverside County, CA" in the "Enter a Search Term" field.
   - Click the search button

3. **Select and Download Data:**
   - Click the "Riverside County, CA" under data categories.
   - Click the "Add to cart" button
   - View your cart
     - Choose the CSV format for your download.

4. **Format the Data:**
   - The downloaded CSV files will contain detailed hourly temperature records.
   - You may need to process the data to match your desired format:
     - **STATION:** Unique identifier for the station.
     - **NAME:** Name of the station.
     - **DATE:** Timestamp of the observation (e.g., 2020-01-01T00:00).
     - **TAVG:** The mean daily temperature for the given station.
     - **TMAX:** The max daily temperature for the given station.
     - **TMIN:** The min daily temperature for the given station.
     - **TOBS:** The actual daily temperature for the given station.

For additional assistance, the NCEI provides a "Find a Station" tool that can help you locate specific stations and their data: ([Drought.gov](https://www.drought.gov/data-maps-tools/ncei-find-station-tool?utm_source=chatgpt.com))

By following these steps, you should be able to acquire and format the daily temperature data for Riverside County in CSV format.  

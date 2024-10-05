import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime

def process_nc_file(file_path, output_dir):
    # Open the NetCDF file
    ds = xr.open_dataset(file_path)

    # Define latitude and longitude range around Saudi Arabia
    lat_range = slice(32.0, 16)
    lon_range = slice(34, 56)

    # Assign Latitude and Longitude as coordinates if not already set
    if 'Latitude' not in ds.coords or 'Longitude' not in ds.coords:
        ds = ds.assign_coords(
            Latitude=("Idx_Atrack", "Idx_Xtrack", ds['Latitude'].values),
            Longitude=("Idx_Atrack", "Idx_Xtrack", ds['Longitude'].values)
        )

    # Subset the data using .where() based on latitude and longitude range
    try:
        subset = ds.where(
            (ds['Latitude'] >= lat_range.stop) & (ds['Latitude'] <= lat_range.start) &
            (ds['Longitude'] >= lon_range.start) & (ds['Longitude'] <= lon_range.stop),
            drop=True
        )
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return

    # Extract date from filename
    date_str = os.path.basename(file_path).split('.')[1][1:]  # Assumes format like 'AERDB_L2_VIIRS_SNPP.A2019001.0918.002.2023076145255.nc'
    date = datetime.strptime(date_str, '%Y%j')
    year = date.year
    month = date.month

    # Create output directory structure
    year_dir = os.path.join(output_dir, str(year))
    month_dir = os.path.join(year_dir, f"{month:02d}")
    os.makedirs(month_dir, exist_ok=True)

    # Save the filtered dataset
    output_file = os.path.join(month_dir, f"filtered_{os.path.basename(file_path)}")
    subset.to_netcdf(output_file)
    print(f"Saved filtered file: {output_file}")

def process_all_files(input_dir, output_dir):
    for year in range(2012, 2025):  # Adjust range as needed
        year_dir = os.path.join(input_dir, str(year))
        if not os.path.exists(year_dir):
            continue
        for file in os.listdir(year_dir):
            if file.endswith('.nc'):
                file_path = os.path.join(year_dir, file)
                process_nc_file(file_path, output_dir)

# Set input and output directories
input_dir = '../earthdata/VIIRS-NOAA20 Deep Blue Aerosol'
output_dir = '../filtered_noaa20'

# Process all files
process_all_files(input_dir, output_dir)
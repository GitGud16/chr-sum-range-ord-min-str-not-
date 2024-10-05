import xarray as xr
import os
import pandas as pd
from datetime import datetime
import argparse

def process_filtered_file(file_path, lat_range, lon_range):
    ds = xr.open_dataset(file_path)
    
    # Extract smoke-related variable
    smoke_variable_name = 'Aerosol_Optical_Thickness_550_Land'
    smoke_data = ds[smoke_variable_name].values
    
    # Extract corresponding latitude and longitude values
    latitude_values = ds['Latitude'].values
    longitude_values = ds['Longitude'].values
    
    # Extract date from filename
    file_name = os.path.basename(file_path)
    date_str = file_name.split('.')[1][1:]  # Assumes format like 'filtered_AERDB_L2_VIIRS_SNPP.A2019001.0918.002.2023076145255.nc'
    date = datetime.strptime(date_str, '%Y%j')
    
    # Create a list to store data points
    data_points = []
    for i in range(smoke_data.shape[0]):
        for j in range(smoke_data.shape[1]):
            lat = latitude_values[i, j]
            lon = longitude_values[i, j]
            if (not pd.isna(smoke_data[i, j]) and
                lat_range[0] <= lat <= lat_range[1] and
                lon_range[0] <= lon <= lon_range[1]):
                data_points.append([date, lon, lat, smoke_data[i, j]])
    
    return data_points

def process_all_filtered_files(base_dir, output_file, region):
    all_data_points = []
    
    # Set latitude and longitude ranges based on the region
    if region == 'riyadh':
        lat_range = (24.5, 25.0)
        lon_range = (46.5, 47.0)
    else:  # Saudi Arabia
        lat_range = (16.0, 32.0)
        lon_range = (34.0, 56.0)
    
    for year in range(2012, 2025):  # Adjust range as needed
        year_dir = os.path.join(base_dir, str(year))
        if not os.path.exists(year_dir):
            continue
        
        for month in range(1, 13):
            month_dir = os.path.join(year_dir, f"{month:02d}")
            if not os.path.exists(month_dir):
                continue
            
            for file in os.listdir(month_dir):
                if file.startswith('filtered_') and file.endswith('.nc'):
                    file_path = os.path.join(month_dir, file)
                    data_points = process_filtered_file(file_path, lat_range, lon_range)
                    all_data_points.extend(data_points)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(all_data_points, columns=["Date", "Longitude", "Latitude", "Aerosol_Optical_Thickness"])
    
    # Sort the DataFrame by date
    df = df.sort_values("Date")
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process filtered NetCDF files for aerosol data.")
    parser.add_argument('--region', choices=['saudi_arabia', 'riyadh'], default='saudi_arabia',
                        help="Choose the region to process: 'saudi_arabia' or 'riyadh'")
    args = parser.parse_args()

    # Set directories and output file
    base_dir = '../filtered_noaa20'
    output_file = f'aerosol_data_{args.region}.csv'

    # Process all filtered files and save results
    df = process_all_filtered_files(base_dir, output_file, args.region)

    # Print summary information
    print(f"Data has been written to {output_file}")
    print(f"\nSummary for {args.region.capitalize()}:")
    print(f"Total data points: {len(df)}")
    print(f"Date range: from {df['Date'].min()} to {df['Date'].max()}")
    print(f"Longitude range: from {df['Longitude'].min():.2f} to {df['Longitude'].max():.2f}")
    print(f"Latitude range: from {df['Latitude'].min():.2f} to {df['Latitude'].max():.2f}")
    print(f"Aerosol Optical Thickness range: from {df['Aerosol_Optical_Thickness'].min():.4f} to {df['Aerosol_Optical_Thickness'].max():.4f}")
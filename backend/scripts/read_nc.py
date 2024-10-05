import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd

# Open the NetCDF file
file_path = '../earthdata/filtered_noaa20/2019/1/filtered_AERDB_L2_VIIRS_SNPP.A2019001.0918.002.2023076145255.nc'
ds = xr.open_dataset(file_path)

# Define latitude and longitude range around Riyadh
lat_range = slice(32.0, 16)  # Latitude range around Saudi Arabia
lon_range = slice(34, 56)  # Longitude range around Saudi Arabia
# lat_range = slice(25.0, 24.5)  # Latitude range around Riyadh
# lon_range = slice(46.5, 47.0)  # Longitude range around Riyadh
# lat_range = slice(16, 32)  # Latitude range around Riyadh
# lon_range = slice(34, 56)  # Longitude range around Riyadh

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
    print(e)
    subset = ds
# Extract smoke-related variable
smoke_variable_name = 'Aerosol_Optical_Thickness_550_Land'  # Update based on your dataset
smoke_data = subset[smoke_variable_name].values

# Extract corresponding latitude and longitude values
latitude_values = subset['Latitude'].values
longitude_values = subset['Longitude'].values

# Print a sample of the data along with lat/lon
print("Sample Data with Latitude and Longitude:\n")
count = 0
for i in range(smoke_data.shape[0]):
    for j in range(smoke_data.shape[1]):
        if not pd.isna(smoke_data[i, j]):  # Avoid printing NaN values
            print(f"Latitude: {latitude_values[i, j]}, Longitude: {longitude_values[i, j]}, Smoke Value: {smoke_data[i, j]}")
            count = count + 1
print(count, " VARIABLES")

# Optional: Create a DataFrame for better visualization and analysis
data_points = []
for i in range(smoke_data.shape[0]):
    for j in range(smoke_data.shape[1]):
        if not pd.isna(smoke_data[i, j]):  # Avoid NaN values
            data_points.append([latitude_values[i, j], longitude_values[i, j], smoke_data[i, j]])

# Create a pandas DataFrame
df = pd.DataFrame(data_points, columns=["Latitude", "Longitude", "Smoke Value"])
print("DataFrame with Latitude, Longitude, and Smoke Values:\n", df.head())

# Visualize the smoke data using scatter plot with actual lat/lon
plt.figure(figsize=(10, 6))
plt.scatter(df["Longitude"], df["Latitude"], c=df["Smoke Value"], cmap='Reds', marker='o', edgecolor='k')
plt.colorbar(label='Aerosol Optical Thickness (Smoke)')
plt.title('Smoke Data Over Riyadh with Actual Coordinates')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()
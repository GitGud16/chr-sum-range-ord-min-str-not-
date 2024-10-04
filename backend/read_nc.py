import xarray as xr


path = 'EarthData/Aerosol/filteredData/2024/filtered_AERDB_L2_VIIRS_NOAA20.A2024001.0930.002.2024001215552.nc'
ds = xr.open_dataset(path)


print(ds.data_vars)
# print(ds.data_vars['Aerosol_Type_Land'].values)
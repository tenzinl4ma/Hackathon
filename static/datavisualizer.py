import xarray as xr
import pandas as pd

# Open MERRA-2 NetCDF file
ds = xr.open_dataset("/Users/m22-007/Desktop/Hackathon/Hackathon/static/MERRA2_400.tavg1_2d_aer_Nx.20250901.nc4")

# Check variable name (likely 'PM2_5_AER')
print(ds)

# Select PM2.5
pm25 = ds['PM2_5_AER']

# Tokyo bounding box
pm25_tokyo = pm25.sel(lon=slice(139.5, 140), lat=slice(35.5, 35.9))

# Convert to pandas DataFrame
df = pm25_tokyo.to_dataframe().reset_index()

# Save as CSV
df.to_csv("Tokyo_PM25_20250901.csv", index=False)
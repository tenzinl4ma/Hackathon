import json
import numpy as np
from netCDF4 import Dataset

file_path = "MERRA2_400.tavg1_2d_aer_Nx.20250901.nc4"
ds = Dataset(file_path, 'r')

# Optional: list all variables
print("Variables:", list(ds.variables.keys()))

# Use the correct total AOD variable
if 'TOTEXTTAU' not in ds.variables:
    raise ValueError("Expected variable 'TOTEXTTAU' not found in file.")

lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]

# Japan bounding box
lat_min, lat_max = 24.0, 46.0
lon_min, lon_max = 122.0, 153.0

lat_mask = (lats >= lat_min) & (lats <= lat_max)
lon_mask = (lons >= lon_min) & (lons <= lon_max)

lat_indices = np.where(lat_mask)[0]
lon_indices = np.where(lon_mask)[0]

# Extract total AOD at first time step
aod_total = ds.variables['TOTEXTTAU'][0, :, :].filled(np.nan)

# Subset to Japan
aod_japan = aod_total[np.ix_(lat_indices, lon_indices)]
japan_lats = lats[lat_indices]
japan_lons = lons[lon_indices]

# Build JSON
features = []
for i, lat in enumerate(japan_lats):
    for j, lon in enumerate(japan_lons):
        val = float(aod_japan[i, j])
        if not np.isnan(val) and val >= 0:  # AOD should be >= 0
            features.append({
                "lat": round(lat, 4),
                "lon": round(lon, 4),
                "aod": round(val, 4)
            })

output = {
    "date": "2025-09-01",
    "source": "MERRA-2 tavg1_2d_aer_Nx",
    "variable": "TOTEXTTAU (Total AOD at 550nm)",
    "data": features
}

with open("merra2_aod_japan_20250901.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"✅ Saved {len(features)} points to JSON.")
ds.close()
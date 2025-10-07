import xarray as xr
import numpy as np
import json
from scipy.interpolate import griddata


input_nc = "MERRA2_400.tavg1_2d_aer_Nx.20250901.nc4"
output_json = "aod.json"

# japan
min_lat, max_lat = 20.0, 50.0
min_lon, max_lon = 120.0, 150.0

# data res
resolution = 0.1

# main program
print("Loading NetCDF file...")
ds = xr.open_dataset(input_nc)


var_name = 'TOTEXTTAU'
if var_name not in ds:
    raise KeyError(f"'{var_name}' not found. Available: {list(ds.data_vars)}")

aod = ds[var_name]
if 'time' in aod.dims:
    aod = aod.isel(time=0)  # clock

lat = ds['lat'].values
lon = ds['lon'].values

# grid
LON, LAT = np.meshgrid(lon, lat)
AOD = aod.values


flat_lat = LAT.ravel()
flat_lon = LON.ravel()
flat_aod = AOD.ravel()

mask = (
    (flat_lat >= min_lat) &
    (flat_lat <= max_lat) &
    (flat_lon >= min_lon) &
    (flat_lon <= max_lon) &
    np.isfinite(flat_aod) &
    (flat_aod >= 0)
)

lats = flat_lat[mask]
lons = flat_lon[mask]
aods = flat_aod[mask]

print("Interpolating to dense grid...")
grid_lats = np.arange(min_lat, max_lat + resolution, resolution)
grid_lons = np.arange(min_lon, max_lon + resolution, resolution)

GRID_LON, GRID_LAT = np.meshgrid(grid_lons, grid_lats)
grid_points = np.column_stack([GRID_LAT.ravel(), GRID_LON.ravel()])

interpolated_aod = griddata(
    points=np.column_stack([lats, lons]),
    values=aods,
    xi=grid_points,
    method='linear',
    fill_value=np.nan
)

# sanity
valid = ~np.isnan(interpolated_aod)
dense_lat = grid_points[valid, 0]
dense_lon = grid_points[valid, 1]
dense_aod = interpolated_aod[valid]

# data
data_points = [
    {
        "lat": round(float(lat_val), 4),
        "lon": round(float(lon_val), 4),
        "aod": round(float(aod_val), 4)
    }
    for lat_val, lon_val, aod_val in zip(dense_lat, dense_lon, dense_aod)
]


output = {
    "date": "2025-09-01",
    "source": "MERRA-2 tavg1_2d_aer_Nx",
    "variable": "TOTEXTTAU (Total AOD at 550nm)",
    "data": data_points
}


with open(output_json, 'w') as f:
    json.dump(output, f, indent=2)

print("done")
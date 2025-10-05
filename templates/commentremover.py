import json
import random

# Define coordinate bounds (Japan roughly)
MIN_LAT, MAX_LAT = 30.0, 46.0
MIN_LON, MAX_LON = 129.0, 146.0

# Number of sample points
NUM_POINTS = 2000  # adjust as needed

data = []

for i in range(NUM_POINTS):
    lat = round(random.uniform(MIN_LAT, MAX_LAT), 5)
    lon = round(random.uniform(MIN_LON, MAX_LON), 5)

    # Simulated data with reasonable ranges
    aod = round(random.uniform(0.05, 0.8), 3)  # aerosol optical depth
    temperature = round(random.uniform(10, 38), 2)  # °C
    vegetation = round(random.uniform(0.2, 0.95), 3)  # NDVI index
    precipitation = round(random.uniform(0, 100), 2)  # mm

    data.append({
        "id": i + 1,
        "lat": lat,
        "lon": lon,
        "aod": aod,
        "temperature": temperature,
        "vegetation": vegetation,
        "precipitation": precipitation
    })

# Wrap in structure compatible with your frontend
output = {
    "layer_info": [
        {"id": "airQuality", "name": "Air Quality (MODIS AOD)", "color": "#f59e0b"},
        {"id": "temperature", "name": "Surface Temperature (Landsat 8)", "color": "#ef4444"},
        {"id": "vegetation", "name": "Vegetation Health (NDVI)", "color": "#10b981"},
        {"id": "precipitation", "name": "Precipitation (GPM)", "color": "#3b82f6"}
    ],
    "data": data
}

# Save to a single JSON file (replace aod.json with your existing one)
with open("combined_data.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ combined_data.json created with", NUM_POINTS, "entries.")

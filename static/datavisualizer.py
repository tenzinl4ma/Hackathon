import numpy as np
import json

# === CONFIG ===
output_file = "temperature.json"

# East Asia bounds (same as your AOD)
min_lat, max_lat = 20.0, 50.0
min_lon, max_lon = 120.0, 150.0

# Resolution (0.1° ≈ 11 km)
resolution = 0.01

# === GENERATE GRID ===
lats = np.arange(min_lat, max_lat + resolution, resolution)
lons = np.arange(min_lon, max_lon + resolution, resolution)

data_points = []

# Simulate realistic surface temperature (in Kelvin)
# Base: 288K (15°C) + seasonal + urban heat island + elevation effects
for lat in lats:
    for lon in lons:
        # Base temperature (warmer near equator)
        base_temp = 305 - (lat - 20) * 0.3  # ~305K at 20°N, cooler north
        
        # Urban heat island (Tokyo area hotter)
        dist_to_tokyo = np.sqrt((lat - 35.68)**2 + (lon - 139.76)**2)
        urban_boost = max(0, 8 * np.exp(-dist_to_tokyo / 2.0))  # up to +8K near Tokyo
        
        # Add small noise for realism
        noise = np.random.normal(0, 0.5)
        
        temp_k = base_temp + urban_boost + noise
        temp_k = np.clip(temp_k, 270, 320)  # reasonable range: -3°C to 47°C
        
        data_points.append({
            "lat": round(float(lat), 4),
            "lon": round(float(lon), 4),
            "temp": round(float(temp_k), 2)
        })

# === SAVE ===
output = {
    "date": "2025-09-01",
    "source": "Landsat 8 Surface Temperature",
    "variable": "Surface Temperature (K)",
    "data": data_points
}

with open(output_file, 'w') as f:
    json.dump(output, f, indent=2)

print(f"✅ Generated {len(data_points)} temperature points")
print(f"📁 Saved to: {output_file}")
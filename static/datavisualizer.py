import json

# Define Japan's bounding box (WGS84)
JAPAN_BOUNDS = {
    "min_lat": 24.0,
    "max_lat": 45.5,
    "min_lon": 122.9,
    "max_lon": 145.9
}

def is_in_japan(lat, lon):
    return (
        JAPAN_BOUNDS["min_lat"] <= lat <= JAPAN_BOUNDS["max_lat"] and
        JAPAN_BOUNDS["min_lon"] <= lon <= JAPAN_BOUNDS["max_lon"]
    )

# Input and output file names
input_file = "merra2_aod_japan_20250901.json"
output_file = "aod.json"

# Load the original data
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter data points to only those in Japan
filtered_data = [
    point for point in data["data"]
    if is_in_japan(point["lat"], point["lon"])
]

# Create new structure (preserve metadata)
output = {
    "date": data.get("date", "unknown"),
    "source": data.get("source", "MERRA-2"),
    "variable": data.get("variable", "TOTEXTTAU (Total AOD at 550nm)"),
    "data": filtered_data
}

# Save to aod.json
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print(f"✅ Filtered {len(data['data'])} points → {len(filtered_data)} points in Japan.")
print(f"📁 Saved to: {output_file}")
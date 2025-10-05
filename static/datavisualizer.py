import json
import random

# --- Configuration ---
INPUT_GEOJSON = 'veg.json'
OUTPUT_GEOJSON = 'temperature.json'

# Temperature range (°C)
TEMP_NORTH = 5    # Hokkaido cold
TEMP_SOUTH = 32   # Okinawa hot
NOISE_RANGE = 2   # ±2°C random noise

# Density optional (like your previous veg_with_density)
USE_DENSITY = True

URBAN_PREFECTURES = {
    '東京都', '大阪府', '神奈川県', '愛知県', '埼玉県', '千葉県', '兵庫県', '北海道'
}
FORESTED_PREFECTURES = {
    '京都府', '奈良府', '長野県', '岐阜県', '高知県', '島根県', '栃木県',
    '群馬県', '福井県', '和歌山県', '宮崎県', '熊本県', '大分県'
}

# --- Load GeoJSON ---
with open(INPUT_GEOJSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

for feature in data['features']:
    # --- Compute centroid latitude for MultiPolygon safely ---
    coords_list = feature['geometry']['coordinates']
    all_points = []

    for polygon in coords_list:
        for ring in polygon:
            for pt in ring:
                if isinstance(pt, list) and len(pt) >= 2:
                    all_points.append(pt)

    if all_points:
        lat = sum(pt[1] for pt in all_points) / len(all_points)
    else:
        lat = 35.0  # fallback latitude

    # --- Map latitude to temperature (north→south) ---
    temp = ((lat - 24) / (45 - 24)) * (TEMP_SOUTH - TEMP_NORTH) + TEMP_NORTH
    temp += random.uniform(-NOISE_RANGE, NOISE_RANGE)
    feature['properties']['temperature'] = round(temp, 1)

    # --- Optional: add density for vegetation-style visualization ---
    if USE_DENSITY:
        name = feature['properties'].get('nam_ja') or feature['properties'].get('nam')
        if name in URBAN_PREFECTURES:
            base = 0.1
        elif name in FORESTED_PREFECTURES:
            base = 0.7
        else:
            base = 0.4  # medium for others
        noise = random.uniform(-0.15, 0.15)
        density = max(0.05, min(0.9, base + noise))
        feature['properties']['density'] = round(density, 2)

# --- Save new GeoJSON ---
with open(OUTPUT_GEOJSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Generated '{OUTPUT_GEOJSON}' with temperature and density for {len(data['features'])} features.")

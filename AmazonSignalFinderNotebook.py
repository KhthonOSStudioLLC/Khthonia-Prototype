# Amazon Signal Finder - Jupyter Notebook Version

from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- INPUT SECTION ---
tile_input = {
    "lidar_tile_id": "BR-XINGU-2031-LIDAR001",
    "satellite_scene_id": "S2A_MSIL2A_20250614T143211_N0500_R096_T22MZV_20250614T145623",
    "mythic_seed": "Kuhikugu"
}

# --- TILE ANALYSIS ---
def analyze_tiles(lidar_tile_id: str, satellite_scene_id: str):
    return {
        "summary": f"Tile {lidar_tile_id} overlaps with dense canopy zones. Satellite {satellite_scene_id} shows slight rectilinear clearings near Xingu tributaries.",
        "coords": ["-10.1234", "-52.5678"],
        "anomaly_type": "possible geometric anomaly",
        "confidence": 0.72
    }

# --- GPT-4 HISTORIC CORRELATION ---
def mythic_correlation_report(mythic_seed: str, anomaly_desc: str) -> str:
    prompt = (
        f"You're an AI archaeologist assisting in Amazonian exploration. "
        f"Given the legend '{mythic_seed}' and anomaly '{anomaly_desc}', "
        f"evaluate potential historical significance and settlement patterns."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# --- SITE REPORT GENERATOR ---
def generate_site_report(inputs: dict, tile_analysis: dict, mythic_analysis: str) -> str:
    return f"""
🗺️ AMAZON SIGNAL FINDER - SITE REPORT
------------------------------------
Date: {datetime.now().strftime('%Y-%m-%d')}

📍 Coordinates: {tile_analysis['coords'][0]}, {tile_analysis['coords'][1]}
🛰️ LIDAR Tile ID: {inputs['lidar_tile_id']}
🌐 Satellite Scene ID: {inputs['satellite_scene_id']}

🔍 Anomaly Detected: {tile_analysis['anomaly_type']}
📊 Confidence Score: {tile_analysis['confidence']}

🔮 Mythic Correlation: {inputs['mythic_seed']}
🧠 GPT-4 Insight: {mythic_analysis}
"""

# --- EXECUTION ---
tile_data = analyze_tiles(tile_input["lidar_tile_id"], tile_input["satellite_scene_id"])
mythic_report = mythic_correlation_report(tile_input['mythic_seed'], tile_data['anomaly_type'])
report = generate_site_report(tile_input, tile_data, mythic_report)
print(report)

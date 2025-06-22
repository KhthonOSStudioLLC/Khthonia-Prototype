import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_tiles(lidar_tile_id: str, satellite_scene_id: str):
    return {
        "summary": f"Tile {lidar_tile_id} overlaps with dense canopy zones. Satellite {satellite_scene_id} shows slight rectilinear clearings.",
        "coords": ["-10.1234", "-52.5678"],
        "anomaly_type": "possible geometric anomaly",
        "confidence": 0.72
    }

def mythic_correlation_report(mythic_seed: str, anomaly_desc: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # <-- Move it here!
    prompt = (
        f"You're an AI archaeologist. Given the legend '{mythic_seed}' and anomaly '{anomaly_desc}', "
        f"evaluate historical significance and potential settlement patterns."
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def generate_site_report(lidar_tile_id, satellite_scene_id, mythic_seed):
    tile_data = analyze_tiles(lidar_tile_id, satellite_scene_id)
    mythic_report = mythic_correlation_report(mythic_seed, tile_data['anomaly_type'])
    return f"""
📈 AMAZON SIGNAL FINDER - SITE REPORT
------------------------------------
Date: {datetime.now().strftime('%Y-%m-%d')}

📍 Coordinates: {tile_data['coords'][0]}, {tile_data['coords'][1]}
🚁 LIDAR Tile ID: {lidar_tile_id}
🌐 Satellite Scene ID: {satellite_scene_id}

🔍 Anomaly Detected: {tile_data['anomaly_type']}
📊 Confidence Score: {tile_data['confidence']}

🔮 Mythic Correlation: {mythic_seed}
🧠 GPT-4 Insight: {mythic_report}
"""

st.title("Amazon Signal Finder - Z-Challenge Prototype")

lidar_tile_id = st.text_input("Enter LIDAR Tile ID", "BR-XINGU-2031-LIDAR001")
satellite_scene_id = st.text_input("Enter Satellite Scene ID", "S2A_MSIL2A_20250614T143211_N0500_R096_T22MZV_20250614T145623")
mythic_seed = st.text_input("Enter Mythic Seed (e.g., Kuhikugu, Paititi)", "Kuhikugu")

if st.button("Generate Report"):
    with st.spinner("Analyzing..."):
        report = generate_site_report(lidar_tile_id, satellite_scene_id, mythic_seed)
        st.text_area("Site Report", report, height=500)
        st.success("Report generated successfully!")

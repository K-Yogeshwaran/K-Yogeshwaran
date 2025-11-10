import requests
import os
from datetime import datetime, timedelta

API_KEY = os.environ.get("WAKATIME_API_KEY")
headers = {"Authorization": f"Basic {API_KEY}"}

def get_stats():
    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
    return requests.get(url, headers=headers).json()["data"]

data = get_stats()

def block(title, items):
    md = f"### {title}\n"
    for item in items:
        md += f"- **{item['name']}**: {item['text']}\n"
    md += "\n"
    return md

markdown = "## ⏳ Last 7 Days WakaTime Stats\n\n"
markdown += block("Languages", data["languages"])
markdown += block("Editors", data["editors"])
markdown += block("Operating Systems", data["operating_systems"])
markdown += block("Projects", data["projects"])
markdown += block("Machines", data["machines"])

with open("WAKA_STATS.md", "w", encoding="utf-8") as f:
    f.write(markdown)

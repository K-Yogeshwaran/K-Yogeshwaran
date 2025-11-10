import requests
import os
import re

API_KEY = os.environ.get("WAKATIME_API_KEY")
headers = {"Authorization": f"Basic {API_KEY}"}

def fetch(url):
    return requests.get(url, headers=headers).json()["data"]

today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")

def block(title, items):
    out = f"### {title}\n"
    for item in items:
        out += f"- **{item['name']}**: {item['text']}\n"
    return out + "\n"

content = (
    "## ⏱ Today’s WakaTime Stats\n\n"
    + block("Languages", today["languages"])
    + block("Editors", today["editors"])
    + block("Operating Systems", today["operating_systems"])
    + block("Projects", today["projects"])
    + block("Machines", today["machines"])
    + "\n---\n\n"
    + "## ⏳ Last 7 Days WakaTime Stats\n\n"
    + block("Languages", week["languages"])
    + block("Editors", week["editors"])
    + block("Operating Systems", week["operating_systems"])
    + block("Projects", week["projects"])
    + block("Machines", week["machines"])
)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

new_readme = re.sub(
    r"<!--START_WAKATIME-->[\s\S]*<!--END_WAKATIME-->",
    f"<!--START_WAKATIME-->\n{content}<!--END_WAKATIME-->",
    readme,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

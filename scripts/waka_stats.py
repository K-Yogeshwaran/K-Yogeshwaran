import requests
import os
import re

API_KEY = os.environ.get("WAKATIME_API_KEY")

def fetch(url):
    return requests.get(url, params={"api_key": API_KEY}).json()["data"]

today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")

# Add this before the file write to debug in the Action logs
print(f"Generated content length: {len(content)}")

def block(title, items):
    out = f"### {title}\n"
    for item in items:
        out += f"- **{item['name']}**: {item['text']}\n"
    return out + "\n"

content = (
    "## ⏱ Today’s WakaTime Stats\n\n"
    + block("Languages", today.get("languages", []))
    + block("Editors", today.get("editors", []))
    + block("Operating Systems", today.get("operating_systems", []))
    + block("Projects", today.get("projects", []))
    + block("Machines", today.get("machines", []))
    + "\n---\n\n"
    + "## ⏳ Last 7 Days WakaTime Stats\n\n"
    + block("Languages", week.get("languages", []))
    + block("Editors", week.get("editors", []))
    + block("Operating Systems", week.get("operating_systems", []))
    + block("Projects", week.get("projects", []))
    + block("Machines", week.get("machines", []))
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

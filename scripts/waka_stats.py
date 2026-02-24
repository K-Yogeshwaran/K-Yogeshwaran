import requests
import os
import re
import sys

API_KEY = os.environ.get("WAKATIME_API_KEY")

def fetch(url):
    try:
        response = requests.get(url, params={"api_key": API_KEY}, timeout=10)
        response.raise_for_status()
        return response.json().get("data", {})
    except:
        return {}

def make_bar(percent):
    done = int(percent / 10)
    return f"{'█' * done}{'░' * (10 - done)}"

def block(title, items):
    if not items: return ""
    out = f"#### {title}\n| Item | Time | Progress |\n| :--- | :--- | :--- |\n"
    for item in items[:5]:
        bar = make_bar(item.get('percent', 0))
        out += f"| {item['name']} | {item['text']} | `{bar}` {item['percent']}% |\n"
    return out + "\n"

# Fetch Data
today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")
all_time = fetch("https://wakatime.com/api/v1/users/current/stats/all_time")

content = ""

# Only show Today if you've actually coded
if today.get("total_seconds", 0) > 0:
    content += f"### ⏱ Today's Activity: {today.get('human_readable_total')}\n"
    content += block("Languages", today.get("languages", []))
    content += "---\n"

content += "### ⏳ Last 7 Days\n"
content += block("Languages", week.get("languages", []))
content += block("Projects", week.get("projects", []))
content += "---\n"

if all_time:
    content += f"### 🌍 Lifetime Coding: {all_time.get('human_readable_total')}\n"
    content += block("Top Languages", all_time.get("languages", []))

# The Surgical Update
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# This regex finds the space between your markers
pattern = r"[\s\S]*"
replacement = f"\n{content}"

if re.search(pattern, readme):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(re.sub(pattern, replacement, readme))
    print("Stats updated without touching your intro!")
else:
    print("Error: Could not find markers. Make sure they are in your README.")

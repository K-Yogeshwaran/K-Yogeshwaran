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
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {}

def make_bar(percent):
    done = int(percent / 10)
    return f"{'█' * done}{'░' * (10 - done)}"

def block(title, items):
    # Only show if percent > 1.0 (removes the 0 sec/tiny entries)
    filtered = [i for i in items if i.get('percent', 0) > 1.0]
    if not filtered: return ""
    
    out = f"#### {title}\n| Item | Time | Progress |\n| :--- | :--- | :--- |\n"
    for item in filtered[:5]:
        bar = make_bar(item.get('percent', 0))
        out += f"| {item['name']} | {item['text']} | `{bar}` {item['percent']}% |\n"
    return out + "\n"

# Fetch Data
today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")
all_time = fetch("https://wakatime.com/api/v1/users/current/stats/all_time")

stats_content = ""

# 1. Today (Only show if > 0)
if today.get("total_seconds", 0) > 0:
    stats_content += f"### ⏱ Today's Activity: {today.get('human_readable_total')}\n"
    stats_content += block("Languages", today.get("languages", []))
    stats_content += "---\n"

# 2. Last 7 Days
stats_content += "### ⏳ Last 7 Days\n"
stats_content += block("Languages", week.get("languages", []))
stats_content += block("Projects", week.get("projects", []))

# 3. All Time (Impressive total)
if all_time:
    stats_content += "---\n### 🌍 Lifetime Coding: " + all_time.get("human_readable_total", "0 secs") + "\n"
    stats_content += block("Top Languages", all_time.get("languages", []))

# Update README
try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    # The surgical pattern
    pattern = r"[\s\S]*"
    replacement = f"\n{stats_content}\n"

    if "" in readme:
        new_readme = re.sub(pattern, replacement, readme)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("Successfully updated the stats section!")
    else:
        print("ERROR: Markers not found. README not modified.")
        sys.exit(1)
except Exception as e:
    print(f"File Error: {e}")
    sys.exit(1)

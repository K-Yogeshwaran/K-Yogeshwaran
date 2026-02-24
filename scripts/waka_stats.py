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
        print(f"Error fetching: {e}")
        return {}

def make_bar(percent):
    done = int(percent / 10)
    return f"{'█' * done}{'░' * (10 - done)}"

def block(title, items):
    # Filter: Only show if percent > 1% and time is not '0 secs'
    filtered_items = [i for i in items if i.get('percent', 0) > 1 and i.get('text') != "0 secs"]
    
    if not filtered_items:
        return ""
    
    out = f"#### {title}\n| Item | Time | Progress |\n| :--- | :--- | :--- |\n"
    for item in filtered_items[:5]:
        bar = make_bar(item.get('percent', 0))
        out += f"| {item['name']} | {item['text']} | `{bar}` {item['percent']}% |\n"
    return out + "\n"

# Fetch Data
today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")
all_time = fetch("https://wakatime.com/api/v1/users/current/stats/all_time")

stats_content = ""

# 1. Today's Stats (Only if coding happened)
if today.get("total_seconds", 0) > 0:
    stats_content += f"### ⏱ Today's Activity: {today.get('human_readable_total')}\n"
    stats_content += block("Languages", today.get("languages", []))
    stats_content += "---\n"

# 2. Weekly Stats
stats_content += "### ⏳ Last 7 Days\n"
stats_content += block("Languages", week.get("languages", []))
stats_content += block("Projects", week.get("projects", []))
stats_content += "---\n"

# 3. All-Time Stats
if all_time:
    stats_content += f"### 🌍 Lifetime Coding: {all_time.get('human_readable_total')}\n"
    stats_content += block("Top Languages", all_time.get("languages", []))

# --- UPDATE README WITHOUT OVERWRITING ---
try:
    with open("README.md", "r", encoding="utf-8") as f:
        full_content = f.read()

    # The key is to match EXACTLY between the markers
    pattern = r"[\s\S]*"
    new_block = f"\n{stats_content}"

    if "" in full_content and "" in full_content:
        updated_content = re.sub(pattern, new_block, full_content)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("Successfully updated stats section.")
    else:
        print("Critical Error: Markers or not found!")
        sys.exit(1)
except Exception as e:
    print(f"File error: {e}")
    sys.exit(1)

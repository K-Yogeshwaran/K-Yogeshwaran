import requests
import os
import re
import sys

API_KEY = os.environ.get("WAKATIME_API_KEY")

def fetch(url):
    try:
        response = requests.get(url, params={"api_key": API_KEY}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {})
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return {}

def make_progress_bar(percent):
    # Visual bar: ████░░░░░░
    done = int(percent / 10)
    left = 10 - done
    return f"{'█' * done}{'░' * left}"

def block(title, items):
    if not items:
        return f"#### {title}\n- No activity recorded\n\n"
    
    out = f"#### {title}\n"
    out += "| Item | Time | Progress |\n"
    out += "| :--- | :--- | :--- |\n"
    
    for item in items[:5]:
        name = item.get('name', 'Unknown')
        text = item.get('text', '0 secs')
        percent = item.get('percent', 0)
        bar = make_progress_bar(percent)
        out += f"| {name} | {text} | `{bar}` {percent}% |\n"
    return out + "\n"

# Fetch Data
today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")

if not week:
    print("Could not retrieve weekly stats.")
    sys.exit(1)

# Prepare Content
today_total = today.get("human_readable_total", "0 secs")
content = f"### ⏱ Today's Activity: {today_total}\n\n"

if today.get("total_seconds", 0) > 0:
    content += block("Languages", today.get("languages", []))
else:
    content += "_No coding activity tracked yet for today._\n\n"

content += "---\n\n### ⏳ Last 7 Days\n"
content += block("Languages", week.get("languages", []))
content += block("Editors", week.get("editors", []))
content += block("Projects", week.get("projects", []))

# Update README.md
try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    pattern = r"[\s\S]*"
    replacement = f"\n{content}"

    if re.search(pattern, readme):
        new_readme = re.sub(pattern, replacement, readme)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("README updated successfully.")
    else:
        print("Markers not found!")
        sys.exit(1)
except Exception as e:
    print(f"File error: {e}")
    sys.exit(1)

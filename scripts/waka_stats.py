import requests
import os
import re
import sys

API_KEY = os.environ.get("WAKATIME_API_KEY")

def fetch(url):
    try:
        response = requests.get(url, params={"api_key": API_KEY}, timeout=10)
        response.raise_for_status() # Check for HTTP errors
        data = response.json()
        return data.get("data", {})
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return {}

# Fetching both Today and Last 7 Days
today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")

# If 'week' is empty, the API key might be wrong or WakaTime is down
if not week:
    print("Could not retrieve weekly stats. Check your API Key.")
    sys.exit(1)

def block(title, items):
    if not items or len(items) == 0:
        return f"### {title}\n- No activity recorded\n\n"
    out = f"### {title}\n"
    for item in items[:5]: # Top 5
        out += f"- **{item['name']}**: {item['text']}\n"
    return out + "\n"

# Prepare the markdown content
today_total = today.get("human_readable_total", "0 secs")
content = f"## ⏱ Today's Activity: {today_total}\n\n"

if today.get("total_seconds", 0) > 0:
    content += block("Languages", today.get("languages", []))
    content += block("Editors", today.get("editors", []))
else:
    content += "_No coding activity tracked yet for today._\n\n"

content += "---\n\n## ⏳ Last 7 Days Stats\n\n"
content += block("Languages", week.get("languages", []))
content += block("Editors", week.get("editors", []))
content += block("Projects", week.get("projects", []))

# Update the README
try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()

    pattern = r"[\s\S]*"
    replacement = f"\n{content}"

    if re.search(pattern, readme):
        new_readme = re.sub(pattern, replacement, readme)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_readme)
        print("README.md updated locally.")
    else:
        print("Could not find markers in README.md")
        sys.exit(1)
except Exception as e:
    print(f"File error: {e}")
    sys.exit(1)

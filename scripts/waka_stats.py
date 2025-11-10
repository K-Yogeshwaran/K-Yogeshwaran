import requests
import os
import re

API_KEY = os.environ.get("WAKATIME_API_KEY")
headers = {"Authorization": f"Basic {API_KEY}"}
url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"

data = requests.get(url, headers=headers).json()["data"]

def block(title, items):
    out = f"### {title}\n"
    for item in items:
        out += f"- **{item['name']}**: {item['text']}\n"
    return out + "\n"

content = (
    block("Languages", data["languages"])
    + block("Editors", data["editors"])
    + block("Operating Systems", data["operating_systems"])
    + block("Projects", data["projects"])
    + block("Machines", data["machines"])
)

# Load README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace content between markers
new_readme = re.sub(
    r"<!--START_WAKATIME-->[\s\S]*<!--END_WAKATIME-->",
    f"<!--START_WAKATIME-->\n{content}<!--END_WAKATIME-->",
    readme,
)

# Save README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

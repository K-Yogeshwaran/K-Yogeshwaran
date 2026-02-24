import requests
import os
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
    # Only show if percent > 1.0%
    filtered = [i for i in items if i.get('percent', 0) > 1.0]
    if not filtered: return ""
    
    out = f"#### {title}\n| Item | Time | Progress |\n| :--- | :--- | :--- |\n"
    for item in filtered[:5]:
        bar = make_bar(item.get('percent', 0))
        out += f"| {item['name']} | {item['text']} | `{bar}` {item['percent']}% |\n"
    return out + "\n"

# 1. Fetch Stats
today = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")
all_time = fetch("https://wakatime.com/api/v1/users/current/stats/all_time")

# 2. Build the "Impressive" Intro Section
intro = """# 👨‍💻 Yogeshwaran K
**AI/ML Enthusiast | Java & Python Developer | Coimbatore, India**

<p align="left">
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" />
</p>

---

### 🚀 About Me
I am a dedicated developer based in **Coimbatore, Tamil Nadu**, focused on building intelligent systems and high-performance web applications.

* 🔭 **Active Development**: Currently working on an **Air Quality Prediction Project** applying feature engineering and outlier handling.
* 🌱 **Continuous Learning**: Mastering **Deep Learning** and **AI** frameworks.
* 💻 **Project Spotlight**: Architected **Study Sync**, a real-time collaborative platform using **Spring Boot**, **WebSockets**, and **React**.
* 🏆 **Hackathons**: Recently participated in **Devtrails 2026** hosted by Guidewire.

---

### 📊 Coding Dashboard
"""

# 3. Build Stats Section
stats_content = ""
if today.get("total_seconds", 0) > 0:
    stats_content += f"### ⏱ Today's Activity: {today.get('human_readable_total')}\n"
    stats_content += block("Languages", today.get("languages", []))
    stats_content += "---\n"

stats_content += "### ⏳ Last 7 Days\n"
stats_content += block("Languages", week.get("languages", []))
stats_content += block("Projects", week.get("projects", []))

if all_time:
    stats_content += "---\n### 🌍 Lifetime Coding: " + all_time.get("human_readable_total", "0 secs") + "\n"
    stats_content += block("Top Languages", all_time.get("languages", []))

# 4. Build Footer (GitHub Stats)
footer = """
---

### 📈 GitHub Insights
<p align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=K-Yogeshwaran&show_icons=true&theme=radical&include_all_commits=true&count_private=true" />
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=K-Yogeshwaran&layout=compact&theme=radical" />
</p>
"""

# 5. Write everything to README.md (Overwriting is now intentional)
full_readme = intro + stats_content + footer

with open("README.md", "w", encoding="utf-8") as f:
    f.write(full_readme)

print("Profile regenerated successfully!")

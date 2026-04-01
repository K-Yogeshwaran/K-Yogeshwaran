import requests
import os

API_KEY = os.environ.get("WAKATIME_API_KEY")

def fetch(url):
    try:
        response = requests.get(url, params={"api_key": API_KEY}, timeout=10)
        response.raise_for_status()
        return response.json().get("data", {})
    except:
        return {}

def active_only(items):
    return [i for i in items if i.get("total_seconds", 0) >= 60]

def badge_row(items):
    COLOR_MAP = {
        "Java":       ("ED8B00", "openjdk"),
        "Python":     ("3776AB", "python"),
        "JavaScript": ("F7DF1E", "javascript"),
        "TypeScript": ("3178C6", "typescript"),
        "CSS":        ("1572B6", "css3"),
        "HTML":       ("E34F26", "html5"),
        "Bash":       ("4EAA25", "gnubash"),
        "SQL":        ("4479A1", "postgresql"),
        "XML":        ("555555", ""),
        "Markdown":   ("000000", "markdown"),
        "Text":       ("555555", ""),
        "Properties": ("555555", ""),
    }
    badges = []
    for item in items[:8]:
        name  = item["name"]
        time  = item.get("text", "").replace(" ", "_")
        color, logo = COLOR_MAP.get(name, ("555555", ""))
        label = name.replace("-", "--").replace(" ", "_")
        logo_part = f"&logo={logo}" if logo else ""
        badges.append(
            f"![{name}](https://img.shields.io/badge/{label}-{time}-{color}?style=flat-square{logo_part}&logoColor=white)"
        )
    return " ".join(badges)

def summary_badges(week_total, alltime_total, week_projects):
    week_clean = week_total.replace(" ", "_")
    at_clean   = alltime_total.replace(" ", "_")
    lines = []
    lines.append(
        f"![All-Time](https://img.shields.io/badge/All--Time_Coding-{at_clean}-58a6ff?style=for-the-badge&logo=wakatime&logoColor=white)"
        f"&nbsp;&nbsp;"
        f"![This Week](https://img.shields.io/badge/This_Week-{week_clean}-3fb950?style=for-the-badge&logo=wakatime&logoColor=white)"
    )
    if week_projects:
        proj = week_projects[0].get("name", "")[:20].replace(" ", "_").replace("-", "--")
        lines.append(
            f"![Top Project](https://img.shields.io/badge/Top_Project-{proj}-d29922?style=for-the-badge&logo=github&logoColor=white)"
        )
    return "\n\n".join(lines)

# ── Fetch ─────────────────────────────────────────────────────────────────────
week     = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")
all_time = fetch("https://wakatime.com/api/v1/users/current/stats/all_time")

week_total    = week.get("human_readable_total", "0 hrs")
alltime_total = all_time.get("human_readable_total", "0 hrs") if all_time else "0 hrs"
week_langs    = active_only(week.get("languages", []))
week_projects = active_only(week.get("projects", []))
at_langs      = active_only(all_time.get("languages", [])) if all_time else []

WAKA_USER = "K-Yogeshwaran"

wakatime_img = (
    f"https://github-readme-stats.vercel.app/api/wakatime"
    f"?username={WAKA_USER}&theme=github_dark&hide_border=true"
    f"&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&icon_color=58a6ff"
    f"&layout=compact&langs_count=8&custom_title=WakaTime%20Activity"
)

stats_block = f"""\
{summary_badges(week_total, alltime_total, week_projects)}

<br/>

<img src="{wakatime_img}" alt="WakaTime Stats" />

<br/>

**Last 7 days — active languages only:**

{badge_row(week_langs)}

**All-time — top languages:**

{badge_row(at_langs)}
"""

readme = f"""\
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=32&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=Yogeshwaran+K;Software+Engineer;Java+%26+Full-Stack+Developer" alt="Typing SVG" />

<br/>

**`Software Engineer · Java & Full-Stack · Coimbatore, India`**

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/k-yogeshwaran)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/K-Yogeshwaran)
[![WakaTime](https://img.shields.io/badge/WakaTime-000000?style=for-the-badge&logo=wakatime&logoColor=white)](https://wakatime.com/@K-Yogeshwaran)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yogeshwaran@example.com)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=K-Yogeshwaran&style=for-the-badge&color=58a6ff&label=PROFILE+VIEWS)

</div>

---

## 🧑‍💻 About Me

```java
public class Yogeshwaran {{

    String role        = "Software Engineer";
    String location    = "Coimbatore, Tamil Nadu, India";
    String college     = "Sri Eshwar College of Engineering";

    String[] primary   = {{ "Java", "Spring Boot", "Microservices", "REST APIs" }};
    String[] frontend  = {{ "React", "React Native", "TypeScript" }};
    String[] databases = {{ "PostgreSQL", "MongoDB", "Redis" }};
    String   ml        = "Applied when the problem calls for it";

    String building    = "GigShield — AI parametric insurance · DevTrails 2026";
    String exploring   = "Distributed systems · JVM internals · System design";

    String philosophy  = "Clean architecture. Scalable APIs. Ship things that work.";
}}
```

---

## 🛠️ Tech Stack

<div align="center">

### Languages
[![Skills](https://skillicons.dev/icons?i=java,python,js,ts,bash&theme=dark)](https://skillicons.dev)

### Frameworks & Backend
[![Skills](https://skillicons.dev/icons?i=spring,react,flask,nodejs&theme=dark)](https://skillicons.dev)

### Databases & Infrastructure
[![Skills](https://skillicons.dev/icons?i=postgres,mongodb,redis,docker,github&theme=dark)](https://skillicons.dev)

### Tools & Editors
[![Skills](https://skillicons.dev/icons?i=vscode,idea,git,postman,linux&theme=dark)](https://skillicons.dev)

</div>

---

## 🚀 Featured Projects

<div align="center">

| Project | Description | Stack |
|---------|-------------|-------|
| 🛡️ **[GigShield](https://github.com/K-Yogeshwaran)** | Parametric insurance platform for India's gig economy. Spring Boot microservices — Worker, Policy, Claims & Payout — with XGBoost premium calculator and Flask trigger engine. | `Java` `Spring Boot` `XGBoost` `React Native` `PostgreSQL` |
| 📚 **[StudySync](https://github.com/K-Yogeshwaran)** | Real-time collaborative study platform. Architected WebSocket layer and REST API backend with room-based sessions and live presence indicators. | `Spring Boot` `WebSockets` `React` `MongoDB` |
| 🌾 **[IntelliFarm](https://github.com/K-Yogeshwaran)** | IoT + ML platform bridging traditional farming and data-driven agriculture. Real-time soil/weather monitoring, crop prediction, and resource automation. Unifies farmers, dealers, and drivers. | `Python` `Spring Boot` `IoT` `scikit-learn` `React` |

</div>

---

## 📊 Coding Activity

<div align="center">

{stats_block}

</div>

---

## 📈 GitHub Insights

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=K-Yogeshwaran&show_icons=true&theme=github_dark&include_all_commits=true&count_private=true&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9" />
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=K-Yogeshwaran&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=K-Yogeshwaran&theme=github-dark-blue&hide_border=true&background=0d1117&stroke=58a6ff&ring=58a6ff&fire=ff6b6b&currStreakNum=ffffff&sideNums=58a6ff&currStreakLabel=58a6ff&sideLabels=8b949e&dates=8b949e" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=K-Yogeshwaran&theme=github-compact&hide_border=true&bg_color=0d1117&color=58a6ff&line=58a6ff&point=ffffff&area=true&area_color=58a6ff" />

</div>

---

## 🏆 GitHub Trophies

<div align="center">

<img src="https://github-profile-trophy.vercel.app/?username=K-Yogeshwaran&theme=algolia&no-frame=true&no-bg=true&margin-w=4&row=1" />

</div>

---

<div align="center">

<img src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg" />

<sub>📡 Coding stats auto-refreshed daily via <b>GitHub Actions</b> + <b>WakaTime API</b></sub>

</div>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print(f"✅ README.md generated!")
print(f"   All-time : {alltime_total}")
print(f"   This week: {week_total}")
print(f"   Active langs (7d): {[i['name'] for i in week_langs]}")

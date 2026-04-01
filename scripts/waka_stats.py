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

def make_bar(percent, width=20):
    done = int(percent / (100 / width))
    return "█" * done + "░" * (width - done)

def lang_block(comment, items):
    filtered = [i for i in items if i.get("total_seconds", 0) >= 60]
    if not filtered:
        return ""
    out = f"# {comment}\n"
    out += f"{'Language':<16} {'Bar':<22} {'Pct':>6}  {'Time':>9}\n"
    out += "-" * 58 + "\n"
    for item in filtered[:8]:
        bar = make_bar(item.get("percent", 0))
        name = item["name"][:15]
        pct = f"{round(item.get('percent', 0), 1)}%"
        time = item.get("text", "")
        out += f"{name:<16} {bar:<22} {pct:>6}  {time:>9}\n"
    return out

def project_block(title, items):
    filtered = [i for i in items if i.get("total_seconds", 0) >= 60]
    if not filtered:
        return ""
    out = f"\n# {title}\n"
    out += f"{'Project':<28} {'Time':>9}  {'Share':>6}\n"
    out += "-" * 50 + "\n"
    for item in filtered[:5]:
        name = item["name"][:27]
        time = item.get("text", "")
        pct = f"{round(item.get('percent', 0), 1)}%"
        out += f"{name:<28} {time:>9}  {pct:>6}\n"
    return out

def wrap_codeblock(content):
    if not content.strip():
        return ""
    return f"```text\n{content.strip()}\n```\n\n"

# Fetch stats
today    = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week     = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")
month    = fetch("https://wakatime.com/api/v1/users/current/stats/last_30_days")
all_time = fetch("https://wakatime.com/api/v1/users/current/stats/all_time")

alltime_total = all_time.get("human_readable_total", "N/A") if all_time else "N/A"
week_total    = week.get("human_readable_total", "N/A")

readme = """\
<div align="center">

# Yogeshwaran K

**Software Engineer · Java & Full-Stack Developer · Coimbatore, India**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/k-yogeshwaran)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/K-Yogeshwaran)
[![WakaTime](https://img.shields.io/badge/WakaTime-000000?style=flat-square&logo=wakatime&logoColor=white)](https://wakatime.com/@K-Yogeshwaran)

</div>

---

## About Me

> Software engineer focused on building **production-grade Java backends** and full-stack systems.
> I thrive on clean architecture, scalable APIs, and shipping things that actually work.

- **Primary stack:** Java · Spring Boot · REST APIs · Microservices
- **Building now:** GigShield — AI parametric insurance platform · Guidewire DevTrails 2026
- **Exploring:** Distributed systems · JVM internals · System design patterns
- **ML as a tool:** Applied XGBoost and scikit-learn when the problem calls for it

---

## Tech Stack

### Languages
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

### Frameworks & Backend
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring-boot&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![React Native](https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socket.io&logoColor=white)

### Databases & Infrastructure
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

### ML Toolkit (Applied)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EA4335?style=flat-square&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-111111?style=flat-square&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)

---

## Featured Projects

### 🛡️ GigShield &nbsp; `[Guidewire DevTrails 2026]`
> **Java · Spring Boot · Python · XGBoost · Flask · React Native · PostgreSQL**

Parametric insurance platform for India's gig economy. Designed a full microservices backend in Spring Boot — Worker, Policy, Claims, and Payout services — with an XGBoost-powered premium calculator and a Flask trigger engine for real-time event detection. React Native app connects workers, insurers, and claim handlers in one unified flow.

---

### 📚 StudySync &nbsp; `[Real-time Platform]`
> **Spring Boot · WebSockets · React · MongoDB**

Real-time collaborative study platform. Architected the WebSocket layer and REST API backend with room-based sessions, live presence indicators, and concurrent document editing. Built for low-latency multi-user state synchronization.

---

### 🌾 IntelliFarm &nbsp; `[IoT + ML]`
> **Python · Spring Boot · IoT · scikit-learn · React · PostgreSQL**

A digital farming consultant bridging traditional agriculture and data-driven decisions. IoT sensors stream soil and weather data in real time; ML models drive crop prediction and resource automation. Integrates farmers, dealers, and logistics drivers into one unified application.

---

## 📊 Coding Activity

"""

readme += f"> **All-time:** `{alltime_total}` &nbsp;|&nbsp; **Last 7 days:** `{week_total}`\n\n"

if today.get("total_seconds", 0) > 0:
    block = lang_block(
        f"today · {today.get('human_readable_total', '')}",
        today.get("languages", [])
    ) + project_block("projects", today.get("projects", []))
    readme += wrap_codeblock(block)

week_block = lang_block(
    f"last 7 days · {week_total}",
    week.get("languages", [])
) + project_block("active projects (7 days)", week.get("projects", []))
readme += wrap_codeblock(week_block)

if month.get("total_seconds", 0) > 0:
    m_block = lang_block(
        f"last 30 days · {month.get('human_readable_total', '')}",
        month.get("languages", [])
    )
    readme += wrap_codeblock(m_block)

if all_time:
    at_block = lang_block(
        f"all-time · {alltime_total}",
        all_time.get("languages", [])
    )
    readme += wrap_codeblock(at_block)

readme += """\
---

## 📈 GitHub Insights

<p align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=K-Yogeshwaran&show_icons=true&theme=github_dark&include_all_commits=true&count_private=true&hide_border=true" />
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=K-Yogeshwaran&layout=compact&theme=github_dark&hide_border=true" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=K-Yogeshwaran&theme=github-dark-blue&hide_border=true" />
</p>

---

<div align="center">
  <sub>📡 Stats auto-refreshed daily via GitHub Actions + WakaTime API</sub>
</div>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("✅ README regenerated successfully!")

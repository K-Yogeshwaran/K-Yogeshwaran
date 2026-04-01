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

def make_bar(percent):
    done = int(percent / 10)
    return f"{'█' * done}{'░' * (10 - done)}"

def block(title, items):
    # Only show languages/projects with actual recorded time (total_seconds > 0)
    filtered = [i for i in items if i.get("total_seconds", 0) > 0 or i.get("percent", 0) > 0]
    # Secondary filter: skip anything with truly negligible usage (< 1 minute)
    filtered = [i for i in filtered if i.get("total_seconds", 0) >= 60]
    if not filtered:
        return ""
    out = f"#### {title}\n| Item | Time | Progress |\n| :--- | :--- | :--- |\n"
    for item in filtered[:8]:
        bar = make_bar(item.get("percent", 0))
        out += f"| {item['name']} | {item['text']} | `{bar}` {round(item['percent'], 1)}% |\n"
    return out + "\n"

# Fetch Stats
today  = fetch("https://wakatime.com/api/v1/users/current/stats/today")
week   = fetch("https://wakatime.com/api/v1/users/current/stats/last_7_days")
month  = fetch("https://wakatime.com/api/v1/users/current/stats/last_30_days")
all_time = fetch("https://wakatime.com/api/v1/users/current/stats/all_time")

# ── Intro ────────────────────────────────────────────────────────────────────
intro = """\
<div align="center">

# Yogeshwaran K

### AI/ML Engineer · Full-Stack Developer · Coimbatore, India

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/k-yogeshwaran)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/K-Yogeshwaran)
[![WakaTime](https://img.shields.io/badge/WakaTime-000000?style=flat-square&logo=wakatime&logoColor=white)](https://wakatime.com/@K-Yogeshwaran)

</div>

---

## 🧑‍💻 About Me

I'm a developer obsessed with building **intelligent, high-impact systems** — from ML-powered insurance platforms to real-time collaborative tools. I thrive at the intersection of **machine learning**, **backend engineering**, and **socially meaningful products**.

- 🔭 Building **GigShield** — an AI-powered parametric insurance platform for India's gig economy (Guidewire DevTrails 2026)
- 🧠 Mastering **Deep Learning**, **XGBoost**, and distributed ML inference pipelines
- ☕ Architected **StudySync** — a real-time collaborative platform with Spring Boot + WebSockets + React
- 🚦 Built a **Dynamic AI Traffic Flow Optimizer** with YOLOv8 + SUMO simulation + Flask dashboard
- ⚖️ Developed an **AI Legal Analyzer** for underserved populations — scraping & analyzing Indian legal acts across 10 domains
- 🏆 Active hackathon builder | India Innovates 2026 | DevTrails 2026

---

## 🛠️ Tech Stack

### Languages
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

### Frameworks & Libraries
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=spring-boot&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![React Native](https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EA4335?style=flat-square&logo=xgboost&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

### Databases & Infrastructure
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

### AI / ML Toolkit
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-111111?style=flat-square&logo=yolo&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)

---

## 🚀 Featured Projects

### 🛡️ GigShield — AI Parametric Insurance for Gig Workers
> **Python · Flask · XGBoost · Java Spring Boot · React Native · PostgreSQL**

An end-to-end parametric insurance platform for India's unorganized gig economy. Features an XGBoost-based premium calculator, a Flask trigger engine (ports 5001–5003) for real-time event detection, and a microservices Java backend (Worker, Policy, Claims, Payout services). Built for Guidewire DevTrails 2026.

---

### 🚦 Dynamic AI Traffic Flow Optimizer
> **Python · Flask · YOLOv8 · SUMO · Chart.js**

A computer vision-powered traffic management system using a queue-based signal control algorithm. Integrates YOLOv8 for real-time vehicle density estimation from a Roboflow dataset, with a SUMO simulation backend and a Flask web dashboard with live Chart.js visualizations.

---

### 📚 StudySync — Real-Time Collaborative Platform
> **Java Spring Boot · WebSockets · React · MongoDB**

A feature-complete collaborative study platform with real-time document editing, live presence indicators, and room-based sessions. Architected the WebSocket layer and REST API backend from scratch.

---

### ⚖️ AI Legal Analyzer
> **Python · BeautifulSoup · NLP**

A legal access tool for underserved communities in India. Built a data pipeline scraping 10 domains of Indian law (IPC, Consumer Protection, Cyber Laws, etc.) from indiacode.nic.in and indiankanoon.org. Contributed ML-driven section classification and summarization.

---

### 🗳️ Secure E-Voting System
> **Python · React · Java Spring Boot · Face Recognition**

A tamper-proof digital voting system featuring Fernet encryption, SHA-256 hash chaining, face liveness detection, and a Duress PIN anti-coercion mechanism.

---

## 📊 Coding Activity

"""

# ── Stats Section ─────────────────────────────────────────────────────────────
stats_content = ""

if today.get("total_seconds", 0) > 0:
    stats_content += f"### ⏱️ Today: {today.get('human_readable_total', '0 mins')}\n"
    stats_content += block("Languages", today.get("languages", []))
    stats_content += block("Projects", today.get("projects", []))
    stats_content += "---\n\n"

stats_content += f"### 📅 Last 7 Days: {week.get('human_readable_total', 'N/A')}\n"
stats_content += block("Languages", week.get("languages", []))
stats_content += block("Projects", week.get("projects", []))

if month.get("total_seconds", 0) > 0:
    stats_content += f"---\n\n### 🗓️ Last 30 Days: {month.get('human_readable_total', 'N/A')}\n"
    stats_content += block("Languages", month.get("languages", []))

if all_time:
    stats_content += f"---\n\n### 🌍 All-Time: {all_time.get('human_readable_total', '0 hrs')}\n"
    stats_content += block("Languages", all_time.get("languages", []))

# ── Footer ─────────────────────────────────────────────────────────────────────
footer = """
---

## 📈 GitHub Insights

<p align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=K-Yogeshwaran&show_icons=true&theme=radical&include_all_commits=true&count_private=true" />
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=K-Yogeshwaran&layout=compact&theme=radical" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=K-Yogeshwaran&theme=radical" />
</p>

---

<div align="center">
  <sub>📡 Stats auto-updated daily via GitHub Actions + WakaTime API</sub>
</div>
"""

full_readme = intro + stats_content + footer

with open("README.md", "w", encoding="utf-8") as f:
    f.write(full_readme)

print("✅ Profile README regenerated successfully!")

# Project Planning & Breakdown Agent

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-API-v1.0+-green?logo=openai)
![License](https://img.shields.io/badge/License-MIT-yellow)

An intelligent agent that transforms project goals into structured development plans with phases, tasks, and required roles using OpenAI's API.

## ✨ Features

- Converts natural language goals into actionable project plans
- Generates JSON-structured output with:
  - Development phases
  - Key tasks (2-3 per phase)
  - Recommended roles/skillsets
- Robust error handling for API limitations
- Clean, production-ready Python implementation

## 🛠️ Tools & Technologies

- **Python 3.8+** (Core implementation)
- **OpenAI API** (GPT-3.5-turbo model)
- **python-dotenv** (Secure credential management)
- **JSON** (Structured output format)

## 🚀 Getting Started

### Prerequisites
- OpenAI API key (Get yours at [platform.openai.com](https://platform.openai.com))
- Python 3.8+ installed

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/project-breakdown-agent.git
cd project-breakdown-agent

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

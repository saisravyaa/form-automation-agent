# 🧠 Form Automation Agent

A LangGraph-powered backend + Angular frontend that automates filling out web forms using data fetched from APIs and databases.

## 🚀 Tech Stack
- **Python**: FastAPI, LangGraph, Playwright
- **Frontend**: Angular
- **LangGraph**: Orchestrates data flow & state logic
- **Playwright**: Automates browser form interactions

## 🔧 Setup Instructions

### Backend (FastAPI)
```bash
# 1. Activate your virtual environment
cd form-automation-backend
finalenv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt
playwright install

# 3. Run the server
uvicorn api:app --port 8000
# In a new terminal:
cd form-automation-ui
npm install
ng serve
💡 How It Works
User enters a city name in the Angular UI.

Backend receives it and runs a LangGraph state machine.

A mocked API (or real one later) returns geolocation data.

Playwright launches a browser and fills a form with that data.

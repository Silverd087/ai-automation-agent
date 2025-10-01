# AI Automation Agent 🚀

This project is an MVP automation system where you can tell the agent what to do in plain English (e.g. "Search YouTube for lofi playlists and return the top 5 results").

The workflow is:

Planner (Gemini) – Converts natural language into structured steps (JSON).

Executor (Playwright) – Runs those steps inside a browser (navigation, filling forms, scraping, etc.).

FastAPI Backend – Provides endpoints to submit instructions, run tasks, and retrieve results.

SQLite Storage – Persists task history and scraped outputs.

🔹 Stack: FastAPI · Google Gemini API · Playwright · SQLite
🔹 Goal: Show how LLMs + automation frameworks can combine to create a simple but powerful AI agent.
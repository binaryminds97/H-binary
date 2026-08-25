# JeevanMitra AI — Phase 1 (Project Skeleton)

This repository contains the Phase 1 skeleton for JeevanMitra AI — a voice-first, multilingual livelihood & skilling assistant prototype targeted for SIH 26097.

Purpose
-------
This folder contains a minimal Streamlit entrypoint and project structure. Phase 1 creates the repository skeleton and placeholder files so the development team can implement subsequent phases incrementally.

Structure
---------
- app.py — Streamlit entrypoint (Phase 1 placeholder)
- pages/ — multipage components to be added in Phase 2/3
- components/ — UI components
- services/ — backend service modules (ai_service, recommendation_service, ...)
- database/ — SQLite helpers and schema
- data/ — CSV/JSON sample datasets
- prompts/ — LLM prompt templates
- utils/ — utility modules
- tests/ — pytest tests

Next steps
----------
After review and approval of the plan, Phase 1 will be followed by Phase 2 (landing page + navigation) implementation.

How to run (Phase 1)
--------------------
1. Create a virtual environment and activate it

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # PowerShell

2. Install dependencies

   pip install -r requirements.txt

3. Run Streamlit

   streamlit run app.py

Notes
-----
- Do not commit secrets or API keys. Use .env or Streamlit secrets.
- This is a Phase 1 skeleton. Core features are implemented in later phases.

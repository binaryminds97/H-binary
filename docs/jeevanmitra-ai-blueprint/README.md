# JeevanMitra AI Blueprint

## Project name
JeevanMitra AI

## Tagline
"Aapki awaaz, aapki skills, aapka behtar livelihood."

## Overview
JeevanMitra AI is a voice-first, multilingual livelihood and skills assistant designed for beneficiaries to discover suitable career and training pathways using a simple, explainable AI-powered workflow.

The product is especially relevant to SIH Problem Statement 26097:
"AI-Driven Voice Assistant for Livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY."

## Core goal
The platform should help users:
- speak in Hindi, Marathi or English
- answer a short conversational interview
- generate a structured beneficiary profile
- match their profile against NSQF-aligned job roles
- identify skill gaps
- propose a training roadmap and employment/self-employment path
- show local opportunity awareness
- provide an admin dashboard with aggregate insights

## Product flow
1. User selects language
2. User speaks or types answers to a short interview
3. AI extracts structured profile details
4. Recommendation engine scores and ranks jobs
5. Skill gap analysis identifies missing capabilities
6. Training roadmap and livelihood path are suggested
7. Local opportunity module adds geographic context
8. Admin can review analytics and trends

## User experience
### Landing page
- hero section with brand message
- CTA: "Start My Livelihood Journey"
- benefits overview
- how it works
- trust/privacy content

### Beneficiary journey
- language selection
- voice-first interview
- conversational question flow
- dynamic skipping of answered questions
- final profile summary
- top 3 career recommendations

### Recommendation output
Each recommendation includes:
- final score
- NSQF level
- sector
- matched skills
- skill gaps
- reason behind the match
- training path

## Architecture
### Frontend
- Streamlit
- mobile-friendly, accessible UI

### Backend
- Python services
- local scoring engine
- service layer for AI, recommendations, analytics, skill gaps, and opportunities

### AI layer
- Gemini API for:
  - language understanding
  - extraction of structured profile JSON
  - translation support
  - short explanation of recommendation rationale

### Database layer
- SQLite for MVP
- optional upgrade path to Supabase/PostgreSQL

### Data layer
- CSV/JSON prototype datasets
- structured job-role and opportunity information
- translation data

## Recommendation engine
The core principle is:
> AI understands the beneficiary; the recommendation engine makes the recommendation explainable.

The scoring is deterministic and transparent. Default weights:
- Education compatibility: 20%
- Existing skill compatibility: 25%
- Interest compatibility: 20%
- Mobility compatibility: 15%
- Employment preference: 10%
- Local opportunity: 10%

The final score is computed locally in Python, not by LLM guessing.

## Skill gap logic
The system compares:
- beneficiary skills
- job required skills

and returns:
- matched skills
- missing skills
- partially matched skills
- readiness indicator

The readiness indicator should be labeled as:
- Profile Match / Current Readiness Indicator
- not a guaranteed employment probability

## AI rules
The AI must:
- ask one question at a time
- respect the selected language
- avoid asking already-answered questions
- parse voice/text into valid structured JSON
- explain recommendations in simple language

The AI must not:
- invent NSQF qualification codes
- invent government scheme details
- guarantee employment
- claim fake vacancies
- decide final score with no rules

## Data source policy
Prioritize:
1. official NSDC / Skill India / State skill sources
2. government open-data sources
3. official PM-AJAY / MoSJE portals
4. only then secondary sources

If exact values cannot be verified, the app must label them as prototype/demo data instead of presenting them as verified official data.

## Privacy & security
- collect minimum necessary data
- no Aadhaar, bank, or password collection
- require consent before profile storage
- use environment variables / secrets
- parameterize SQL queries
- never expose personal identifiers in aggregate admin analytics

## Development strategy
Implement in phases, not all at once:
1. Architecture & project setup
2. Landing page & navigation
3. Beneficiary profile UI
4. NSQF dataset and recommendation engine
5. Skill-gap engine
6. Database layer
7. Gemini integration
8. Voice interaction
9. Multilingual UI
10. Local opportunity module
11. Admin dashboard
12. Testing and demo
13. Deployment

## Suggested folder structure
```text
jeevanmitra-ai/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── .streamlit/
│   └── config.toml
├── pages/
├── components/
├── services/
├── database/
├── data/
├── prompts/
├── utils/
├── tests/
└── docs/
```

## Demo flow
Example SIH demo flow:
1. User selects Marathi
2. Starts voice interview
3. Speech is converted to profile JSON
4. Recommendation engine shows top 3 options
5. Best match: Agricultural Machinery Technician
6. Skill-gap analysis highlights missing training areas
7. Local opportunities are shown
8. AI speaks the final recommendation

## Deployment recommendation
For hackathon prototype:
- GitHub repository
- Streamlit Community Cloud
- SQLite / CSV datasets
- environment variables for secrets
- avoid paid services unless absolutely necessary

## Future production direction
After the prototype:
- Supabase/PostgreSQL for production data
- secure authentication
- verified connectors to official government datasets
- voice channels such as IVR and WhatsApp
- improved regional speech models and analytics

## Acceptance checklist
The final implementation should only be considered complete when:
- landing page works
- language selection works
- beneficiary interview works
- profile extraction works
- recommendation engine works
- skill gap works
- local opportunities work
- admin dashboard works
- tests pass
- demo mode works
- deployment works

## Final statement
This blueprint is intentionally designed to keep the project beginner-friendly, explainable, practical, and realistic for a hackathon prototype. The key technical strength is not "AI generates everything"; instead, the approach is:

"AI understands the beneficiary; the recommendation engine makes the recommendation explainable."

This is the right balance for a credible and auditable solution.

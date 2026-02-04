🧠 AI Skill Gap Analyzer

An AI-powered Skill Gap Analyzer that evaluates a learner’s current skills against a target job role and provides:

Strengths and weaknesses

Identified skill gaps

Priority learning areas

Personalized learning roadmap

The system uses interactive, scenario-based questions and dynamically updates the skill map and recommendations based on user responses.

🚀 Live Demo

Deployed App:
👉 https://skill-gap-analyzer-mine.streamlit.app/

Source Code:
👉 https://github.com/Puzzledcat06/Skill-Gap-Analyzer

🎯 Problem Statement

Design and develop an AI-based Skill Gap Analyzer that evaluates a learner’s current skill level against a target job role and provides:

Strengths and weaknesses

Identified skill gaps

Priority focus areas

Personalized learning recommendations

The system works in an interactive and continuous manner using scenario-based Q&A and skill checkpoints. The evaluation adapts dynamically based on user responses and generates a clear improvement roadmap.

🧩 Features

🔹 Multi-role support (ML Engineer, Data Engineer, Frontend Developer, Backend Developer)

🔹 Skillset customization per role

🔹 Interactive, scenario-based assessment

🔹 Dynamic evaluation of core & supporting skills

🔹 Skill strengths, needs improvement, and gaps

🔹 Priority learning areas & recommended next steps

🔹 Free-first AI integration (Groq API)

🔹 Deployed on Streamlit Cloud

🏗️ Architecture
skill-gap-analyzer/
├── app.py                 # Streamlit UI
├── ai/                    # AI layer (Groq)
│   ├── question_generator.py
│   └── response_interpreter.py
├── core/                  # Evaluation logic
│   ├── schema.py
│   ├── evaluator.py
│   ├── priority.py
│   ├── recommendations.py
│   └── progress.py (optional)
├── data/                  # Role & skill schemas (JSON)
│   ├── ml_engineer.json
│   ├── data_engineer.json
│   ├── frontend_developer.json
│   └── backend_developer.json
└── requirements.txt

🧠 Skill Evaluation Logic

Each role is defined using a structured schema with:

Skills

Subskills

Measurable checkpoints

Importance weights

User responses are classified into:

none, partial, complete

Scores are aggregated from:

Checkpoint → Subskill → Skill

Priority areas are computed by combining:

Role-specific importance weight

Learner’s proficiency score

This ensures high-impact gaps are prioritized in the roadmap.

🤖 AI Flow

The AI layer is used to:

Generate scenario-based questions per checkpoint

Interpret free-text responses into structured understanding levels

The final evaluation, prioritization, and recommendations are handled by rule-based logic for explainability and consistency.

This hybrid design ensures robustness while keeping the system adaptive and interactive.

🧪 Example User Journey

User selects a target role (e.g., Data Engineer)

User customizes the relevant skillset

The system asks scenario-based questions for each skill checkpoint

The AI evaluates responses in real time

The skill map updates dynamically

The final report displays:

Strengths

Needs Improvement

Skill Gaps

High Priority Focus

Recommended Next Steps

The user receives a personalized skill progression roadmap

⚙️ Local Setup (Optional)
git clone https://github.com/Puzzledcat06/Skill-Gap-Analyzer
cd Skill-Gap-Analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


Set Groq API key (Windows PowerShell):

$env:GROQ_API_KEY="your_api_key_here"

📦 Deployment

The application is deployed on Streamlit Cloud and can be accessed publicly:

👉 https://skill-gap-analyzer-mine.streamlit.app/

📌 Notes

The AI layer is modular and can be swapped with other providers (e.g., local LLMs via Ollama).

The current implementation demonstrates continuous evaluation and dynamic skill prioritization suitable for prototype and demo purposes.

🙌 Acknowledgements

Built as part of an AI skill evaluation challenge to demonstrate adaptive assessment logic, LLM integration, and user-focused learning recommendations.

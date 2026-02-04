import os
import json
from groq import Groq

MODEL = "llama-3.1-8b-instant"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Same fallback map as Ollama version
FALLBACK_SIGNALS = {
    "Feature Engineering": {
        "complete": ["target encoding", "frequency encoding", "high cardinality", "avoid one-hot", "mean encoding"],
        "partial": ["one-hot", "label encoding", "categorical encoding", "encoding"]
    },
    "SQL & Data Modeling": {
        "complete": ["star schema", "snowflake schema", "normalization", "fact table", "dimension table"],
        "partial": ["group by", "join", "index", "primary key"]
    },
    "ETL / Data Pipelines": {
        "complete": ["airflow", "dag", "orchestration", "batch vs streaming", "idempotent"],
        "partial": ["etl", "pipeline", "cron", "job scheduling"]
    },
    "JavaScript": {
        "complete": ["async/await", "promises", "event loop", "closures"],
        "partial": ["callback", "fetch", "then"]
    }
}

def interpret_response(skill_name: str, checkpoint_description: str, user_answer: str) -> dict:
    prompt = f"""
You are an expert technical interviewer evaluating a candidate.

Checkpoint:
{checkpoint_description}

User answer:
\"\"\"{user_answer}\"\"\"

Classify the candidate's understanding STRICTLY as one of:
- none
- partial
- complete

Return ONLY valid JSON in this exact format:
{{"understanding_level": "...", "justification": "..."}}
"""

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Return strict JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        max_tokens=96,
    )

    text = resp.choices[0].message.content.strip()

    try:
        parsed = json.loads(text[text.find("{"): text.rfind("}") + 1])
        if parsed.get("understanding_level") in {"none", "partial", "complete"}:
            return parsed
    except Exception:
        pass

    ans = user_answer.lower()
    signals = FALLBACK_SIGNALS.get(skill_name)
    if signals:
        if any(sig in ans for sig in signals["complete"]):
            return {"understanding_level": "complete", "justification": f"Strong {skill_name} concepts demonstrated."}
        if any(sig in ans for sig in signals["partial"]):
            return {"understanding_level": "partial", "justification": f"Some relevant {skill_name} concepts mentioned."}

    if len(ans.split()) > 20:
        return {"understanding_level": "partial", "justification": "Detailed response but unclear correctness."}

    return {"understanding_level": "none", "justification": "Did not demonstrate sufficient understanding."}

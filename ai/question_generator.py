import os
from groq import Groq

MODEL = "llama-3.1-8b-instant"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_question(skill_name: str, checkpoint_description: str) -> str:
    prompt = f"""
You are an interviewer assessing a candidate for a technical role.

Checkpoint:
{checkpoint_description}

Ask ONE concrete, scenario-based interview question.
The question MUST:
- Describe a realistic dataset or system (e.g., e-commerce users, transactions, logs, web app).
- Ask what the candidate would DO (design, choose, implement, debug).
Do NOT ask definition or theory-only questions.
Return only the question text. Do not include any answer or explanation.
"""

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Generate concise, scenario-based interview questions only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=64,
    )

    text = resp.choices[0].message.content.strip()

    for prefix in ["Question:", "Q:", "Question -", "\""]:
        if text.lower().startswith(prefix.lower()):
            text = text[len(prefix):].strip()

    if "Answer:" in text:
        text = text.split("Answer:")[0].strip()

    if "\n" in text:
        text = text.splitlines()[0].strip()

    if not text.endswith("?"):
        text = text.rstrip(".") + "?"

    return text

import streamlit as st
import os

from core.schema import load_role_schema
from core.evaluator import score_checkpoint, evaluate_subskill, evaluate_skill
from core.priority import calculate_priority, classify_skill
from core.recommendations import get_recommendations

from ai.question_generator import generate_question
from ai.response_interpreter import interpret_response

st.set_page_config(page_title="AI Skill Gap Analyzer", layout="wide")
st.title("🧠 AI Skill Gap Analyzer")
st.caption("Interactive, role-based skill assessment with AI-driven evaluation")

st.markdown("""
This AI-powered Skill Gap Analyzer evaluates your current skills against a target job role.
You’ll answer scenario-based questions, and the system will identify strengths, areas for improvement,
and priority learning areas with a personalized roadmap.
""")

# --- Reset button ---
if st.button("🔄 Reset Assessment"):
    st.session_state.clear()
    st.experimental_rerun()

# --- Role selection ---
def list_roles():
    roles = {}
    for file in os.listdir("data"):
        if file.endswith(".json"):
            role_id = file.replace(".json", "")
            roles[role_id] = role_id.replace("_", " ").title()
    return roles

roles = list_roles()
selected_role_id = st.selectbox(
    "Select Target Role",
    list(roles.keys()),
    format_func=lambda x: roles[x]
)

schema = load_role_schema(selected_role_id)
st.subheader(f"Target Role: {schema['role_name']}")

# --- Skill customization ---
st.markdown("### Customize Skillset")
enabled_skills = {}
for skill in schema["skills"]:
    enabled_skills[skill["skill_name"]] = st.checkbox(
        f"{skill['skill_name']} ({skill['category']})",
        value=True
    )

st.divider()

# --- Interactive Assessment ---
st.markdown("## 📝 Interactive Skill Assessment")
results = []

for skill in schema["skills"]:
    if not enabled_skills.get(skill["skill_name"], True):
        continue

    st.markdown(f"### 🔹 {skill['skill_name']} ({skill['category']})")
    subskill_scores = []

    for subskill in skill["subskills"]:
        checkpoint_scores = []

        for checkpoint in subskill["checkpoints"]:
            question = generate_question(skill["skill_name"], checkpoint["description"])
            st.write("**Question:**", question)

            user_answer = st.text_area(
                "Your Answer:",
                key=f"{skill['skill_id']}_{checkpoint['checkpoint_id']}",
                placeholder="Type your answer here..."
            )

            if user_answer.strip():
                interp = interpret_response(
                    skill["skill_name"],
                    checkpoint["description"],
                    user_answer
                )

                score = score_checkpoint(interp["understanding_level"])
                checkpoint_scores.append(score)

                st.info(f"AI Feedback: {interp['justification']}")

        subskill_scores.append(evaluate_subskill(checkpoint_scores))

    skill_score = evaluate_skill(subskill_scores)
    priority = calculate_priority(skill["importance_weight"], skill_score)

    results.append({
        "skill": skill["skill_name"],
        "category": skill["category"],
        "score": round(skill_score, 2),
        "priority": round(priority, 2),
        "status": classify_skill(skill_score)
    })

# --- Structured Output ---
st.divider()
st.header("📊 Skill Gap Report")

skillset = [r["skill"] for r in results]
strengths = [r["skill"] for r in results if r["status"] == "strength"]
needs_improvement = [r["skill"] for r in results if r["status"] == "needs_improvement"]
gaps = [r["skill"] for r in results if r["status"] == "gap"]

priority_focus = [r["skill"] for r in sorted(results, key=lambda x: x["priority"], reverse=True)[:3]]

st.markdown(f"**Target Role:** {schema['role_name']}")
st.markdown(f"**Skillset:** {', '.join(skillset) if skillset else 'None selected'}")

st.markdown("**Strengths:**")
if strengths:
    for s in strengths:
        st.write(f"- {s}")
else:
    st.write("- None identified yet")

st.markdown("**Needs Improvement:**")
if needs_improvement:
    for n in needs_improvement:
        st.write(f"- {n}")
else:
    st.write("- None")

st.markdown("**Skill Gaps:**")
if gaps:
    for g in gaps:
        st.write(f"- {g}")
else:
    st.write("- No major gaps identified")

st.markdown("**High Priority Focus:**")
for p in priority_focus:
    st.write(f"- {p}")

st.markdown("**Recommended Next Steps:**")
if priority_focus:
    for skill_name in priority_focus:
        recs = get_recommendations(skill_name)
        for rec in recs:
            st.write(f"- {rec}")
else:
    st.write("- No immediate priority areas identified")

st.success("Assessment complete. Use the roadmap above to guide your learning journey.")

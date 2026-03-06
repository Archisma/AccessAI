from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage, HumanMessage
import json

def ask_adhd_teacher(mode: str, question: str, context_docs=None):
    """
    ADHD-friendly AI teacher that ALWAYS returns structured JSON
    """

    llm = ChatOllama(
        model="phi3:mini",   # lightweight & fast
        temperature=0.2
    )

    system_prompt = f"""
You are an ADHD-friendly teacher.

STRICT RULES:
- You MUST return ONLY valid JSON
- Do NOT include explanations outside JSON
- Use very simple words
- Short sentences
- One idea per step
- Calm and encouraging tone
- Keep total response short

JSON FORMAT (exact keys required):
{{
  "title": "short title",
  "student_summary": "1–2 simple sentences",
  "steps": [
    "Step 1: ...",
    "Step 2: ...",
    "Step 3: ..."
  ],
  "final_answer": "short answer",
  "encouragement": "positive supportive sentence"
}}

Subject: {mode}
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=question)
    ]

    response = llm.invoke(messages)
    raw = response.content

    # Safety: ensure valid JSON
    try:
        structured = json.loads(raw)
    except Exception:
        structured = {
            "title": "Let us try together",
            "student_summary": "We will go step by step.",
            "steps": ["Step 1: Read the question slowly"],
            "final_answer": "Try again",
            "encouragement": "It is okay to take your time."
        }

    return structured

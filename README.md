# AccessAI – ADHD Friendly AI Teacher

AccessAI is an AI-powered learning assistant designed to help **students with ADHD learn in a calm, structured, step-by-step way**.

The system combines **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and structured prompting** to generate explanations that avoid cognitive overload and support focused learning.

Instead of long explanations, AccessAI delivers **simple instructions, small steps, and encouragement**, making learning easier to follow.

---

## Problem

Many AI tutors produce **long and complex explanations**, which can overwhelm students with ADHD.

Students with ADHD benefit from:

- Short instructions
- Step-by-step guidance
- Clear structure
- Encouraging feedback

AccessAI addresses this by forcing the AI to produce **structured ADHD-friendly responses**.

---

## Features

### ADHD-Friendly Teaching Style
The AI responses follow strict rules:

- Simple language
- Short sentences
- One step at a time
- Calm and supportive tone

### Step-by-Step Learning
Each response contains:

- Short explanation
- Guided steps
- Final answer
- Encouragement
- Quick understanding check

### Multiple Subjects

The assistant currently supports:

- Math
- English
- Cognitive Skills
- General Knowledge

### Retrieval-Augmented Generation (RAG)

AccessAI retrieves relevant learning material from a **vector database** before generating responses, improving accuracy and context.

---

## Architecture

Frontend (HTML Interface)
        |
        v
FastAPI Backend
        |
        v
AI Teacher Module
        |
        v
Vector Database (ChromaDB)
        |
        v
Subject Knowledge Files

---

## Tech Stack

### Backend
- Python
- FastAPI

### AI / ML
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Local LLM (Phi-3 Mini)

### Frontend
- HTML
- JavaScript

---

## Project Structure

```
AccessAI
│
├── main.py
├── ai_teacher.py
├── prompts.py
├── vector_store.py
│
├── data
│   ├── math.txt
│   ├── english.txt
│   ├── cognitive.txt
│   └── gk.txt
│
├── index.html
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/accessai-adhd-teacher.git
cd accessai-adhd-teacher
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the backend server

```
uvicorn main:app --reload
```

---

## Example API Request

POST `/ask`

Request

```
{
  "mode": "math",
  "question": "What is 24 divided by 6?"
}
```

Example Response

```
{
  "title": "Division",
  "student_summary": "We divide numbers to see how many equal groups we can make.",
  "steps": [
    "Step 1: Look at the numbers",
    "Step 2: Divide 24 by 6",
    "Step 3: Check your answer"
  ],
  "final_answer": "4",
  "encouragement": "Great work!"
}
```

---

## Hackathon Project

This project was built during an **AI Hackathon** to explore how generative AI can support **inclusive education and neurodivergent learners**.

---

## Future Improvements

- Voice interaction for students
- Adaptive learning difficulty
- Learning progress tracking
- Mobile-friendly interface
- Multi-language support

---

## Author

**Archisma Ghosal**

AI Engineer working on:

- Generative AI  
- Retrieval-Augmented Generation (RAG)  
- Agentic AI systems  
- Production AI applications

AccessAI – ADHD Friendly AI Teacher

AccessAI is an AI-powered learning assistant designed to help students with ADHD learn in a calm, structured, step-by-step way.

The system combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and structured prompting to provide explanations that avoid cognitive overload and support focused learning.

Instead of long explanations, AccessAI delivers simple instructions, small steps, and encouragement, making learning easier to follow.

Problem

Traditional AI tutors often produce long and complex explanations, which can overwhelm students with ADHD or attention difficulties.

Students with ADHD benefit from:

Short instructions

One step at a time guidance

Clear structure

Encouraging feedback

AccessAI addresses this by forcing the AI to produce structured responses designed for ADHD-friendly learning.

Features
ADHD-Friendly Teaching

The AI responses follow strict rules:

Simple words

Short sentences

One step at a time

Calm and supportive tone

Step-by-Step Learning

Each answer includes:

Short explanation

Guided steps

Final answer

Encouragement

Quick understanding check

Multiple Subjects

The assistant currently supports:

Math

English

Cognitive Skills

General Knowledge

Retrieval-Augmented Generation (RAG)

The system retrieves relevant learning material from a vector database before generating answers, improving accuracy and context.

Architecture
Frontend (HTML Interface)
        |
        v
FastAPI Backend
        |
        v
AI Teacher Module
        |
        v
Vector Database (Chroma)
        |
        v
Subject Knowledge Files
Tech Stack

Backend

Python

FastAPI

AI / ML

LangChain

ChromaDB

HuggingFace Embeddings

Local LLM (Phi-3 Mini)

Frontend

HTML

JavaScript

Project Structure
AccessAI
│
├── main.py                # FastAPI server
├── ai_teacher.py          # ADHD-friendly AI logic
├── prompts.py             # Structured prompt rules
├── vector_store.py        # RAG vector database setup
│
├── data
│   ├── math.txt
│   ├── english.txt
│   ├── cognitive.txt
│   └── gk.txt
│
├── index.html             # Frontend interface
├── requirements.txt
└── README.md
Installation

Clone the repository

git clone https://github.com/yourusername/accessai-adhd-teacher.git
cd accessai-adhd-teacher

Install dependencies

pip install -r requirements.txt

Run the backend server

uvicorn main:app --reload

Open the application in your browser.

Example API Request

POST request to /ask

Request

{
  "mode": "math",
  "question": "What is 24 divided by 6?"
}

Example Response

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
Hackathon Project

This project was developed during an AI Hackathon to explore how generative AI can improve inclusive education and accessibility for neurodivergent learners.

Future Improvements

Voice interaction for students

Adaptive learning difficulty

Learning progress tracking

Mobile-friendly interface

Multi-language support

Author

Archisma Ghosal

AI Engineer focused on:

Generative AI

Retrieval-Augmented Generation (RAG)

Agentic AI systems

Production AI applications

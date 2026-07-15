import os
from dotenv import load_dotenv
from crewai import LLM

# Load .env file
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini LLM
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=GEMINI_API_KEY
)

PROJECT_NAME = "Create a Library Management System"
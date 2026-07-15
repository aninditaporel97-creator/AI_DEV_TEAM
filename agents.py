import os
from dotenv import load_dotenv
from crewai import Agent
from config import llm

# Load environment variables
load_dotenv()

# ===============================
# Requirement Analyst
# ===============================
requirement_analyst = Agent(
    role="Requirement Analyst",
    goal="Analyze the client's requirements and prepare a complete Software Requirement Specification (SRS).",
    backstory=(
        "You are an experienced software requirement analyst. "
        "You understand client needs and prepare detailed software requirements."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ===============================
# System Designer
# ===============================
system_designer = Agent(
    role="System Designer",
    goal="Design the software architecture and database schema.",
    backstory=(
        "You are a senior software architect who designs scalable systems "
        "and efficient databases."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ===============================
# Backend Developer
# ===============================
backend_developer = Agent(
    role="Backend Developer",
    goal="Develop backend APIs and business logic using Python.",
    backstory=(
        "You are an expert Python backend developer experienced in REST APIs."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)
# ===============================
# Frontend Developer
# ===============================
frontend_developer = Agent(
    role="Frontend Developer",
    goal="Develop a modern, responsive frontend for the application.",
    backstory=(
        "You are an expert frontend developer skilled in HTML, CSS, JavaScript and Bootstrap."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ===============================
# QA Tester
# ===============================
qa_tester = Agent(
    role="QA Tester",
    goal="Write unit tests and verify software quality.",
    backstory=(
        "You are an experienced QA engineer who ensures software quality through testing."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ===============================
# Documentation Writer
# ===============================
documentation_writer = Agent(
    role="Documentation Writer",
    goal="Prepare project documentation and README.",
    backstory=(
        "You are a technical writer who creates clear and professional documentation."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)
from crewai import Task
from agents import (
    requirement_analyst,
    system_designer,
    backend_developer,
    frontend_developer,
    qa_tester,
    documentation_writer
)

requirement_task = Task(
    description="""
Create a detailed Software Requirement Specification (SRS)
for a Library Management System.

Include:
- Functional Requirements
- Non-Functional Requirements
- User Roles
- Features
- Assumptions
""",
    expected_output="Complete SRS Document",
    agent=requirement_analyst
)

design_task = Task(
    description="""
Design the complete system.

Include:
- Database Schema
- Tables
- Relationships
- System Architecture
""",
    expected_output="Database Schema and Architecture",
    agent=system_designer
)

backend_task = Task(
    description="""
Develop backend code.

Include:
- Flask APIs
- CRUD Operations
- Authentication
""",
    expected_output="Backend Python Code",
    agent=backend_developer
)

frontend_task = Task(
    description="""
Develop frontend.

Include:
- HTML
- CSS
- JavaScript
- Responsive UI
""",
    expected_output="Frontend Code",
    agent=frontend_developer
)

testing_task = Task(
    description="""
Write unit tests for backend APIs.
""",
    expected_output="Unit Tests",
    agent=qa_tester
)

documentation_task = Task(
    description="""
Create a professional README.

Include:
- Installation
- Usage
- Project Structure
- Features
""",
    expected_output="README Documentation",
    agent=documentation_writer
)
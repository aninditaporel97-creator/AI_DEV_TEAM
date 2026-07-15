from crewai import Crew, Process

from agents import (
    requirement_analyst,
    system_designer,
    backend_developer,
    frontend_developer,
    qa_tester,
    documentation_writer
)

from tasks import (
    requirement_task,
    design_task,
    backend_task,
    frontend_task,
    testing_task,
    documentation_task
)

crew = Crew(
    agents=[
        requirement_analyst,
        system_designer,
        backend_developer,
        frontend_developer,
        qa_tester,
        documentation_writer
    ],

    tasks=[
        requirement_task,
        design_task,
        backend_task,
        frontend_task,
        testing_task,
        documentation_task
    ],

    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(
    inputs={
        "project": "Create a Library Management System"
    }
)

print("\n\n========== FINAL OUTPUT ==========\n")
print(result)
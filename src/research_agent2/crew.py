from crewai import Agent, Task, Crew
from crewai_tools import CodeInterpreterTool

# Initialize the tool
code_interpreter = CodeInterpreterTool()

# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Code Analyzer",
    goal="Analyze and provide insights on Python code.",
    backstory="An experienced AI code reviewer that evaluates Python code for correctness and optimization.",
    tools=[code_interpreter],
)



	# Create a task that requires code execution
code_analysis_task = Task(
	description="Analyze the given Python code and provide insights.",
	expected_output="A detailed analysis of the given Python code, highlighting improvements and errors.",
	agent=coding_agent,
)

	# Create a crew and add the task
crew = Crew(
	agents=[coding_agent],
	tasks=[code_analysis_task]
	)

	# Execute the crew
def go():
	print("Code Analysis Result:")
	result = crew.kickoff()
	print(result)

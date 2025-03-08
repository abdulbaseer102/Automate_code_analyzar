from crewai import Agent, Task, Crew
from IPython.display import Markdown
# Initialize the tool

# Create an agent with code execution enabled
coding_agent = Agent(
    role="Python Code Analyzer",
    goal="Analyze and provide insights on Python code:{topic}.",
    backstory="An experienced AI code reviewer that evaluates Python code for correctness and optimization.",
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
	tasks=[code_analysis_task],
	varbose=False
	)


	# Execute the crew
def go():
	print("Code Analysis Result:")
	topic = "print('hello world')"
	result = crew.kickoff(inputs={"topic": topic})
    
	print(result)
	

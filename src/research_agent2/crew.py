from crewai import Agent, Task, Crew,LLM,Process
from IPython.display import Markdown
import os
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

planning_llm = LLM(
	model = "gemini/gemini-1.5-flash",
	api_key = "GEMINI_API_KEY",
)

crew = Crew(
	agents=[coding_agent],
	tasks=[code_analysis_task],
	planning=True,
	planning_llm=planning_llm,
	varbose=False
	)


	# Execute the crew
def go():
	print("Code Analysis Result:")
	topic = """
	import requests

API_KEY = "your_api_key"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather.capitalize()}\n")
    else:
        print("City not found. Please try again.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)

	
	"""
	result = crew.kickoff(inputs={"topic": topic})
    
	print(result)
	

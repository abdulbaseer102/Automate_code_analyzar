#!/usr/bin/env python3

import os
import yaml
from crewai import Agent, Task, Crew, Process
from crewai_tools import CodeInterpreterTool
import warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore")

# Initialize the tool
code_interpreter = CodeInterpreterTool()

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(BASE_DIR, "config")

def load_yaml(filename):
    """Load YAML configuration files from the config directory."""
    file_path = os.path.join(CONFIG_DIR, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"⚠️ YAML file not found: {file_path}")
    
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def setup_crew():
    """Set up the Crew with agents and tasks from YAML configurations."""
    # Load YAML files
    agents_config = load_yaml("agents.yaml")
    tasks_config = load_yaml("tasks.yaml")

    # Create agents using config parameter
    game_developer = Agent(config=agents_config["game_developer"],tools=[code_interpreter])
    code_quality_engineer = Agent(config=agents_config["code_quality_engineer"])
    game_tester = Agent(config=agents_config["game_tester"])

    # Create tasks using config parameter and explicit agent assignment
    game_code_generation = Task(
        description="""
         Create a Python game following these instructions:

         instructions
         {game_description}

    - The player should be represented using a **blue rectangle**.
    - The enemy should be represented using a **red circle**.
    - The bullet should be represented using a **green rectangle**.
    - Do NOT use images, only use `pygame.draw` functions.
    - The final answer must be the **full Python code**, with no explanations.
        """,
        expected_output = """
         A fully functional Python script implementing the game using `pygame.draw` for all objects.

        """,

        agent=game_developer
    )
    code_review_and_bug_fixes = Task(
        config=tasks_config["code_review_and_bug_fixes"],
        agent=code_quality_engineer
    )
    game_testing_and_validation = Task(
        config=tasks_config["game_testing_and_validation"],
        agent=game_tester,
        output_file="generated_game.py"  # Save the final output here
    )

    # Define Crew with sequential execution
    crew = Crew(
        agents=[game_developer, code_quality_engineer, game_tester],
        tasks=[game_code_generation, code_review_and_bug_fixes, game_testing_and_validation],
        process=Process.sequential,
        verbose=False
    )
    return crew

   
def go(crew,game_description):
    """Generate game code using the Crew."""
    print("\n🚀 Starting the Game Generation Process...\n")
    
    # Run the Crew with the game description as input
    result = crew.kickoff(inputs={"game_description": game_description})
    
    print("\n🎮 Game Code Generated Successfully!\n")
    print(result.raw)  # Print the final output for verification
    
    print("\n✅ The generated game code has been saved as 'generated_game.py'. You can now run and test it!\n")

def main():
    """Main execution function."""
    try:
        # Set up the crew
        crew = setup_crew()
        print("🚀 Crew setup completed successfully!")

        # Define the game concept
        game_description = (
            "A simple 2D space shooter game where the player controls a spaceship "
            "and must defeat waves of enemy ships while collecting power-ups."
        )

        # Generate the game
        go(crew,game_description)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
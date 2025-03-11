# Game Generation AI using CrewAI

## 📌 Overview
This project utilizes **CrewAI** to automate the development of a simple **2D space shooter game** using `pygame`. The AI agents are responsible for generating, reviewing, and testing game code, ensuring a fully functional and optimized result.

## 🏗 Project Structure
```
/project-root
│── config/
│   ├── agents.yaml  # Configuration for AI agents
│   ├── tasks.yaml   # Configuration for tasks
│── src/
│   ├── main.py      # Main script to run the CrewAI workflow
│── generated_game.py  # Final output file containing the generated game
│── README.md        # Project documentation
```

## 🎯 Key Features
- **AI-powered game development**: Automates the creation of `pygame`-based games.
- **Multi-agent collaboration**: Utilizes CrewAI for structured task delegation.
- **Game testing & debugging**: Ensures code quality and correctness before finalizing.
- **Config-driven workflow**: Uses YAML files for easy customization of AI behavior.

## 🚀 How It Works
### 1️⃣ Agents
This project defines three AI agents:
- **Game Developer**: Generates the game code based on the given description.
- **Code Quality Engineer**: Reviews the code for errors and optimizations.
- **Game Tester**: Validates the game’s functionality and ensures proper execution.

### 2️⃣ Tasks
Each agent is assigned specific tasks:
- **Game Code Generation** → AI writes the complete game script.
- **Code Review & Bug Fixes** → AI reviews and improves the code.
- **Game Testing & Validation** → AI runs and verifies the game logic.

### 3️⃣ Workflow
The process runs **sequentially**:
1. **Game Developer** writes the game code.
2. **Code Quality Engineer** reviews & fixes issues.
3. **Game Tester** runs the game & confirms functionality.
4. The final game code is saved in `generated_game.py`.

## ⚙️ Installation
### 🔹 Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **pip**
- **virtualenv** (optional, but recommended)

### 🔹 Step-by-Step Setup
1️⃣ **Clone the repository**
```bash
git clone https://github.com/your-repo/game-generation-ai.git
cd game-generation-ai
```

2️⃣ **Create & activate a virtual environment** (optional but recommended)
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Set up environment variables**
```bash
export GEMINI_API_KEY="your-api-key-here"  # macOS/Linux
set GEMINI_API_KEY=your-api-key-here  # Windows (cmd)
$env:GEMINI_API_KEY="your-api-key-here"  # Windows (PowerShell)
```

## ▶️ Running the Project
To start the AI-powered game generation process, run:
```bash
python src/main.py
```

## 📂 Configuration
### 🔹 Agents Configuration (`config/agents.yaml`)
Modify agent settings such as name, role, and expertise:
```yaml
game_developer:
  name: "Game Developer"
  role: "Writes Python game code using pygame"
  expertise: "Expert in Python game development"
```

### 🔹 Tasks Configuration (`config/tasks.yaml`)
Define expected outputs and execution logic:
```yaml
code_review_and_bug_fixes:
  description: "Review game code for errors and improve quality"
  expected_output: "A cleaner, optimized Python script"
```

## 🔥 Example Output
Once the process completes, you’ll see:
```
🚀 Starting the Game Generation Process...
🎮 Game Code Generated Successfully!
✅ The generated game code has been saved as 'generated_game.py'.
```

## 🛠 Troubleshooting
- **Issue: `GEMINI_API_KEY is not set`**
  - Ensure you've exported the API key correctly.
  - Run `echo $GEMINI_API_KEY` (Linux/macOS) or `echo %GEMINI_API_KEY%` (Windows) to verify.

- **Issue: `ModuleNotFoundError: No module named 'crew'`**
  - Ensure you've installed dependencies with `pip install -r requirements.txt`.

## 📜 License
This project is licensed under the **MIT License**.

## 💡 Future Improvements
- Support for multiple game genres
- AI-driven difficulty balancing
- Improved debugging and optimization techniques

---
🔹 **Developed using CrewAI & Gemini API** 🚀


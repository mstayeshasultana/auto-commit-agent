# 🤖 AutoCommit Agentic AI



<img width="973" height="728" alt="image" src="https://github.com/user-attachments/assets/8a20be6f-ce34-417b-88ec-235836965a50" />





**AutoCommit Agent** is an AI-powered CLI tool that automates Git commits for **Dart / Flutter** projects.  
It reads code changes, generates meaningful commit messages following **Conventional Commits**, and stages, commits, and pushes changes **after user confirmation**.

---

## ✨ Features

- 🔍 Automatically detects changes using `git status` and `git diff`
- 🧠 Generates concise, meaningful commit messages using AI  
  - OpenAI (GPT-4 / GPT-3.5)
  - Ollama (self-hosted models)
- ✅ Asks for confirmation before committing and pushing
- 🧾 Follows **Conventional Commits** style
- 🚀 Easy to run with a single command: `push-ai`
- 🔧 Can be extended with PR descriptions and branch safety checks

---

## 🛠 Installation & Setup

### Step 1: Install Required Tools


1️⃣ Git
   Check if installed:  
 
   git --version

If missing, download: Git Downloads


If missing, download Git from:
👉 https://git-scm.com/downloads

2️⃣ Python

Check if Python is installed:

python --version


If missing, download Python from:
👉 https://www.python.org/downloads/

3️⃣ GitHub CLI

Download GitHub CLI:
👉 https://cli.github.com/

Login to GitHub:

gh auth login

📂 Step 2: Download AutoCommit Agent Files

Download and keep the following files in the same folder:

ai_push.py
push-ai.bat

🧩 Step 3: Add push-ai to PATH (Windows)
Option 1 (Not Recommended)

Move push-ai.bat to:

C:\Windows\System32

✅ Option 2 (Recommended)

Create a folder:

C:\ai-tools\


Move push-ai.bat into:

C:\ai-tools\

🔑 Step 4: Add Folder to PATH

Press Windows Key

Type Environment Variables

Click Edit the system environment variables

Click Environment Variables…

Under User variables, find Path

Click Edit

Click New

Add:

C:\ai-tools\


Click OK on all windows

Restart your terminal



🔐 Step 5: Get Your OpenAI API Key

5.1 Open OpenAI Platform

👉 https://platform.openai.com/


5.2 Log In

Log in using the same account you use for ChatGPT Plus.

5.3 Open API Keys Page

Click your profile icon (top-right)

Click View API keys

OR open directly:
👉 https://platform.openai.com/account/api-keys




5.4 Create New Secret Key

Click + Create new secret key

Copy the key immediately

⚠️ You won’t be able to see it again

Example:

sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx





⚙️ Step 6: Set OpenAI API Key

In PowerShell:

setx OPENAI_API_KEY "your_api_key_here"


Restart the terminal.

Verify:

echo $env:OPENAI_API_KEY




📦 Step 7: Install OpenAI Python Library
pip install openai

🧠 Step 8: Configure API Key in Script

Inside ai_push.py:

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

🚀 Usage

From any Git repository, run:

push-ai

📸 Example Output


🔍 Checking git status...

 M lib/screens/login.dart

🧠 Generating commit message...

➡️ fix: resolve null crash in login validation

Proceed with commit & push? (y/n): y

🎉 SUCCESS! Changes committed and pushed.



🧾 Commit Message Format

AutoCommit Agent follows Conventional Commits:

feat: add user authentication flow
fix: resolve null crash in login validation
refactor: clean up auth service logic
docs: update README instructions

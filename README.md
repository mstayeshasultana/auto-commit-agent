


<img width="1024" height="874" alt="ChatGPT Image Feb 9, 2026, 01_29_d27 PM" src="https://github.com/user-attachments/assets/a463fc36-b91c-4e5b-b068-5cf26bc862fb" />

# 🧠 AutoCommit Agentic AI

An AI-powered agent that automates the Git commit workflow using GPT.  
Built with **LangGraph**, **LangChain**, and the **Git CLI**, this agent generates meaningful commit messages by analyzing code changes, confirming with the user, and pushing to the repository.

---

## 🚀 Features

- 📄 Reads `git status` and `git diff`
- 🧠 Uses GPT (via OpenAI) to generate commit messages
- 🧾 Follows [Conventional Commits](https://www.conventionalcommits.org/) style
- 🔄 Confirms with the user before committing
- ✅ Stages, commits, and pushes automatically
- ⚙️ Built with a stateful LangGraph workflow (modular & extendable)

---

## 🧱 How It Works

1. **Check Git Status** – Detects if there are changes
2. **Read Diff** – Captures all changes to be committed
3. **Generate Commit Message** – GPT crafts a meaningful message
4. **Ask for Confirmation** – Human-in-the-loop safety
5. **Commit & Push** – Automatically executes Git commands

Each step is a **LangGraph node**, and the system uses shared state to track and control the workflow.

---

## 💡 Technologies

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)
- Python 3.11+
- Git (CLI)
- Runs on Linux, macOS, Windows (with Git installed)

---

## 🛠️ Step-by-Step Setup: Git Commit Copilot Agent

### Step 1: Install Requirements

#### Install Git

Check if Git is installed:

```bash
git --version
```

If not installed, download it from:  
[https://git-scm.com/downloads](https://git-scm.com/downloads)

---

#### Install Python

Check if Python is installed:

```bash
python --version
```

Download if missing:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

#### Install GitHub CLI (optional, for extended features)

Download:  
[https://cli.github.com/](https://cli.github.com/)

Login with:

```bash
gh auth login
```

---

### Step 2: Install Python Libraries

```bash
pip install langchain langgraph openai
```

---

### Step 3: Download the Agent Script

Save the file as:

```bash
git_copilot.py
```

You can rename it, but keep the extension `.py`.

---

### Step 4: Set Your OpenAI API Key

#### How to Get Your `OPENAI_API_KEY`

1. Go to: [https://platform.openai.com/](https://platform.openai.com/)  
2. Log in using your ChatGPT account  
3. Click your profile icon (top right) → "View API Keys"  
   Or go directly to: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)  
4. Click **"Create new secret key"**  
   - You will get a key like: `sk-xxxxxxxxxxxxxxxxxxxxx`
   - **Copy it immediately** — you can't see it again!

---

#### Set the key in your terminal (Windows):

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Then restart your terminal and test it with:

```bash
echo %OPENAI_API_KEY%
```

✅ You should see your key printed.

---

#### Note on Billing

You must have a valid OpenAI billing account to use the API:  
[https://platform.openai.com/account/billing](https://platform.openai.com/account/billing)

A small $5 credit is enough to run this agent.

---

### Step 5: (Optional) Create a Shortcut Command

#### For Windows (Batch File Setup)

1. Create a folder, e.g.:

```
C:\ai-tools\
```

2. Move both `git_copilot.py` and `autocommit.bat` into that folder.

3. Add the folder to your system PATH:
   - Search for **Environment Variables**
   - Edit the system PATH
   - Add: `C:\ai-tools\`

4. Restart your terminal

Now you can run the command from anywhere.

---

### Step 6: Run the Agent

In any Git repository, run:

```bash
autocommit
```

If there are changes, the agent will:
- Detect modified files
- Generate a commit message with GPT
- Ask for confirmation
- Push the changes

---

### Example Output

```text
C:\Users\...\Documents\Flutter_Projects\my_app> autocommit

🔍 Changes found:
 M lib/screens/message/chat_screen.dart
 M lib/screens/profile/people_profile/people_profile_screen.dart

Suggested Commit Message:
➡️ feat: Add user details screen navigation in chat_screen.dart
    - Added navigation to the UserDetailsScreen when tapping on the user avatar in the ChatScreen title.
    - This allows users to view more details about the chat partner.

Proceed with commit & push? (y/n): y

📌 Staging files...
Committing...
[develop 99xyz43] feat: Add user details screen navigation in chat_screen.dart
 2 files changed, 363 insertions(+), 131 deletions(-)
 create mode 100644 lib/screens/message/user_details_screen.dart
Pushing...

SUCCESS! Changes pushed.
```







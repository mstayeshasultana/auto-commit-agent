# 🧠 Git Commit Copilot Agent

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


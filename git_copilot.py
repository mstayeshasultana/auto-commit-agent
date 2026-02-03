
import os
import subprocess
from typing import TypedDict, Literal

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

os.environ["OPENAI_API_KEY"] = ""  # <-- put your key here

# State 
class GitState(TypedDict, total=False):
    status: str
    diff: str
    message: str
    confirmed: Literal["yes", "no"]

# LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

# Node 1: Check Git Status
def check_status(_: GitState) -> GitState:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        encoding="utf-8",      # ✅ FIX: Windows encoding
        errors="replace"       # ✅ FIX: Prevent Unicode crash
    )

    status = (result.stdout or "").strip()

    if not status:
        print("✅ No changes found.")
        exit()

    print("🔍 Changes found:\n", status)
    return {"status": status}

#  Node 2: Get Git Diff
def get_diff(state: GitState) -> GitState:
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True,
        text=True,
        encoding="utf-8",      # ✅ FIX: Windows encoding
        errors="replace"
    )

    diff = (result.stdout or "").strip()

    return {
        **state,
        "diff": diff
    }

#  Node 3: Generate Commit Message
def generate_commit(state: GitState) -> GitState:
    prompt = f"""
You are a Git Commit Copilot Agent specialized in Dart/Flutter.

Rules:
- Use Conventional Commits format
- Types: feat, fix, ui, refactor, docs, chore
- Message must be meaningful
- Max 10 sentences
- Include file name or class name from the actual code changes
- Do not write commit messages for files or lines that have not changed
- Return ONLY the commit message

Git Status:
{state['status']}

Git Diff:
{state['diff']}
"""

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    message = response.content.strip()

    print("🧠 Suggested Commit Message:")
    print("➡️", message)

    return {
        **state,
        "message": message
    }

# Node 4: User Confirmation
def confirm_commit(state: GitState) -> GitState:
    answer = input("\nProceed with commit & push? (y/n): ").lower()

    return {
        **state,
        "confirmed": "yes" if answer == "y" else "no"
    }

#  Node 5: Commit & Push
def commit_push(state: GitState) -> GitState:
    print("\n📌 Staging files...")
    subprocess.run(["git", "add", "."])

    print("📝 Committing...")
    subprocess.run(["git", "commit", "-m", state["message"]])

    print("🚀 Pushing...")
    subprocess.run(["git", "push"])

    print("\n🎉 SUCCESS! Changes pushed.")
    return state

#  LangGraph Workflow
graph = StateGraph(GitState)

graph.add_node("status", check_status)
graph.add_node("diff", get_diff)
graph.add_node("generate", generate_commit)
graph.add_node("confirm", confirm_commit)
graph.add_node("commit", commit_push)

graph.set_entry_point("status")

graph.add_edge("status", "diff")
graph.add_edge("diff", "generate")
graph.add_edge("generate", "confirm")

graph.add_conditional_edges(
    "confirm",
    lambda s: "commit" if s["confirmed"] == "yes" else END
)

graph.add_edge("commit", END)

copilot_agent = graph.compile()

#  Run Agent
copilot_agent.invoke({})

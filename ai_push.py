

import subprocess
import os
from openai import OpenAI

# Create OpenAI client
client = OpenAI(api_key=os.getenv("Your-Open-AI-Key"))

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True, encoding="utf-8", errors="replace")


print("\n🔍 Checking git status...\n")

status = run("git status --short")

if not status.strip():
    print("✅ No changes detected.")
    exit()

print("Changes found:\n", status)

print("\n📄 Reading git diff...\n")
diff = run("git diff")

prompt = f"""
You are a Git Commit Copilot Agent specialized in Dart/Flutter.

Rules:
- Use Conventional Commits format
- Types: feat, fix, ui, refactor, docs, chore
- Message size can be different as per the changes made
- Message size: not more than ten sentences
- Message should be meaningful


Git Status:
{status}

Git Diff:
{diff}

Return ONLY the commit message line.
"""

print("🧠 Generating commit message...\n")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

commit_msg = response.choices[0].message.content.strip()

print("✅ Suggested Commit Message:")
print("➡️", commit_msg)

confirm = input("\nProceed with commit & push? (y/n): ")

if confirm.lower() != "y":
    print("❌ Cancelled.")
    exit()

print("\n📌 Staging files...")
run("git add .")

print("📝 Committing...")
run(f'git commit -m "{commit_msg}"')

print("🚀 Pushing...")
run("git push")

print("\n🎉 SUCCESS! Changes pushed.")

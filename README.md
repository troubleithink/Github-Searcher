🔍 GitHub Repo & Commit Explorer

A simple Python script that pulls public data straight from the GitHub API 🐙

✨ What it does
📝 Enter any GitHub username
📦 Fetches all public repositories for that user
💾 Digs into each repo's commit history
🆔 Prints out the commit SHA and the author's email for every commit found
⚙️ How it works
Sends a request to api.github.com/users/{username}/repos to list repos
Loops through each repo and hits api.github.com/repos/{username}/{repo}/commits
Extracts and prints commit sha + author email 📧
Handles connection errors and bad responses gracefully ✅
🛠️ Built with
Python 🐍
requests library
🚀 Usage
bash
python Github_search.py

Just type in a GitHub username when prompted, and watch the console fill up with commit data!

# 🔍 GitHub Repo & Commit Explorer

A simple Python script that pulls public data straight from the **GitHub API** 🐙 — enter a username and get a full rundown of their repos and commit history.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/requests-library-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

- 📝 Enter any GitHub username
- 📦 Fetches **all public repositories** for that user
- 💾 Digs into each repo's **commit history**
- 🆔 Prints the commit SHA and author email for every commit found
- ✅ Graceful error handling for connection issues & bad API responses

---

## ⚙️ How It Works

1. Sends a request to `api.github.com/users/{username}/repos` to list repos
2. Loops through each repo and hits `api.github.com/repos/{username}/{repo}/commits`
3. Extracts and prints commit `sha` + author `email` 📧
4. Skips/logs any commit that can't be parsed, instead of crashing

---

## 🛠️ Built With

- 🐍 [Python 3](https://www.python.org/)
- 🌐 [`requests`](https://pypi.org/project/requests/)

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install requests
```

### Run it
```bash
python Github_search.py
```

Then just type in a GitHub username when prompted:

```
Gib einen GitHub Usernamen ein: octocat
```

---

## 📋 Example Output

```
id: a1b2c3d4e5f6...
email: someone@example.com

id: f6e5d4c3b2a1...
email: another@example.com
```

---

## ⚠️ Notes

- This tool only accesses **public** data available through GitHub's public REST API.
- No authentication token is used, so it's subject to GitHub's **unauthenticated rate limits** (60 requests/hour).
- Intended for **educational and research purposes** — please respect GitHub's [Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) and don't use this for scraping/harassment.

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

Made with ❤️ and Python (AI)

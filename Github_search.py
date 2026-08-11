import requests

def hole_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Fehler beim Verbinden mit GitHub")
        return []
    if response.status_code != 200:
        print(f"Fehler beim Abrufen der Repos, Status: {response.status_code}")
        return []
    return response.json()

def hole_commits(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Fehler beim Verbinden mit GitHub")
        return []
    if response.status_code != 200:
        print(f"Fehler beim Abrufen der Commits fuer {repo_name}, Status: {response.status_code}")
        return []
    return response.json()

def main():
    print("made by Gamer")
    print("")

    username = input("Gib einen GitHub Usernamen ein: ")
    repos = hole_repos(username)

    if not repos:
        print("Keine repos")
        return

    for repo in repos:
        repo_name = repo.get("name")
        commits = hole_commits(username, repo_name)

        for commit in commits:
            try:
                sha = commit["sha"]
                email = commit["commit"]["author"]["email"]
                print(f"id: {sha}")
                print(f"email: {email}")
                print("")
            except (KeyError, TypeError):
                print("Fehler beim Lesen dieses Commits")
                print("")

main()

print("Beenden")
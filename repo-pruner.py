import os
import sys
import requests
from dotenv import load_dotenv

ENV_FILE = ".env"


def setup_token():
    # If there is a existing .env, load it.
    load_dotenv()

    token = os.getenv("GITHUB_TOKEN")
    if token:
        print("\nToken found and loaded.")
        return token

    print("No GitHub token found.")
    print("Enter a GitHub Personal Access Token.")
    print("It will be saved to a local .env file for future use.\n")

    token = input("GitHub Token: ").strip()

    if not token:
        print("No token provided.")
        sys.exit(1)


    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write(f"GITHUB_TOKEN={token}\n")

    # Reload environment
    load_dotenv(override=True)

    print("Token saved to .env\n")

    return os.getenv("GITHUB_TOKEN")


GITHUB_TOKEN = setup_token()

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_repositories():
    repos = []
    page = 1

    while True:
        url = (
            f"https://api.github.com/user/repos"
            f"?per_page=100&page={page}&affiliation=owner"
        )

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("Error:", response.text)
            sys.exit(1)

        data = response.json()

        if not data:
            break

        repos.extend(data)
        page += 1

    return repos


def delete_repo(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Deleted {owner}/{repo}")
    else:
        print(f"Failed to delete {owner}/{repo}")
        print(response.text)


def main():
    repos = get_repositories()

    print(f"\nFound {len(repos)} repositories.\n")

    for repo in repos:
        owner = repo["owner"]["login"]
        name = repo["name"]
        visibility = "Private" if repo["private"] else "Public"

        answer = input(
            f"{owner}/{name} ({visibility}) -> Delete? [y/N]: "
        ).strip().lower()

        if answer == "y":
            delete_repo(owner, name)
        else:
            print("Kept.")

    print("\nDone.")


if __name__ == "__main__":
    main()

# github-repo-pruner

An interactive CLI for reviewing and deleting GitHub repositories you own. Supports both public and private repositories with confirmation prompts to help prevent accidental deletion.

> **Warning**
>
> Deleted repositories are typically recoverable for up to **90 days** if they meet GitHub's restoration requirements. Delete repositories carefully.

## Features

* Lists all repositories you own
* Supports both **public** and **private** repositories
* Interactive confirmation for every repository
* Automatically saves your GitHub Personal Access Token to a local `.env` file on first run
* Simple, lightweight Python script

## Requirements

* Python 3.9+
* A GitHub Personal Access Token (PAT) with permission to delete repositories

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/github-repo-pruner.git
cd github-repo-pruner
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests python-dotenv
```

## Usage

Run the script:

```bash
python repo_pruner.py
```

The first time you run it, you'll be prompted for your GitHub Personal Access Token. The token is stored locally in a `.env` file and reused on future runs.

For each repository, you'll see a prompt similar to:

```text
username/my-repository (Public) -> Delete? [y/N]:
```

* Enter **y** to permanently delete the repository.
* Press **Enter** or type **n** to keep it.

## Creating a GitHub Personal Access Token

Create a Personal Access Token with the permissions required to delete repositories. Make sure it has access to the repositories you want to manage.

## Security

Your GitHub token is stored locally in a `.env` file.

This project's `.gitignore` excludes the `.env` file so your token isn't committed to GitHub.

## License

This project is licensed under the MIT License.

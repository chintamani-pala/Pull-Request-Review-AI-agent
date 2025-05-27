# type: ignore
import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_latest_commit_sha(owner, repo, pr_number):
    """Fetches the HEAD commit SHA for a PR."""
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        pr_data = response.json()
        return pr_data["head"]["sha"]
    else:
        print(f"❌ Could not fetch commit SHA: {response.status_code} {response.text}")
        return None

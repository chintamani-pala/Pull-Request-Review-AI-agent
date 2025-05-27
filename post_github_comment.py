# type: ignore
import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def post_github_comment(owner, repo, pr_number, body):
    """Fallback: post general comment on PR."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"body": body}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("✅ General comment posted on PR.")
    else:
        print(
            f"❌ Failed to post general comment: {response.status_code} {response.text}"
        )

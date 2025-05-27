# type: ignore
import os
import requests
from dotenv import load_dotenv
from get_latest_commit_sha import get_latest_commit_sha
from time import sleep

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def post_inline_comment(owner, repo, pr_number, filename, line, body):
    """Posts an inline comment on a PR."""
    commit_id = get_latest_commit_sha(owner, repo, pr_number)
    if not commit_id:
        print("❌ Could not get commit SHA; skipping inline comment.")
        return

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/comments"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "body": body,
        "commit_id": commit_id,
        "path": filename,
        "side": "RIGHT",
        "line": int(line),
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"POST {url} status: {response.status_code}")
    if response.status_code == 201:
        print(f"✅ Inline comment posted on {filename} line {line}.")
        sleep(3)  # Rate limit handling
    else:
        print(
            f"❌ Failed to post inline comment: {response.status_code} {response.text}"
        )
        sleep(3)  # Rate limit handling

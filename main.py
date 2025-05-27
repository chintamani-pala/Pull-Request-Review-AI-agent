# type: ignore
import os
from dotenv import load_dotenv
from get_pr_patch import get_pr_patch
from extract_changed_lines import extract_changed_lines
from build_prompt_from_changed_lines import build_prompt_from_changed_lines
from request_ai_review import request_ai_review
from post_ai_review_comments import post_ai_review_comments

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python main.py <owner> <repo> <pr_number>")
        exit(1)

    owner, repo, pr_number = sys.argv[1], sys.argv[2], sys.argv[3]

    patch_content = get_pr_patch(owner, repo, pr_number)
    if not patch_content:
        print("No patch content found to review.")
        exit(1)

    changed_lines = extract_changed_lines(patch_content)
    if not changed_lines:
        print("No changed lines found in the patch.")
        exit(0)
    with open("./output/change.txt", "w") as f:
        f.write(str(changed_lines) or "No changed lines content available.")
    prompt = build_prompt_from_changed_lines(changed_lines)
    with open("./output/prompt.txt", "w") as f:
        f.write(prompt or "No prompt content available.")
    ai_review = request_ai_review(prompt)
    with open("./output/review.txt", "w") as f:
        f.write(ai_review)
    post_ai_review_comments(owner, repo, pr_number, ai_review)

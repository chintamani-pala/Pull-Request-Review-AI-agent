# type: ignore
import os
import re
from dotenv import load_dotenv
from post_inline_comment import post_inline_comment
from post_github_comment import post_github_comment

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def post_ai_review_comments(owner, repo, pr_number, ai_review):
    """
    Parse AI review lines and post inline comments.
    Expected format per line:
    Line <line_number> in <filename>: <problem>. Suggestion: <fix>.
    """
    pattern = r"Line (\d+) in ([^:]+): (.+?)(?:\. Suggestion: (.+))?$"
    any_posted = False

    for line in ai_review.splitlines():
        match = re.match(pattern, line.strip())
        if match:
            line_num, filename, problem, suggestion = match.groups()
            comment = problem
            if suggestion:
                comment += f". Suggestion: {suggestion}"
            try:
                post_inline_comment(owner, repo, pr_number, filename, line_num, comment)
                any_posted = True
            except Exception as e:
                print(f"Error posting inline comment: {e}")

    if not any_posted:
        print("⚠️ No inline comments posted. Posting a general comment instead.")
        post_github_comment(owner, repo, pr_number, ai_review)

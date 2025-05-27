# aiPR – AI-powered Pull Request Reviewer

**aiPR** is an automated code review tool that leverages AI to analyze pull requests on GitHub, enforce customizable code quality rules, and post inline review comments directly on your PRs.

---

## Features

- **Automated Patch Extraction:** Fetches the latest patch (diff) from a specified GitHub pull request.
- **Changed Line Analysis:** Extracts and processes only the changed lines for focused, efficient review.
- **Customizable Review Rules:** Enforces strict, configurable rules (e.g., camelCase naming, no commented-out code except TODOs, etc.).
- **AI Review Integration:** Uses an AI model to generate review comments based on code changes and rules.
- **Inline GitHub Comments:** Automatically posts AI-generated review comments as inline feedback on the PR.
- **Audit Trail:** Saves intermediate outputs (changed lines, prompts, AI reviews) for transparency and debugging.

---

## Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/aiPR.git
    cd aiPR
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the project root with:
        ```
        GITHUB_TOKEN=your_github_token
        GEMINI_API_KEY=your_gemini_api_key
        ```

4. **Run the tool:**
    ```sh
    python main.py <owner> <repo> <pr_number>
    ```
    - `<owner>`: GitHub username or organization
    - `<repo>`: Repository name
    - `<pr_number>`: Pull request number

---

## Example

```sh
python main.py octocat Hello-World 42
```

---

## Customizing Review Rules

Edit the `pr_checking_rules.py` file to add or modify code review rules according to your team's standards.

---

## Output

- `output/change.txt`: Extracted changed lines from the PR.
- `output/prompt.txt`: The AI prompt generated for review.
- `output/review.txt`: The AI-generated review comments.

---

## Requirements

- Python 3.x
- [GitHub API token](https://github.com/settings/tokens)
- Gemini API key (for AI review)
- Required Python packages (see `requirements.txt`)

---

## License

MIT License

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## Disclaimer

This tool is intended to assist with code review. Always verify AI-generated suggestions before merging code.

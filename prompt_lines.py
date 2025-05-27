# type: ignore
from pr_checking_rules import rules

prompt_lines = [
    "You are a senior code reviewer.",
    "Review the following changed lines of code and provide comments ONLY on issues found.",
    "",
    "Apply these rules strictly:",
]
prompt_lines.extend([f"- {rule}" for rule in rules])
prompt_lines += [
    "",
    "For each issue, output a single line in the format:",
    "Line <line_number> in <filename>: <problem>. Suggestion: <short fix>.",
    "Only comment on lines that have problems.",
    "If no issues are found, respond with 'No issues found'.",
    "Do not include anything else besides these comments.",
    "",
    "Here are the changed lines:",
    "",
]

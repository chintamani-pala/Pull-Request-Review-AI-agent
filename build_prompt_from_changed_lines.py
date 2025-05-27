# type: ignore
from prompt_lines import prompt_lines


def build_prompt_from_changed_lines(changed_lines):
    """
    Build a concise prompt listing changed lines for AI review, including strict review rules.
    """

    current_file = None
    for filename, line_num, content in changed_lines:
        if filename != current_file:
            prompt_lines.append(f"File: {filename}")
            current_file = filename
        prompt_lines.append(f"Line {line_num}: {content}")

    return "\n".join(prompt_lines)

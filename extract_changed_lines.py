# type: ignore
import re


def extract_changed_lines(patch_text):
    """
    Parse patch text and extract tuples of (filename, new_line_number, line_content)
    for added/changed lines (lines starting with '+').
    """
    changed_lines = []
    current_file = None
    new_line_num = None

    for line in patch_text.splitlines():
        # Detect file header line
        if line.startswith("+++ b/"):
            current_file = line[6:].strip()
            new_line_num = None

        # Detect hunk header like @@ -old_line,old_count +new_line,new_count @@
        elif line.startswith("@@"):
            match = re.search(r"\+(\d+)(?:,(\d+))?", line)
            if match:
                new_line_num = (
                    int(match.group(1)) - 1
                )  # minus 1 because we increment before line content

        # Lines starting with '+', but not '+++', are added/changed lines in the new file
        elif line.startswith("+") and not line.startswith("+++"):
            if new_line_num is not None and current_file is not None:
                new_line_num += 1
                changed_lines.append((current_file, new_line_num, line[1:].rstrip()))
        # For unchanged or removed lines
        elif not line.startswith("-"):
            # Increment line number for context lines (unchanged lines in hunk)
            if new_line_num is not None:
                new_line_num += 1
    return changed_lines

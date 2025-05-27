# type: ignore
rules = [
    "Remove any commented-out code, EXCEPT if the comment contains a TODO (e.g., '// TODO: ...' is allowed).",
    "If commented code is present and does NOT contain a TODO, flag it as an issue.",
    "In TypeScript files, all type imports must use 'import type'.",
    "There should be no 'console.log' statements in the code.",
    "If the function name is not in camelCase, flag it as an issue. For example, 'FunctionName' or 'function_name' is not allowed.",
    "All variables must be in camelCase.(eg: 'variableName' is allowed, but 'VariableName' or 'variable_name' is not allowed).",
]

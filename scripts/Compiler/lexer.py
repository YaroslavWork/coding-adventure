import re
from tokens import TOKEN_TYPES

def lexer(code):
    tokens = []

    # Combine all regex patterns into a single pattern
    regex_parts = [f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES]
    master_pattern = re.compile("|".join(regex_parts))

    for match in master_pattern.finditer(code):
        kind = match.lastgroup
        value = match.group()
        
        if kind == 'WHITESPACE':
            continue  # Skip whitespace tokens
        if kind == 'UNKNOWN':
            raise SyntaxError(f"Unexpected character: {value}")
        tokens.append((kind, value))

    return tokens



if __name__ == "__main__":
    sample_code = """
var x = true;
if (x < 10) {
    y = x + 1;
} else {
    y = x - 1;
}
    """
    tokens = lexer(sample_code)
    print(tokens)
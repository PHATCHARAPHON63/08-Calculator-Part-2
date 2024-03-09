from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()
    ADD_OP = "+"
    SUB_OP = "-"
    MUL_OP = "*"
    DIV_OP = "/"
    POWER_OP = "^"
    FAC_OP = "!"
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    EOF = auto()

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)})"

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_number(self):
        number_str = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            number_str += self.current_char
            self.advance()
        return float(number_str) if '.' in number_str else int(number_str)

    def get_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit() or self.current_char == '.':
                return Token(TokenType.NUMBER, self.get_number())

            if self.current_char == '+':
                self.advance()
                return Token(TokenType.ADD_OP, '+')
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.SUB_OP, '-')
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL_OP, '*')
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV_OP, '/')
            if self.current_char == '^':
                self.advance()
                return Token(TokenType.POWER_OP, '^')
            if self.current_char == '!':
                self.advance()
                return Token(TokenType.FAC_OP, '!')
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LEFT_PAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RIGHT_PAREN, ')')

            self.advance()  # Handle unknown character by simply skipping it
            return Token(TokenType.EOF)

        return Token(TokenType.EOF)

# Function to get the list of tokens (not part of the Lexer class)
def get_token_list(text):
    lexer = Lexer(text)
    tokens = []
    while lexer.current_char is not None:
        token = lexer.get_token()
        if token.type == TokenType.EOF:
            break
        tokens.append(token)
    return tokens

# Example usage:
if __name__ == "__main__":
    text = "3 + 4.2 * (1 - 2) ^ 2!"
    tokens = get_token_list(text)
    for token in tokens:
        print(token)

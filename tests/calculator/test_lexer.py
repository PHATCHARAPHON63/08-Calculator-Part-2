import unittest
from calculator.lexer import Lexer, TokenType, Token



class TestLexer(unittest.TestCase):
    def test_number_int(self):
        lexer = Lexer("123")
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.NUMBER, 123))

    def test_number_float(self):
        lexer = Lexer("3.1415")
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.NUMBER, 3.1415))

    def test_operators(self):
        tests = [
            ("+", TokenType.ADD_OP),
            ("-", TokenType.SUB_OP),
            ("*", TokenType.MUL_OP),
            ("/", TokenType.DIV_OP),
            ("^", TokenType.POWER_OP),
            ("!", TokenType.FAC_OP),
        ]
        for text, tokentype in tests:
            with self.subTest(text=text):
                lexer = Lexer(text)
                token = lexer.get_token()
                self.assertEqual(token, Token(tokentype, text))

    def test_parentheses(self):
        lexer = Lexer("()")
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.LEFT_PAREN, '('))
        token = lexer.get_token()
        self.assertEqual(token, Token(TokenType.RIGHT_PAREN, ')'))

    def test_complex_expression(self):
        lexer = Lexer("3 + 4.2 * (1 - 2) ^ 2!")
        expected_tokens = [
            Token(TokenType.NUMBER, 3),
            Token(TokenType.ADD_OP, '+'),
            Token(TokenType.NUMBER, 4.2),
            Token(TokenType.MUL_OP, '*'),
            Token(TokenType.LEFT_PAREN, '('),
            Token(TokenType.NUMBER, 1),
            Token(TokenType.SUB_OP, '-'),
            Token(TokenType.NUMBER, 2),
            Token(TokenType.RIGHT_PAREN, ')'),
            Token(TokenType.POWER_OP, '^'),
            Token(TokenType.NUMBER, 2),
            Token(TokenType.FAC_OP, '!'),
            Token(TokenType.EOF),
        ]
        
        for expected_token in expected_tokens:
            token = lexer.get_token()
            self.assertEqual(token, expected_token)

if __name__ == '__main__':
    unittest.main()

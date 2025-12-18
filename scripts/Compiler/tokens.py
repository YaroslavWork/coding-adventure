import re

TOKEN_TYPES = [
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER', r'\d+'),

    ('IF', r'if'),
    ('ELIF', r'elif'),
    ('ELSE', r'else'),

    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'),
    ('EQUALS', r'='),
    ('NOT_EQUALS', r'!='),
    ('LESS_THAN', r'<'),
    ('GREATER_THAN', r'>'),
    ('NEGATION', r'not'),
    ('AND', r'and'),
    ('OR', r'or'),

    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),
    ('WHITESPACE', r'[ \s\t\n]+'),
]
import re

TOKEN_TYPES = [
    ('VAR', r'var'),
    ('IF', r'if'),
    ('ELIF', r'elif'),
    ('ELSE', r'else'),
    ('TRUE', r'true'),
    ('FALSE', r'false'),

    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('SEMICOLON', r';'),

    ('EQUALS', r'='),
    ('DOUBLE_EQUALS', r'=='),
    ('NOT_EQUALS', r'!='),
    
    ('NEGATION', r'not'),
    ('AND', r'and'),
    ('OR', r'or'),

    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),

    ('LESS_EQUAL', r'<='),
    ('GREATER_EQUAL', r'>='),
    ('LESS_THAN', r'<'),
    ('GREATER_THAN', r'>'),
    
    ('FLOAT', r'\d+\.\d+'),
    ('NUMBER', r'\d+'),
    ('STRING', r'"[^"]*"|\'[^\']*\''),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('WHITESPACE', r'[ \s\t\n]+'),
    ('UNKNOWN', r'.'),
]
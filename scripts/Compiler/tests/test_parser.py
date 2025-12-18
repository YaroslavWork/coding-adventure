import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from scripts.Compiler.lexer import lexer
from scripts.Compiler.parser import Parser
from scripts.Compiler.abstract_syntax_tree import *


def test_parser_var_declaration():
    parser = Parser([('VAR', 'var'), ('IDENTIFIER', 'x'), ('EQUALS', '='), ('NUMBER', '10'), ('SEMICOLON', ';')])
    ast = parser.parse_program()
    assert len(ast) == 1
    assert isinstance(ast[0], VariableDeclarationNode)
    assert ast[0].identifier == 'x'
    assert isinstance(ast[0].value, NumberNode)
    assert ast[0].value.value == 10


test_parser_var_declaration()
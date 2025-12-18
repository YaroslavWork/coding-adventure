import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from scripts.Compiler.lexer import lexer
from scripts.Compiler.parser import Parser
from scripts.Compiler.interpreter import Interpreter

def run_and_return_environment(source_code: str):
    tokens = lexer(source_code)
    parser = Parser(tokens)
    ast = parser.parse_program()
    interpreter = Interpreter()
    for statement in ast:
        interpreter.visit(statement)
    return interpreter.environment

def test_variable_declaration():
    source_code = "var x = 10;"
    env = run_and_return_environment(source_code)
    assert 'x' in env
    assert env['x'] == 10

def test_variable_assignment():
    source_code = """
        var x = 10;
        x = 20;
    """
    env = run_and_return_environment(source_code)
    assert 'x' in env
    assert env['x'] == 20

def test_variable_usage():
    source_code = """
        var x = 10;
        var y = x + 5;
    """
    env = run_and_return_environment(source_code)
    assert 'y' in env
    assert env['y'] == 15

def test_multiply_variable_usage():
    source_code = """
        var a = 3;
        var b = 4;
        var c = a * b + 2;
    """
    env = run_and_return_environment(source_code)
    assert 'c' in env
    assert env['c'] == 14

def test_divide_variable_usage():
    source_code = """
        var a = 20;
        var b = 4;
        var c = a / b - 3;
    """
    env = run_and_return_environment(source_code)
    assert 'c' in env
    assert env['c'] == 2.0

def test_if_statement_variable_assignment():
    source_code = """
        var x = 5;
        if (x < 10) {
            x = 20;
        } else {
            x = 30;
        }
    """
    env = run_and_return_environment(source_code)
    assert 'x' in env
    assert env['x'] == 20

def test_if_statement_variable_assignment_else():
    source_code = """
        var x = 15;
        if (x < 10) {
            x = 20;
        } else {
            x = 30;
        }
    """
    env = run_and_return_environment(source_code)
    assert 'x' in env
    assert env['x'] == 30

def test_multiple_variable_assignments():
    source_code = """
        var x = 10;
        var y = 20;
        x = x + y;
        y = x * 2;
    """
    env = run_and_return_environment(source_code)
    assert 'x' in env
    assert 'y' in env
    assert env['x'] == 30
    assert env['y'] == 60

def test_operation_with_adding_yourself():
    source_code = """
        var x = 5;
        x = x + x;
    """
    env = run_and_return_environment(source_code)
    assert 'x' in env
    assert env['x'] == 10


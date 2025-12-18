from .abstract_syntax_tree import *

class Parser:

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return ('EOF', '')  # End of file token

    def eat(self, token_type: str):
        current = self.current_token()
        if current[0] == token_type:
            self.position += 1
            return current
        raise SyntaxError(f"Expected {token_type}, got {current[0]}")
    
    def parse_factor(self):
        # FACTOR -> NUMBER | FLOAT | TRUE | FALSE | STRING | IDENTIFIER
        token = self.current_token()
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return NumberNode(token[1])
        elif token[0] == 'FLOAT':
            self.eat('FLOAT')
            return FloatNode(token[1])
        elif token[0] == 'TRUE' or token[0] == 'FALSE':
            self.eat(token[0])
            return BooleanNode(token[1])
        elif token[0] == 'STRING':
            self.eat('STRING')
            return StringNode(token[1])
        elif token[0] == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            return VariableAccessNode(token[1])
    
    def parse_expression(self):
        # EXPRESSION -> FACTOR ((PLUS | MINUS) FACTOR)*
        left = self.parse_factor()

        while self.current_token()[0] in (
            'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LESS_THAN',
            'GREATER_THAN', 'LESS_EQUAL', 'GREATER_EQUAL',
            'DOUBLE_EQUALS', 'NOT_EQUALS', 'AND', 'OR'
        ):
            operator = self.current_token()[1]
            self.eat(self.current_token()[0])
            right = self.parse_factor()
            left = BinaryOpNode(left, operator, right)

        return left
    
    def parse_statement(self):
        curr = self.current_token()

        # VAR_DECLARATION -> 'var' IDENTIFIER '=' EXPRESSION ';'
        if curr[0] == 'VAR':
            self.eat('VAR')
            identifier = self.eat('IDENTIFIER')[1]
            self.eat('EQUALS')
            value = self.parse_expression()
            self.eat('SEMICOLON')
            return VariableDeclarationNode(identifier, value)
        
        # IDENTIFIER '=' EXPRESSION ';'
        elif curr[0] == 'IDENTIFIER':
            identifier = self.eat('IDENTIFIER')[1]
            self.eat('EQUALS')
            value = self.parse_expression()
            self.eat('SEMICOLON')
            return VariableAssignNode(identifier, value)
        
        # IF -> 'if' '(' EXPRESSION ')' '{' STATEMENT* '}' ( 'else' '{' STATEMENT* '}' )?
        elif curr[0] == 'IF':
            self.eat('IF')
            self.eat('LPAREN')
            condition = self.parse_expression()
            self.eat('RPAREN')
            self.eat('LBRACE')
            true_branch = []
            while self.current_token()[0] != 'RBRACE':
                true_branch.append(self.parse_statement())
            self.eat('RBRACE')

            false_branch = []
            if self.current_token()[0] == 'ELSE':
                self.eat('ELSE')
                self.eat('LBRACE')
                while self.current_token()[0] != 'RBRACE':
                    false_branch.append(self.parse_statement())
                self.eat('RBRACE')

            return IfNode(condition, true_branch, false_branch)
        
    def parse_program(self):
        statements = []
        while self.current_token()[0] != 'EOF':
            statements.append(self.parse_statement())
        return statements

if __name__ == "__main__":
    Parser([('IDENTIFIER', 'x'), ('EQUALS', '='), ('NUMBER', '10')]).parse_factor()
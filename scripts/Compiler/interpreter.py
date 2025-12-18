from .abstract_syntax_tree import *

class Interpreter:
    def __init__(self):
        self.environment = {}

    def visit(self, node):
        # 1. Numbers return their value
        if isinstance(node, NumberNode):
            return node.value
        
        # 2. Floats return their value
        elif isinstance(node, FloatNode):
            return node.value
        
        # 3. Booleans return their value
        elif isinstance(node, BooleanNode):
            return node.value
        
        # 4. Strings return their value
        elif isinstance(node, StringNode):
            return node.value
        
        # 5. Variable Access
        elif isinstance(node, VariableAccessNode):
            if node.identifier in self.environment:
                return self.environment[node.identifier]
            else:
                raise NameError(f"Variable '{node.identifier}' is not defined.")
            
        # 6. Variable Assignment (for ex. x = 10;)
        elif isinstance(node, VariableAssignNode):
            value = self.visit(node.value)
            self.environment[node.identifier] = value
            return value
        
        # 7. Binary Operations (for ex. x + y)
        elif isinstance(node, BinaryOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)
            operator = node.operator

            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            elif operator == '<':
                return left < right
            elif operator == '>':
                return left > right
            elif operator == '<=':
                return left <= right
            elif operator == '>=':
                return left >= right
            elif operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
            elif operator == 'and':
                return left and right
            elif operator == 'or':
                return left or right
            else:
                raise ValueError(f"Unknown operator: {operator}")
            
        # 8. Unary Operations (for ex. -x)
        elif isinstance(node, UnaryOpNode):
            operand = self.visit(node.operand)
            operator = node.operator

            if operator == '-':
                return -operand
            elif operator == 'not':
                return not operand
            else:
                raise ValueError(f"Unknown operator: {operator}")
            
        # 9. Variable Declarations (for ex. var x = 10;)
        elif isinstance(node, VariableDeclarationNode):
            value = self.visit(node.value)
            self.environment[node.identifier] = value
            return value
        
        # 10. If Statements
        elif isinstance(node, IfNode):
            condition = self.visit(node.condition)
            if condition:
                for stmt in node.true_block:
                    self.visit(stmt)
            elif node.false_block is not None:
                for stmt in node.false_block:
                    self.visit(stmt)

        else:
            raise TypeError(f"Unknown AST node type: {type(node)}")
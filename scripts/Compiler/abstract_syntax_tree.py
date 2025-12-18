class ASTNode: pass

# Data Nodes
class NumberNode(ASTNode):
    def __init__(self, value: str):
        self.value: int = int(value)

    def __repr__(self): return f"Number({self.value})"


class FloatNode(ASTNode):
    def __init__(self, value: str):
        self.value: float = float(value)

    def __repr__(self): return f"Float({self.value})"


class BooleanNode(ASTNode):
    def __init__(self, value: str):
        self.value: bool = True if value == 'true' else False

    def __repr__(self): return f"Boolean({self.value})"


class StringNode(ASTNode):
    def __init__(self, value: str):
        self.value: str = value[1:-1]  # Remove quotes

    def __repr__(self): return f"String({self.value})"


class VariableAccessNode(ASTNode):
    def __init__(self, identifier: str):
        self.identifier: str = identifier

    def __repr__(self):
        return f"VariableAccess({self.identifier})"


class VariableAssignNode(ASTNode):
    def __init__(self, identifier: str, value: ASTNode):
        self.identifier: str = identifier
        self.value: ASTNode = value

    def __repr__(self):
        return f"VariableAssign({self.identifier}, {self.value})"


# Operation Nodes
class BinaryOpNode(ASTNode):
    def __init__(self, left: ASTNode, operator: str, right: ASTNode):
        self.left: ASTNode = left
        self.operator: str = operator
        self.right: ASTNode = right

    def __repr__(self):
        return f"BinaryOp({self.left}, '{self.operator}', {self.right})"


class UnaryOpNode(ASTNode):
    def __init__(self, operator: str, operand: ASTNode):
        self.operator: str = operator
        self.operand: ASTNode = operand

    def __repr__(self):
        return f"UnaryOp('{self.operator}', {self.operand})"

# Statement Nodes
class VariableDeclarationNode(ASTNode):
    def __init__(self, identifier: str, value: ASTNode):
        self.identifier: str = identifier
        self.value: ASTNode = value

    def __repr__(self):
        return f"VarDeclaration({self.identifier}, {self.value})"


class BlockNode(ASTNode):
    def __init__(self, statements: list):
        self.statements: list = statements

    def __repr__(self):
        return f"Block({self.statements})"
    

class IfNode(ASTNode):
    def __init__(self, condition: ASTNode, true_block: BlockNode, false_block: BlockNode = None):
        self.condition: ASTNode = condition
        self.true_block: BlockNode = true_block
        self.false_block: BlockNode = false_block

    def __repr__(self):
        return f"If({self.condition}, {self.true_block}, {self.false_block})"
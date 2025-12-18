class ASTNode: pass

class NumberNode(ASTNode):
    def __init__(self, value: str):
        self.value: int = int(value)

    def __repr__(self): return f"Number({self.value})"

class BooleanNode(ASTNode):
    def __init__(self, value): self.value = value == 'true'
    def __repr__(self): return f"Boolean({self.value})"
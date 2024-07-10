import ast
class Constant1:
    def __init__(self, value):
        self.value = value

eight = Constant1(8)

class UnaryOperator:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

neg_eight = UnaryOperator(ast.USub(), eight)

## The calling on an function is represented by the Call class
class Calling:
    def __init__(self, func, args):
        self.func = func 
        self.args = args

class Naming:
    def __init__(self, id) -> None:
        self.id = id

get_number = Calling(Naming("get_number"), [])

## Represent the binary operation
class BinaryOperation:
    def __init__(self, op, left, right) -> None:
        self.op = op
        self.left = left
        self.right = right

ast1_1 = BinaryOperation(ast.Add, get_number, neg_eight)

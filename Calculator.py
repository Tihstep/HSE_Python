import re
from typing import List

class Calculator:
    def __init__(self):
        self.tokens = None

    def _tokenize(self, expression: str) -> None:
        pattern = r'-?[0-9]*\.?[0-9]+|[()+*\/-]' # Выделяем числа, скобки или функции
        tokens = re.findall(pattern, expression)
        self.tokens = tokens

    def _rpn_transformation(self) -> List[str]:
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, '~': 3}
        output = []
        stack = []
        
        for idx, token in enumerate(self.tokens):
            pattern = r'^-?\d+(?:\.\d+)?$' # Выделяем вещественное число
            if token.isdigit() or re.match(pattern, token):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif token in priority:
                # Если минус унарный, используем ~ как оператор унарного минуса
                # также можно добавлять 0 перед -
                if token == '-' and (output == [] or
                    not(self.tokens[idx-1].isdigit() or re.match(pattern, self.tokens[idx-1]))):
                    token = '~'
                while stack and stack[-1] in priority and priority[stack[-1]] >= priority[token]:
                    output.append(stack.pop())
                stack.append(token)
                
        while stack:
            output.append(stack.pop())
        
        return output

    def evaluate(self, expression: str) -> float:
        self._tokenize(expression)

        rpn = self._rpn_transformation()
        stack = []
        
        for token in rpn:
            if token.isdigit() or re.match(r'^-?\d+(?:\.\d+)?$', token):
                stack.append(float(token))
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                if a == 0:
                    raise ZeroDivisionError("Деление на ноль запрещено")
                stack.append(b / a)
            elif token == '~':
                last = 0 if stack == [] else stack.pop()
                stack.append(0 - last)
        return stack.pop()
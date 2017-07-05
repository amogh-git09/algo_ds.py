from algo_ds.stack import Stack

operators = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}

def convert_to_postfix(expr):
    stack = Stack()
    postfix = ""
    for c in expr:
        if c in operators:
            if c == '(':
                stack.push(c)
            elif c == ')':
                popped = stack.pop()
                while popped != '(':
                    postfix += popped
                    popped = stack.pop()
            elif stack.isEmpty():
                stack.push(c)
            elif operators[stack.peek()] < operators[c]:
                stack.push(c)
            else:
                while (not stack.isEmpty()) and (operators[stack.peek()] >= operators[c]):
                    postfix += stack.pop()
                stack.push(c)
        else:
            postfix += c
    while not stack.isEmpty():
        postfix += stack.pop()
    return postfix

def evaluate(expr):
    if expr == "":
        return 0
    stack = Stack()
    for c in expr:
        if c not in operators:
            stack.push(c)
        else:
            right = int(stack.pop())
            left = int(stack.pop())
            if c == '+':
                result = left + right
            elif c == '-':
                result = left - right
            elif c == '*':
                result = left * right
            elif c == '/':
                result = left / right
            else:
                raise ValueError("invalid operator", c)
            stack.push(result)
    return stack.pop()

def check_balanced_parantheses(expr):
    stack = Stack()
    for c in expr:
        if c == '(':
            stack.push(c)
        elif c == ')':
            if stack.isEmpty():
                return False
            stack.pop()
    return stack.isEmpty()

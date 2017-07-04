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

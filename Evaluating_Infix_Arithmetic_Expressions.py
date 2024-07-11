"""
Name: Sammyajit Kapuria
Email: sammyajit.kapuria87@myhunter.cuny.edu
08/31/2021

Resources: Used pandas.pydata.org as a reference as suggested by the TAs.
pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html

Assignment 8
"""

class EmptyStackException(Exception):
    pass

class DivisionByZeroException(Exception):
    pass

class InvalidExpressionException(Exception):
    pass

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    for token in expression.split():
        if token.isdigit():
            output.append(token)  # Append numbers directly to output
        elif token in precedence:
            # Pop operators from stack to output based on precedence
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)  # Push '(' to stack
        elif token == ')':
            # Pop until '(' is encountered
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if operators and operators[-1] == '(':
                operators.pop()
            else:
                raise InvalidExpressionException("Mismatched parentheses")
        else:
            raise InvalidExpressionException(f"Invalid token: {token}")

    while operators:
        top = operators.pop()
        if top == '(' or top == ')':
            raise InvalidExpressionException("Mismatched parentheses")
        output.append(top)

    return ' '.join(output)

def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))  # Push numbers to stack
        elif token in '+-*/':
            if len(stack) < 2:
                raise InvalidExpressionException("Insufficient operands")
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise DivisionByZeroException("Division by zero")
                stack.append(a / b)
        else:
            raise InvalidExpressionException(f"Invalid token: {token}")

    if len(stack) != 1:
        raise InvalidExpressionException("Too many operands")

    return stack.pop()

def main():
    try:
        infix_expr = "3 + 5 * ( 2 - 8 )"
        postfix_expr = infix_to_postfix(infix_expr)
        print(f"Postfix Expression: {postfix_expr}")
        result = evaluate_postfix(postfix_expr)
        print(f"Result: {result}")
    except EmptyStackException:
        print("Error: Stack is empty")
    except DivisionByZeroException as e:
        print(f"Error: {e}")
    except InvalidExpressionException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

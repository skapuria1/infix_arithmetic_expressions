# Infix to Postfix and Postfix Evaluation

This project provides a solution to convert an infix expression to a postfix expression and evaluate it. The code also includes exception handling for illegal expressions like missing operands or division by zero.

## Code Explanation

### Exceptions

- **EmptyStackException**: Raised when the stack is empty.
- **DivisionByZeroException**: Raised when there's an attempt to divide by zero.
- **InvalidExpressionException**: Raised for invalid expressions.

### Functions

- **infix_to_postfix(expression)**: Converts an infix expression to a postfix expression.
- **evaluate_postfix(expression)**: Evaluates a postfix expression.


## Running the Code

1. Ensure you have Python installed on your machine.
2. Save the code to a file, e.g., `infix_postfix.py`.
3. Run the code using the command:

   ```sh
   python infix_postfix.py

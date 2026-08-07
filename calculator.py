import re

def calculate(expression):
    # Using regular expression to find all numbers in the expression
    numbers = re.findall(r'\d+', expression)
    # Calculate the sum of numbers
    total = sum(map(int, numbers))
    return total

# Example usage:
expression = '10 + 20 * 30'
result = calculate(expression)
print(f'The result of the expression is: {result}')
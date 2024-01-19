def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def subtract(x, y):
    return x - y

# Example usage:
num1 = 10
num2 = 5

result_addition = add(num1, num2)
result_multiplication = multiply(num1, num2)
result_division = divide(num1, num2)
result_subtraction = subtract(num1, num2)

print(f"Addition: {result_addition}")
print(f"Multiplication: {result_multiplication}")
print(f"Division: {result_division}")
print(f"Subtraction: {result_subtraction}")

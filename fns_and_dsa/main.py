# File: main.py

from fns_and_dsa.arithmetic_operations import perform_operation

def main():
    print("Welcome to the Arithmetic Operations Program!")

    # Example usage:
    num1 = 10
    num2 = 5

    # Addition
    result_add = perform_operation(num1, num2, 'add')
    print(f"{num1} + {num2} = {result_add}")

    # Subtraction
    result_sub = perform_operation(num1, num2, 'subtract')
    print(f"{num1} - {num2} = {result_sub}")

    # Multiplication
    result_mul = perform_operation(num1, num2, 'multiply')
    print(f"{num1} * {num2} = {result_mul}")

    # Division
    result_div = perform_operation(num1, num2, 'divide')
    print(f"{num1} / {num2} = {result_div}")

    # Division by zero
    num3 = 10
    num4 = 0
    result_zero_div = perform_operation(num3, num4, 'divide')
    print(f"{num3} / {num4} = {result_zero_div}")

    # Invalid operation
    result_invalid = perform_operation(num1, num2, 'exponentiate')
    print(f"Invalid operation result: {result_invalid}")

if __name__ == "__main__":
    main()

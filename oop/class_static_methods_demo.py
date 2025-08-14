# Task 3: Distinguishing Between Class Methods and Static Methods
# File: class_static_methods_demo.py

class Calculator:
    """
    A class that demonstrates the use of static and class methods.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that adds two numbers.
        It doesn't need access to the class or instance.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that multiplies two numbers.
        It accesses a class attribute using the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
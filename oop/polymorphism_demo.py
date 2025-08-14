# Task 2: Exploring Polymorphism and Method Overriding
# File: polymorphism_demo.py

import math

# Base Class - Shape
class Shape:
    """
    A base class for shapes, demonstrating polymorphism.
    """
    def area(self):
        """
        Calculates the area of the shape.
        Raises an error because this method should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement this method")

# Derived Class - Rectangle
class Rectangle(Shape):
    """
    A derived class for a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the area of a rectangle.
        """
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    """
    A derived class for a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the area of a circle.
        """
        return math.pi * self.radius ** 2
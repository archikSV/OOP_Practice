print("Task 2:\n")

"""
Створіть клас Circle з атрибутом radius та методом
area, який поверне площу кола з вказаним радіусом.
"""

# classes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# objects
circle1 = Circle(5)

# main
print(circle1.area())
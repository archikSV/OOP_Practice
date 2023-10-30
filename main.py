print("Task X:\n")

"""
Створіть клас Circle з атрибутом radius та методом
area, який поверне площу кола з вказаним радіусом.
"""

# classes
class Cirlce:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# objects
cirlce1 = Cirlce(5)

# main
print(circlce1.area())
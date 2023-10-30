print("Task 1:\n")

"""
Створіть клас Student з атрибутами name та age.
Додайте метод print_info, який виведе інформацію про
студента у на вигляді "Ім'я: {name}, Вік: {age}".
"""

# classes
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(f"Name: {self.name} \nAge: {self.age}")

# objects
student1 = Student("Jeremy", 21)

# main
student1.print_info()
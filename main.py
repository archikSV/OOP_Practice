print("Task 4:\n")

"""
Створіть клас Car з атрибутами brand (марка
автомобіля), model (модель) та year (рік випуску).
Додайте метод start_engine, який виведе повідомлення
про те, що двигун запущено.
"""

# classes
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

# objects
car1 = Car("Ford", "Mustang", 2018)

# main
car1.start_engine()
car1.stop_engine()
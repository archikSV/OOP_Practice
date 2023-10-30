print("Task 3:\n")

"""
Створіть клас Book з атрибутами title (назва
книги), author (автор) та genre (жанр). Додайте метод
display_info, який виведе інформацію про книгу у
вигляді "Назва: {title}, Автор: {author}, Жанр: {genre}".
"""

# classes
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title} \nАuthor: {self.author} \nGenre: {self.genre}")

# objects
book1 = Book("War and Peace", "Leo Tolstoy", "novel")

# main
book1.display_info()
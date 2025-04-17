# Assignment 1

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self._pages = pages        # Encapsulated page attribute 
        self.__price = price       # Strongly encapsulated with double underscore

    def get_description(self):
        return print(f"'{self.title}' by {self.author}, {self._pages} pages.")

    def get_price(self):
        return print(f"The price of '{self.title}' is Ksh.{self.__price}.")

# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, pages, price, file_size_mb):
        super().__init__(title, author, pages, price)
        self.file_size_mb = file_size_mb

    def get_description(self):  # Polymorphism - method overridden
        return print(f"E-Book: '{self.title}' by {self.author}, {self._pages} pages, File size: {self.file_size_mb}MB.")
    
book1 = Book("Atomic Habits", "James Clear", 320, 1499.50)
ebook1 = EBook("Deep Work", "Cal Newport", 280, 999, 5)

print(book1.get_description())
print(book1.get_price())

print(ebook1.get_description())
print(ebook1.get_price())


# Assignment 2

class Animal:
    def move(self):
        return "This animal moves in some way."

# Subclass: Dog
class Dog(Animal):
    def move(self):
        return "The dog runs on land "

# Subclass: Bird
class Bird(Animal):
    def move(self):
        return "The bird flies in the sky "

# Subclass: Fish
class Fish(Animal):
    def move(self):
        return "The fish swims in water "

# Create a list of animal objects
animals = [Dog(), Bird(), Fish()]

# Loop through and call move() polymorphically
for animal in animals:
    print(animal.move())

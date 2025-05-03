# Assignment 1: Superhero Class - Demonstrating OOP Concepts
# This program defines a Superhero class and a Spiderman subclass.
# It shows the use of Encapsulation, Inheritance, and Polymorphism.

# Parent Class
class Superhero:
    def __init__(self, name, power, city):
        # Private attributes (Encapsulation)
        self.__name = name
        self.__power = power
        self.__city = city

    # Getter methods to access private attributes
    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def get_city(self):
        return self.__city

    # Method to show superhero details
    def show_details(self):
        print(f"{self.get_name()} protects {self.get_city()} with {self.get_power()}.")

# Child Class - Inherits from Superhero
class Spiderman(Superhero):
    # Overriding show_details method (Polymorphism)
    def show_details(self):
        print("Spiderman is getting ready...")
        # Call the parent class method using super()
        super().show_details()

# Creating an instance of Spiderman
hero = Spiderman("Spiderman", "web-shooting", "New York")

# Displaying details of the superhero
hero.show_details()

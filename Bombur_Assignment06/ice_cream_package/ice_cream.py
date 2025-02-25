#ice_cream.py

# File Name : ice_cream.py
# Student Name: Vanshika Rana
# email: ranava@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 27th February 2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment was about collaborating in groups to develop a Python project in Visual Studio to model real-world objects, and incorporate object-oriented programming principles, and submit a shared GitHub repository.
# Brief Description of what this module does: This module was about fundamentals of Object-Oriented Programming (OOP) in Python, and included the use of classes, objects, encapsulation, inheritance, polymorphism, and data hiding.
# Citations: stackoverflow (https://stackoverflow.com/questions/62636600/how-to-make-a-method-for-a-string-in-python)(https://stackoverflow.com/questions/2579840/do-you-use-the-get-set-pattern-in-python)
# Anything else that's relevant: N/A

class IceCream:
    """
    Model an ice cream for sale at a store.
    """

    #Constructor
    def __init__(self, flavor, price):
        """
        Constructor
        @param flavor string: Flavor of the icecream.
        @param price string: Price of the icecream.
        """
        self.set_flavor(flavor)
        self.set_price(price)

    # __str__ method
    def __str__(self):
        """
        @return string: Returns a user-friendly string representation of the ice cream object.
        """
        return f"(flavor={self.__flavor}, price=${self.__price:.2f})"

    # __repr__ method
    def __repr__(self):
        """
        @param: Returns a debug string representation.
        """
        return f"IceCream('{self.__flavor}', {self.__price})"

    # Property for flavor (Getter & Setter)
    def set_flavor(self, flavor):
        """
       @param string flavor: Sets the flavor of the ice cream.
        """
        self.__flavor = flavor 

    def get_flavor(self):
        """
        Get the flavor of the ice cream.
        """
        return self.__flavor

    # Property for price (Getter & Setter with validation)
    def set_price(self, price):
        """
        @param string price: Set the price of the ice cream.
        """
        if price < 0:  
            raise ValueError("Price cannot be negative")
        else:
            self.__price = price  

    def get_price(self):
        """
        Get the price of the ice cream.
        """
        return self.__price

    # Method that "does something", here selling the ice cream.
    def sell(self):
        """
        Simulates selling the ice cream.
        """
        print(f"Selling {self.__flavor} ice cream for ${self.__price:.2f}!")

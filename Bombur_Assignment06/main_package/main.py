
# File Name: main.py
# Student Name: Cam Shinker
# email: shinkecj@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section: 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Collaborate with a team to run code that is created in classes

# Brief Description of what this module does: Learned about OOP and classes
# Citations: 

# Anything else that's relevant:
try:
    from basketball_package.basketball import *
except:
    print("Unable to import basketball_package")
try:
    from ice_cream_package.ice_cream import *
except:
    print("unable to import ice_cream_package")

if __name__ == "__main__":
    try:
        my_basketball = Basketball("Orange", "Sticky")
        print(my_basketball.__str__())
        print(my_basketball.shoot())
        my_basketball.set_color("Brown")
        print(my_basketball.get_color())
        my_basketball.set_texture("Worn Down")
        print(my_basketball.get_texture())
    except:
        print("Error with Basketball code")


    print("--------------------------------")
    try:
        my_ice_cream = IceCream("Vanilla", 2.99)
        print(my_ice_cream.__str__())
        my_ice_cream.set_flavor("Peanut Butter Chocolate")
        print(my_ice_cream.get_flavor())
        my_ice_cream.set_price(3.49)
        print(my_ice_cream.get_price())
        my_ice_cream.sell()
    except:
        print("Error within IceCream code")
    

# Basketball.py 
# Luke Elmore
# Elmorels@mail.uc.edu
# Spring 2025
# IS 4010-002
# 2/27/2025
# Takes a basketball and models it.

import random
class Basketball(object):
    """
    Models a basketball on a court before a game.
    """
    def __init__(self,color,texture,shoot):
        """
        Constructor
        @param color String: The color of the basketball
        @param texture String: The texture of the basketball
        """
        self.__texture = texture
        self.set_color(color)
        self.__shoot = shoot

    def set_color(self,color):
        """
        @param String Color: set the color of basketball
        """
        if len(color.strip()) == 0:
            raise Exception("The color of the basketball cannot be blank ")
        else:
            self.__color = color

    def get_color(self):
        """
        Get the color of the basketball
        """
        return self.__color 
    def set_texture(self,texture):
        """
        @param String Texture: What does the ball feel like?
        """
        self.__texture = texture

    def get_texture(self):
        """
        Get the texture of the basketball
        """
        return self.__texture

    def shoot(self):
        """
        shooting the basketball and return whether it swishes or clanks.
        """
        self.__shoot = random.choice(["Swish", "Clank"])
        return f"The ball {self.__shoot}ed!"

    def __str__(self): 
        """
        @return String: Gives a string of each property
        """
        return "Color:" + self.__color + " Texture:" + self.__texture + "The basketball"+self.__shoot
        

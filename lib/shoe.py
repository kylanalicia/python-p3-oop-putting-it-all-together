#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        self.is_worn = False  # A simple attribute to track whether the shoe is worn or not

    def wear(self):
        if not self.is_worn:
            self.is_worn = True
            print(f"You are now wearing {self.color} {self.brand} shoes in size {self.size}.")
        else:
            print("You are already wearing these shoes.")

    def take_off(self):
        if self.is_worn:
            self.is_worn = False
            print(f"You have taken off the {self.color} {self.brand} shoes.")
        else:
            print("You are not wearing these shoes right now.")
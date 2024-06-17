# import time

# for i in range(5, 0, -1):
#     print(f"Countdown: {i}", end='\r')
#     time.sleep(1)
# print('Blast off!')

import tkinter as tk

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
    def display_info(self):
        print(f"This car is a {self.color} {self.model}")
        
my_car = Car("red", "Toyota")
my_car.display_info()
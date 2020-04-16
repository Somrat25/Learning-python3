# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:47:19 2020

@author: Moshahed Somrat
"""

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        a = str(self.year) + ' ' + self.model + ' ' + self.make
        return a.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it!")
        
my_new_car = Car('bmw','b4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 13
my_new_car.read_odometer()

my_used_car = Car('audi','a4',2010)
print(my_used_car.get_descriptive_name())
my_used_car.odometer_reading = 30000
my_used_car.read_odometer()


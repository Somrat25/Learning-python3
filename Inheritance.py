# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:27:57 2020

@author: Moshahed Somrat
"""

'''class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        new_name = str(self.year) + ' ' + self.model + ' ' + self.make
        return new_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it!")
        
my_new_car = Car('bmw','b5',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 2300
my_new_car.read_odometer()

class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
        
    def size_of_battery(self):
        print("Battery size is " + str(self.battery_size) + "!")
        
my_toyota = Electric_car('toyota','model t4',2018)
print(my_toyota.get_descriptive_name())
my_toyota.odometer_reading = 2000
my_toyota.read_odometer()
my_toyota.size_of_battery()'''











'''class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        new_name = str(self.year) + ' ' + self.model + ' ' + self.make
        return new_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it!")
        
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
        
    def size_of_battery(self):
        print("Battery size is " + str(self.battery_size) + "!")
        
my_new_car = Car('bmw','b5',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 2300
my_new_car.read_odometer()

class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
        
my_toyota = Electric_car('toyota','model t4',2018)
print(my_toyota.get_descriptive_name())
my_toyota.odometer_reading = 2000
my_toyota.read_odometer()
my_toyota.battery.size_of_battery()'''










'''class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        new_name = str(self.year) + ' ' + self.model + ' ' + self.make
        return new_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it!")
        
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
        
    def size_of_battery(self):
        print("Battery size is " + str(self.battery_size) + "!")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 250
            
        elif self.battery_size == 86:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
my_new_car = Car('bmw','b5',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 2300
my_new_car.read_odometer()

class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
        
my_toyota = Electric_car('toyota','model t4',2018)
print(my_toyota.get_descriptive_name())
my_toyota.odometer_reading = 2000
my_toyota.read_odometer()
my_toyota.battery.size_of_battery()
my_toyota.battery.get_range()'''
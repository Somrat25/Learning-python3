'''class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        a = str(self.year) + ' ' + self.model + ' ' + self.make
        return a.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it!")'''


class Car():
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
            
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        #message += " miles on a full charge."
        print(message)


class Electric_car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
        
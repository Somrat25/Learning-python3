'''from car import Car

my_new_car = Car('bmw','b4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 13
my_new_car.read_odometer()

my_used_car = Car('audi','a4',2010)
print(my_used_car.get_descriptive_name())
my_used_car.odometer_reading = 30000
my_used_car.read_odometer()'''


'''from car import Electric_car
my_toyota = Electric_car('toyota','model t4',2018)
print(my_toyota.get_descriptive_name())
my_toyota.odometer_reading = 2000
my_toyota.read_odometer()
my_toyota.battery.size_of_battery()
my_toyota.battery.get_range()'''


from car import Car, Electric_car

my_new_car = Car('bmw','b5',2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 2300
my_new_car.read_odometer()

my_toyota = Electric_car('toyota','model t4',2018)
print(my_toyota.get_descriptive_name())
my_toyota.odometer_reading = 2000
my_toyota.read_odometer()
my_toyota.battery.size_of_battery()
my_toyota.battery.get_range()
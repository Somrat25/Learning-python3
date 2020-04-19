print("Hello World!")

message = "hello world!"
print(message)
print(message.title())
print(message.upper())
print(message.lower())


first_name = "moshahed"
last_name = "somrat"
full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)

print("\tPython")
print('\nPython')
print("Language : \nPython\nHTML\nCSS")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favourite_language = "python"
print(favourite_language.rstrip())

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

import this

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[1].title())
print(bicycles[-1])
print(bicycles[-1].title())
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
bicycles[0] = 'std'
print(bicycles)
bicycles.append('tds')
print(bicycles)
cars = []
cars.append('bmw')
cars.append('audi')
print(cars)
cars.insert(0,'toyota')
print(cars)
del cars[0]
print(cars)
poped_cars = cars.pop()
print(cars)
print(poped_cars)
print("The last car I owned was a " + poped_cars.title() + ".")
po_cars = cars.pop(0)
print("The last car I owned was a " + po_cars.title() + ".")

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.remove('trek')
print(bicycles)
bicycles.reverse()
print(bicycles)
bicycles.sort()
print(bicycles)
print("Here is the original list:")
print(bicycles)
print("\nHere is the sorted list:")
print(sorted(bicycles))

cars = ['bmw','audi','toyota']

for car in cars:
    print(car)
    print(car.title() +" is a great car!")
    
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1,5):
    print(value)
    
x = list(range(1,6))
print(x)
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])
print(players[:4])
print(players[1:])
print(players[-1:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('burger')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

x = (20,30)
print(x)
print(x[1])
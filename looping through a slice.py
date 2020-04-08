#looping through a slice
players=['sam','mak','messi','neymar']
print('Here are my last three players')
for player in players[1:]:
    print(player.title())
    
#scopying a list
names=['sam','messi','neymar']
my_name=names[:]
print('all names are')
print(names)

print('n\my names are')
my_name.append('kiwi')

print(my_name)
    
#Exercise 4-10(try it myself)
    #1
fruits=['apple','banana','cherry','orange','mango']
print('Here are the first three items in the list are:')
for fruit in fruits[:3]:
    print(fruit.title())
    
    #2
print('Three items from middle:')
for fruit in fruits[1:4]:
    print(fruit.title())

    #3
print('Last three items in the list are:')
for fruit in fruits[2:]:
    print(fruit.title())

#Exercise 4-11(try it myself)

my_names=['sam','somrat','moshahed']
your_names=my_names[:]
print('My favourite names are:')
for my_name in my_names:
    print(my_name.title())

print('n\ your favourite names are:')
for your_name in your_names:
    print(your_name.title())
print('my names are')
my_names.append('moshahed somrat')
print(my_names)

print('n\Your names are:')
your_names.append('ms')
print(your_names)
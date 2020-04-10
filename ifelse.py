'''cars=['audi','bmw','ducati']
for car in cars:
    if 'bmw' in car:
        print(car.lower())
        
    else:
        print(car.title())'''
        
'''car='bmw'
#if car != 'bmw':
if car != 'audi':
    print('No')'''
    

'''cars=['bmw','audi','ducati','honda']
boat='titanic'
if boat not in cars:
    print('yes,'+boat+ ' is not in list')'''

'''age=21
if age>=22:
    print('yes,you can watch porn')
else:
    print('you are not ')'''
'''age=3
if age<4:
    price=0
        #print('admission cost is free')
#elif age>4 and age<18:
elif age<18:
    price=5
        #print('admission fee is $5')
else:
        age>18
        price=10
        #print('admission fee is $10')
print('Your admission cost is $'+str(price)+'.')''' 


        


'''age=17
if age<4:
    price=0
elif age<18:
    price=10
elif age<65:
    price=5
else:
    price=5
print('Admission cost is $'+str(price)+'.')'''

#Exercise 5-3 5-4 5-5 5-6 Alien colors

'''alien_colors=['green','yellow','red']
if 'green' in alien_colors:
    print('you earn 5 points')
alien_color='green'
if 'red' in alien_color:
    print('yes')
#else:
    #print('no')
    if alien_color != 'red':
        print('oh')'''
#exercise 5-5
'''alien_color='green'
if alien_color is 'red':
    print('you earn 5 points')
elif alien_color is 'green':
    print('You earn 15 points')
else:
    print('you earn 10 points')'''
#exercise 5-6
'''age=54
if age<2:
    print('The person is a baby')
elif age<4:
    print('The person is a toldler')
elif age<13:
    print('The person is a kid')
elif age<20:
    print('The person is a teenager')
elif age<65:
    print('The person is an adult')
else:
    print('The person is elder')'''

#Exercise 5-7
'''favourite_fruits=['mango','banana','waterlemon']
if 'mango' in favourite_fruits:
    print('I really like mango')
if 'banana' in favourite_fruits:
    print('I really like banana')
if 'apple' in favourite_fruits:
    print('I really like apple')
if 'pineapple' in favourite_fruits:
    print('I really like pineapple')
if 'waterlemon' in favourite_fruits:
    print('I really like waterlemon')
print('\n finished')'''





'''teams=['bangladesh','pakistan','australia','india','sri lanka','afganistan']
for team in teams:
    if team == 'afganistan':
        print('Too much weak team. ')
    else:
        print('Best in cricket, '+team.title()+'.')
        
    #if 'bangladesh' in team:
       # print('yes')
       #print('Best in cricket, '+team.title()+'.')'''
       
'''teams=[]
if teams:
    for team in teams:
        print('Best in cricket, '+team.title()+'.')
else:
        print('Is there any other best team?')'''
#Exercise 5-8, 5-9
'''#usernames=['moderator','admin','patient','sam','somrat']
usernames=[]
for username in usernames:
    if username=='admin':
        print('Hello '+username+', thank you for login')
    print('hello '+username+', how are you?')
else:
    print('We need to find some users')'''
    #Exercise 5-10
'''usernames=['moderator','admin','patient','sam','somrat']
new_usernames=['admin','moshahed','sam']
for new_username in new_usernames:
    if new_username in usernames:
        print('you '+new_username)
    else:
        print('You need to add another name '+new_username)'''
        
'''#Exercise 5-11
numbers=[1,2,3,4,5,6,7,8,9]
#for number in numbers:
    #print(number)'''

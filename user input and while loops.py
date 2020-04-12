'''message=input('Tell something :')
print(message)'''

'''name = 'Tell me your name '
name+='\nIs this your real name? '
names =input(name)
print('\nHello , ' + names + '.')'''




#Int()
'''age = input('How old are you?')
age=int(age)
if age<=21:
    print('\nYou are not allowed to ride .')
else:
    print('\nYou can ride here .')'''




'''height=input('How tall you are ? Height in inches :')
height=int(height)

if height>=60:
    print('\nYou can go there.')
else:
    print("\nYou can't go there!")'''
    
    
    


#Modulo
'''number=input('Even number presentation by modulo operator :')
number=int(number)

if number % 2 == 0:
    print('This is an even number!')
else:
    print('This is an odd number .')'''
    
    
    
########################    While loop
#name = input('Tell me your name :')


'''id_no = 11170120037
while id_no<=11170120068:
    print(id_no)
#print(str(id_no) +':'+ name)
    id_no+=1'''
    
    
    
    
    
'''message = '\nHey ! What are you looking for ??'
message += "\nEnter 'doll' to end the program :"

messages =" "
while messages != 'doll':
    messages=input(message)
    if messages !='doll':
        print(messages)'''
        
        
        
        
        
        
'''prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
         active = False
    else:
         print(message)'''
    
    
    




'''message = '\nHey ! What are you looking for ??'
message += "\nEnter 'doll' to end the program :"

active = True
while active:
    dress = input(message)
    if dress == 'doll':
        active = False
    else:
        print(dress)'''
        
        
        
        
        
        
'''message = '\nHey ! What are you looking for ??'
message += "\nEnter 'doll' to end the program :"

while True:
    dress = input(message)
    
    if dress == 'doll':
        break
    else:
        print("I'd love to buy :" + dress.title())'''
        
        
        
        
        
        
        
        
#Exercise 7-4 to 7-7
        
'''prompts = "\nEnter a pizza name "
prompts += "\nEnter 'quit' to end :" 

message =" "

while message != 'quit':
    message = input(prompts)
    if message != 'quit':
        print(message)'''
        





'''age= input("\nEnter your age here : ")
age = int(age)

if age<3:
    print("\nThe ticket is free")
elif age<12:
    print("\nThe ticket is $10")
else:
    print("\nthe ticket is 15$")'''
    
    
    
    
    
    
'''id=1
while id<5:
    print(id)'''
    
    
    
#using a while loop with lists and dictionaries
    
    
'''unconfirmed_users = ['sam','somrat','moshahed']
confirmed_users = []

while unconfirmed_users :
    current_user = unconfirmed_users.pop()
    print("Verified users: " +current_user.title() +".")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")   
for confirmed_user in confirmed_users:
    print(confirmed_user.title())'''
    
    
'''pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)'''



'''u_ss = ['s','p','d']
cs = []
while u_ss:
    c_us = u_ss.pop()
    print(c_us)
    cs.append(c_us)
print("dfs")
for css in cs:
    print(css.title())'''
    
    
    
    
    

    
    
    
'''responses = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name?")
    response = input("\nWhice mountain would you like to climb?")
    responses[name] = response
    repeat = input("\nWould you like to climb another mountain? (Yes or NO)")
    if repeat == 'no':
        poll_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")'''

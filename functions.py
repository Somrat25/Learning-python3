'''#defining a function

def greet_user():
    print('Hello!')
greet_user()'''



'''#Passing Information to a Function 


def greet_user(username):
    print('Hello, ' +username.title()+'!')
greet_user('sam')'''


#Exercise 8-1 & 8-2


'''def display_message():
    print('What are you learning in this chapter?')
display_message()'''




'''def favourite_book(title):
    print('One of my favorite books is , ' +title.title()+'!')
favourite_book('Alice in Wonderland')'''




#Positional Arguments


'''def favourite_bodyspray(spray_type,spray_name):
    print('The type is '+spray_name+'.')
    print('The name is '+spray_name.title()+' '+spray_type.title()+'.')
favourite_bodyspray('master','fogg')'''





'''def describe_pet(animal_type, pet_name):
     print("\nI have a " + animal_type + ".")
     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')'''




'''#Multiple Function Calls
def describe_pet(animal_type, pet_name):
     print("\nI have a " + animal_type + ".")
     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('lobstar','larry')'''



'''#Keyword arguments


def describe_pet(animal_type, pet_name):
     print("\nI have a " + animal_type + ".")
     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')'''



'''#Defaut Values


def describe_pet(animal_type, pet_name='harry'):
     print("\nI have a " + animal_type + ".")
     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster')
#describe_pet('willie')
#describe_pet(pet_name='harry', animal_type='hamster')'''




'''#Return Values


def get_formatted_name(first_name,last_name):
    full_name = first_name+' '+ last_name
    return full_name.title()
cricketer = get_formatted_name('mushfiqur','rahim')
print(cricketer)'''

'''def get_formatted_name(first_name,middle_name,last_name):
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name.title()
cricketer = get_formatted_name('shakib','al','hasan')
print(cricketer)'''


'''#Making an Argument Optional

def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
        
    else:
        full_name = first_name +' '+last_name
    return full_name.title()
cricketer = get_formatted_name('mushfiqur','rahim')
print(cricketer)

cricketer = get_formatted_name('shakib','al','hasan')
print(cricketer)'''


#Returning a Dictionary

'''def build_data(first_name,last_name):
    person_name = {'first':first_name,'last':last_name}
    return person_name
cricketer = build_data('moshahed','somrat')
print(cricketer)'''


'''def build_data(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
cricketer = build_data('moshahed','somrat',age=25)
print(cricketer)'''


'''#Using a Function with a while Loop 

def get_formatted_name(first_name,last_name):
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' to end this program)")
    
    f_name = input("first_name")
    if f_name == 'q':
        break

    l_name = input("last_name")
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")'''



'''#Passing a List


def formatted(names):
    
    for name in names:
        message = "Hello , " + name.title() + "!"
        print(message)
        
usernames = ['sam','somrat']
formatted(usernames)'''


'''#Modifying a list with function


def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design.title())
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['samsung','iphone']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)'''




'''def print_models(unfinished_models,completed_models):
    while unfinished_models:
        current_models = unfinished_models.pop()
        print(current_models)
        completed_models.append(current_models)
        
def show_completed_models(completed_models):
    print("eWRr")
    for completed_model in completed_models:
        print(completed_model)
        
unfinished_models =['aaa','sss']
completed_models = []

print_models(unfinished_models,completed_models)
show_completed_models(completed_models)'''



'''#Exercise 8-9,8-10,8-11

def show_magicians(names):
    for name in names:
        print(name.title())
        
def make_great(names):
    great_names = []
    
    while names:
        name = names.pop()
        great_name = name + " the great"
        great_names.append(great_name)
        
    for great_name in great_names:
        names.append(great_name)
        
        
        
magicians = ['sam','somrat']
show_magicians(magicians)


print("\n")
make_great(magicians)
show_magicians(magicians)'''


#Arbitrary arguments

'''def my_function(*kids):
  print("The youngest child is " + kids[2] +".")

my_function("Emil", "Tobias", "Linus")'''


'''def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(topping)
        
make_pizza('pepperoni')'''


'''def make_pizza(size,*toppings):
    print("\nMaking a pizza with "+str(size)+ " inch following toppings:")
    for topping in toppings:
        print(topping)
        
make_pizza(27,'pepperoni')'''



'''def build_profile(first,last,**user_info):
    profile={}
    profile['First name']=first
    profile['Last name']=last

    for key, value in user_info.items():
        profile[key] = value
        return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)'''
        


'''def make_pizza(size,*toppings):
    print("\nMaking a pizza with "+str(size)+ " inch following toppings:")
    for topping in toppings:
        print(topping)
        
import pizza
pizza.make_pizza(16, 'pepperoni')'''
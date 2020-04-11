#Dictionaries
'''person={'name':'sam' , 'age':24}
print(person['name'])
print(person['age'])'''



#Accessing Values in a Dictionary
'''alien_0={'color':'green','point':5}
new_point=alien_0['point']
print('You just earned '+str(new_point)+' points!')
'''



#Adding New Key-Value Pairs 
'''alien_0={'color':'green', 'points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)'''




#Empty string
'''alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)'''




#Modifying Values in a Dictionary
'''alien_0={'color':'green'}
print('You kill '+alien_0['color']+' color alien!')
alien_0['color']='yellow'
print('Now alien color is '+alien_0['color'])'''




'''alien_0={'x_position' : 0 , 'y_position' : 25 ,'speed' : 'fast'}
print('Orginal x-position: '+str(alien_0['x_position']))
if alien_0 ['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position']=alien_0['x_position'] + x_increment
print('New position: '+str(alien_0['x_position']))'''




#Removing key value
'''alien_0={'color' : 'green' , 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)'''



#Removing key value pairs
'''alien_0={'color':'green' , 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)'''



#A dictionary of similar object
'''favourite_languages={
        'sam' : 'python',
        'sakib' : 'java',
        'tamim' : 'c',
        'soumya' : 'c++'
        }
print(favourite_languages)
print("Sam's favourite language is " + favourite_languages['sam'].title()+".")'''


#Exercise 6-1
#Looping through all key value pairs
'''person_information = {
        'first_name' : 'moshahed',
        'last_name' : 'somrat',
        'city' : 'khulna'
        }
for key, value in person_information.items():
    #print(person_information)
    print('\nkey : ' + key.title())
    print('value : ' + value.title())'''






'''favourite_languages={
        'sam' : 'python',
        'sakib' : 'java',
        'tamim' : 'c',
        'soumya' : 'c++'
        }
#print(favourite_languages)
for name, language in favourite_languages.items():
    print(name.title() +"'s favourite language is " +language.title()+".")'''
    
    
    
#Looping Through All the Keys in a Dictionary
    
'''favourite_languages={
        'sam' : 'python',
        'sakib' : 'java',
        'tamim' : 'c',
        'soumya' : 'c++'
        }
#for name in favourite_languages.keys():
   #print(name.title())
for language in favourite_languages.values():
    print(language.title())'''
    
    


#A list of dictionaries
    
'''alien_0 = {'color' : 'green' , 'points' : 5}
alien_1 = {'color' : 'yellow' , 'points' : 10}
aliens = [alien_0 , alien_1]
for alien in aliens:
    print(alien)'''


'''aliens = []

for alien in range(30):
    new_alien = {'color' : 'green' , 'points' : 5}
    aliens.append(new_alien)
    
    for alien in aliens[0:10]:
        print(alien)
    print('...')'''
'''try:
    print(5/0)
except ZeroDivisionError:
    print("Nothing can't divided by zero!")
    
    


print("Give me two numbers and I'll divide them:")
print("Enter 'q' to exit")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    last_number = input("Last number: ")
    if last_number == 'q':
        break
    try:
        answer = int(first_number)/int(last_number)
    except ZeroDivisionError:
            print("Can't divide by zero")
    else:
        print(answer)'''
        
'''f = open("bd.txt" , "rt")
#print(f.read())
#print(f.read(10))
#print(f.readline())
print(f.readline())
f.close()
#for x in f:
    #print(x)
    
    
f = open("bd.txt" , "a") #append a file
f.write("This is a great country.")
f.close()

f = open("bd.txt","r") #read a file
print(f.read())
f.close()


f = open("aaa.txt" , "x") #creat a new file'''

try:
    f = open("hd.txt")
except FileNotFoundError:
    print("File doesn't exist")
    
    
try:
    print(x)
except NameError:
    print('not exist')
except:
    print('someting went wrong')
    

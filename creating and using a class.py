class Dog():
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is sitting now !")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")
        
my_dog = Dog("edward",2)
print("My dog name is " + my_dog.name.title() + "!")
print(my_dog.name.title() + " is " + str(my_dog.age) +" years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('collen',3)
print("\nYour dog name is " + your_dog.name.title() + "!")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
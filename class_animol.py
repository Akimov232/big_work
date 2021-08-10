class Animal():
    def __init__(self , name , color):
        self.name = name 
        self.color = color 
    
    def sleep(self):
        print(f"{self.name} Zzzz")
    
    def eat(self):
        print(f"{self.name } Om nom nom...")

class Cat(Animal):
    def say(self):
        print(f"Meow!!!")

class Dog(Animal):
    def say(self):
        print(f"Bark!!!")


fluffy = Cat('Snowball' , 'white')

fluffy.say()

cooper =  Dog('Cooper ' , 'red ')

cooper.say()
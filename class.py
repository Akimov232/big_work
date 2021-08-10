class Cat():
    def __init__(self , name , color):
        self.name = name 
        self.color = color 
    
    def sleep(self):
        print(f"{self.name} Zzzz")
    
    def eat(self):
        print(f"{self.name } Om nom nom...")


fluffy = Cat("Snowball" , 'white')   

smokey = Cat('Smokey' , 'grey')



smokey.eat()
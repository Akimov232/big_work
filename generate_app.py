foo = ['*' , '_' , '_']

from random import randint
rand = randint(1 , 3)

foo[rand] = '~'

print(foo)
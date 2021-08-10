def build(w):
    for i in range(w):
        print(str (i + 1 )* (i + 1) )

def user_guess():
    return int(input("Введите число:"))

def base():
    number_user = user_guess()
    build(number_user)
base()
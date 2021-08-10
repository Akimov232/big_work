def build_pyromix(r):
    for i in range(r // 2):
        print('*' * (i + 1))

    for i in ((r//2) + 1 , 0 , -1):
        print('*' * (i))

def user_number():
    return int(input("Ввидите нечетное число:"))

def pyrom():
    number = user_number()
    if number  %2 == 0:
        print("Введите нечетное число:")
    else:
        build_pyromix(number)
pyrom()
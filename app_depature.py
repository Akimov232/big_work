plane_info = [243 , 345]

def skrech_number(w):
    flag = True
    for r in w:
        if r == user_guess:
            return flag == True 
        else:
            flag == False
    return flag 

def resalt(q):
    if q ==True:
        print("Ваш рейс найден")
    elif q ==False:
        print("Ваш рейс не найден")
    else:
        print("Ошибка ")


def user_guess():
    return int(input("Введите номер вашего рейса(только цыфры):"))


def main():
    user_guess()
    skrech_of_plane = skrech_number(plane_info)
    resalt(skrech_of_plane)
main()
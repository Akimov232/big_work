from random import randint

game = True
num = randint(1 , 100)

file = open("game_random_1" , "w" , encoding="utf8")

print("Поробуй отгадать число ")

file.write("Поробуй отгадать число \n ")
while game:
    guess = int(input("Введи число:"))
    file.write(f"Введи число:{guess}\n")
    if guess == num:
        print("Вы угадали число")
        file.write("Вы угадали число\n")
        break
    elif guess < num:
        print(f"ответ неверный , поробуй число больше чем {guess}")
        file.write(f"ответ неверный , поробуй число больше чем {guess}\n")
    elif guess > num:
        print(f"ответ неверный , поробуй число меньше чем {guess}")
        file.write(f"ответ неверный , поробуй число меньше чем {guess}\n")
hb = {
    'Богдан': '10/12/05',
    'Маша': '06/01/06',
    'Мама': '14/02/69'
}
print("Добро пожаловать в базу данных <Дни Рождения> от Даниила")
for name in hb:
    print(name )

name = input("Введите имя:")

if name in hb:
    print(f"День рождения {name} - {hb[name]}")
else:
    print(f"В нашей базе данных нет {name}")
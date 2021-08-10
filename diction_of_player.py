name_of_player = ['штурмовик' , 'андроид']
items = ['мечь' , 'автомат' , 'пистолет']
potion = ['здоровье' , 'хилка']

def create_char(name , char_class ,cher_items ,char_position ):
    return {name:{char_class:{'предмет':cher_items , 'дополнение':char_position}}}

character_name = input("Введите имя вашего игрока:")

choose_class = input(f'Выбирите класс вашего игрока::{" ".join(name_of_player)}:')

if choose_class not in name_of_player:
    choose_class = input(f'Данного класа нет в нашей базе данных, введите класс заново:{" ".join(name_of_player)}:')

choose_items = input(f'Выбирите предмет для вашего игрока: {" ".join(items)}:')

if  choose_items not in items:
    choose_items = input(f'Данного придмета  нет в нашей базе данных, введите придмет заново:{" ".join(items)}:')

choose_potion = input(f'Выберите дополнение к вашему игроку:{" ".join(potion)}:')

if  choose_potion  not in potion:
    choose_potion = input(f'Данного дополнения  нет в нашей базе данных, введите дополнения заново:{" ".join(potion)}:')

character = create_char(character_name , choose_class ,  choose_items ,choose_potion )

print(f'Мы создали вашего персанажа{character}')





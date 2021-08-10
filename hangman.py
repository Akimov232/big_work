from random import choice

def generate_word(w):
    '''
    input: list of words 
    output: 1 word which generated choice 
    '''
    return choice(w)

def start_string(w):
    tp = []
    for i in w :
        tp.append('_')
    return tp

def welcome_speake(t):
    print(f'''Добро пожаловать в игру hangman2000
    Вам надо отгадать словов за три попытки или вы проиграете!
    Загаданное слово состоит из {len(t)} букв {t}
    ''')

def user_guess():
    return input("Введите букву:")


def build_tamplate_in_game(w , r , n=''):
    for i in range(len(r)):
        if w[i] == '_':
            if r[i] == n:
                w[i] = r[i]
            else:
                w[i] = '_'
    return w


def listen_convert(t):
    s = ''
    return s.join(t)


def print_resalts(w):
    print(f"Ваш результат:{w}")


def check_win(w):
    for i in w:
        if i == '_':
            return True 
    return False
        

def check_mistake(w, g):
    foo = False  
    for i in w:
        if i == g:
            foo = True 
    return foo 

def check_lifes(life):
    life = life - 1 
    return life 


def lose_print():
    print("Вы проиграли!")

def win_print():
    print("Поздравляю, Вы выйграли!")




def main():
    game = True 
    lifes = 3 
    word = ['ban' , 'daniil' , 'love']
    word_play = generate_word(word)
    string = start_string(word_play)
    welcome_speake(listen_convert(string))
    
    while game:
        user_input = user_guess()
        tamplate = build_tamplate_in_game(string , word_play , user_input)
        guessed = listen_convert(tamplate)
        print_resalts(guessed)
        game = check_win(guessed)

        if not check_mistake(word_play , user_input):
            print(f"У вас осталось {lifes} попыток!")
            lifes = check_lifes(lifes)

        if lifes == 0:
            lose_print()
        
        if not game :
            win_print()

main()
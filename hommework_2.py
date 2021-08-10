letter_all = 'фывапролджэйцукенгшщзхъячсмитьбю'
def letter_upper(w):
    '''
    input: string user
    output: list of quantity letter capital
    '''
    letter = 0
    for i in w:
        for q in letter_all.upper():
            if i == q:
                letter += 1
    return letter



def letter_lower(d):
    '''
    input: string user
    output: list of quanalty letter lower
    '''
    letter = 0
    for i in d:
        for q in letter_all.lower():
            if i == q:
                letter += 1
    return letter
         
string = 'Мамам  '


print(f"Всего больших букв:{letter_upper(string)}")
print(f"Всего маленьких букв:{letter_lower(string)}")
def build_filed(r):
    filed = []
    fileds = []
    for i in range(r):
        filed.append('_')
    for k in range(r):
        fileds.append(filed[:])
    return fileds 


def make_start_location(n):
    n[0][0] = 'x'
    return n 

def print_filed(n):
    for i in n:
        print(' '.join(i))


def start_up(n):
    filed_size = range(len(n))
    fide = n[:]
    for i in filed_size:
        for r in filed_size:
            if n[i][r] == 'x':
                fide[i] , fide[i - 1] = fide[i-1] , fide[i]
                break
    return fide 

def start_down(n):
    filed_size = range(len(n))
    fide = n[:]
    for i in filed_size:
        for r in filed_size:
            if n[i][r] == 'x':
                if i == len(n) - 1:
                    fide[0], fide[i - 1] = fide[i - 1] , fide[0]
                else:
                    fide[i] , fide[i + 1] = fide[i +1] , fide[i]
                    break
    return fide


def start_right(n):
    filed_size = range(len(n))
    fide = n[:]
    for i in filed_size:
        for r in filed_size:
            if n[i][r] == 'x':
                fide[i][r] = '_'
                if r == len(n) - 1:
                    fide[i][0] = 'x'
                else:
                    fide[i][r+1] = 'x'
                    break
    return fide 


def start_left(n):
    filde_size = range(len(n))
    fide = n[:]
    for i in filde_size:
        for r in filde_size:
            if n[i][r] == 'x':
                fide[i][r] = '_'
                fide[i][r -1] = 'x'
                break
    return fide 


def user_guess_direction():
    return input("Введите действие: up , down , right , left или  exit(что выйти )")



def user_input_size():
    return int(input("Введите размер поле:"))



def main():
    game = True
    size = user_input_size()
    make_filed = make_start_location(build_filed(size))
    print_filed(make_filed)
    while game:
        user_direction = user_guess_direction()

        if user_direction == 'up':
            make_filed = start_up(make_filed)
        if user_direction == 'down':
            make_filed = start_down(make_filed)
        if user_direction == 'right':
            make_filed = start_right(make_filed)
        if user_direction == 'left':
            make_filed = start_left(make_filed)
        if user_direction == 'exit':
            game = False 
        if game:
            print_filed(make_filed)

main()

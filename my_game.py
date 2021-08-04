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
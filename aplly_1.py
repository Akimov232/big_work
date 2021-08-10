def apply_to_each(L,F):
    for i in range(len(L)):
        L[i] = F (L[i])

    
numbers = [1 ,0 , 3.14 , -2]


def change_direction(w):
    return w * -1


apply_to_each(numbers , abs)
print(numbers)
apply_to_each(numbers , int)
print(numbers)
apply_to_each(numbers , float)
print(numbers)
apply_to_each(numbers , change_direction)
print(numbers)
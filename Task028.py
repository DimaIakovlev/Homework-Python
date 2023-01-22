import os
os.system('cls||clear')
a = int(input('Введите число \nа= '))
b = int(input('Введите второе число \nb='))
    
def sum(num_1, num_2):
        if num_1 == 0:
            return num_2
        elif num_1 > 0:
            return sum(num_1 - 1, num_2 + 1)
    
print(sum(a,b))

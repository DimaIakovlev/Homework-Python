import os
os.system('cls||clear')
a = int(input('Введите число \nа= '))
b = int(input('Введите его степень \nb='))

def recurs_exponentiation(start, exp):
    if exp ==1:
        return (start)
    if (exp !=1):
        return(start*recurs_exponentiation(start, exp-1))
    
print(recurs_exponentiation(a,b))
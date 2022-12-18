# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os
os.system('cls||clear')
n = int(input('Введите число N='))
i = 0
while 2 ** i <= n :
    print(i, 2 ** i)
    i += 1
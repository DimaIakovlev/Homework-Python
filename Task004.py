# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем 
# Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
import os
os.system('cls||clear')
a = int(input('Введите количество сделанных журавликов \nа= '))
if (a %6 == 0) :
    print ('Петя и Сережа сделали по', int(a /6) , 'а Катя сделала ', int(a/6*4), 'журавликов' )
else:
    print ('Неправильное количество журавликов!!!' )
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один 
# разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
import os
os.system('cls||clear')
n = int(input ('Введите число долек по вертикали N='))
m = int(input ('Введите число долек по горизонтали M='))
k = int(input ('Введите число долек которые хотите отломить K='))
if m * n > k :
    if k % n == 0 or k % m == 0 :
        print('YES - у Вас получится')
    else :
        print('NO - не выйдет столько отломить')
else :
    print('NO - не выйдет столько отломить')
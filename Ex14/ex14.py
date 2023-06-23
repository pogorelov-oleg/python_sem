# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = 1024

pow = 0
pow_list = []
while 2**pow <= n:
    pow_list.append(2**pow) 
    pow += 1
print(*pow_list)


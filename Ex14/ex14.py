# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = 1000

pow = 0
result = 0
pow_list = []
while 2**pow <= n:
    result = 2**pow
    pow_list.append(result) 
    pow += 1
print(*pow_list)


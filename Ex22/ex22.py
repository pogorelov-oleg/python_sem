# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n = int(input('Введите колличество элементов первого списка: '))
m = int(input('Введите колличество элементов второго списка: '))
nums1 = [random.randint(0, 10) for i in range (n)]
nums2 = [random.randint(0, 10) for i in range (m)]
# nums1 = [int(input(f'Введите {i + 1} число первого списка: ')) for i in range (n)]  
# nums2 = [int(input(f'Введите {i + 1} число второго списка: ')) for i in range (m)]  
print(*nums1)
print(*nums2)

new_nums = []
for i in nums1:
    if i in nums2 and not i in new_nums:
        new_nums.append(i) 

print(*sorted(new_nums))                                                           



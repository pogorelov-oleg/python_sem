# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

array = [random.randint(0,20) for i in range(10)]
print(array)
min_num = int(input("min number = "))
max_num = int(input("max number = "))

index_array = []
for i in array:
    if min_num <= i <= max_num:
        index_array.append(array.index(i))

print(index_array)

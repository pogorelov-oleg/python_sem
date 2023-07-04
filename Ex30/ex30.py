# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input("first element = "))
step = int(input("step = "))
arr_length = int(input("array length = "))

array =  [first_element]
for i in range(arr_length - 1):
    array.append(array[i] + step)
print(array)
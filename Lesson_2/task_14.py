#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите N "))

k = 0 

while (2**k < n):
    print(k)
    k += 1

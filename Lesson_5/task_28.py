#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#*Пример:*
#2 2
#    4 


a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

def summa(a, b, s=0):

    if a > 0:
        s += 1 
    
    if b > 0:
        s += 1 

    if a == 0 and b == 0:
        print(s)
        return s
    
    if a > 0: a -= 1
    if b > 0: b -= 1
    
    summa(a, b, s)


summa(a, b)
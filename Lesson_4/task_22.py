#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]

    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

def makeResultList(arr1, arr2):
    arr = arr1+arr2
    result_arr = []
    for i in arr:
        if i not in result_arr: 
            result_arr.append(i)
            
    return result_arr


n = int(input("Введите количество чисел в первом наборе "))
m = int(input("Введите количество чисел во втором наборе "))

list1 = []
list2 = []

for i in range(0, n):
    list1.append(int(input("Введите число для первого набора ")))

print(list1)

for i in range(0, m):
    list2.append(int(input("Введите число для второго набора ")))

print(list2)

merged = makeResultList(list1, list2)

sorted = quick_sort(merged)

print(sorted)
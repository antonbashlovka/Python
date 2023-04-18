#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).

length = int(input("Введите длину шоколадки "))
width = int(input("Введите ширину шоколадки "))

k = int(input("Введите количество долек, которые хотите отломить "))

s = length*width

possible = "no"
r = range(1, k)
if k < s:
    for a in r:
        if k/a == length or k/a == width or a == length or a == width:
            possible = "yes"



print(possible)
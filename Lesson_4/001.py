#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов 
#второго множества. Затем пользователь вводит сами элементы множеств.


list_1=[]
list_2=[]
n=int(input())
m=int(input())
for i in range (n):
    l1= int(input("Введите число для первого списка: "))
    list_1.append(l1)
for i in range (m):
    l2= int(input("Введите число для второго списка: "))
    list_2.append(l2)
print ()
set_1=set(list_1)
set_2=set(list_2)
a = set_1.intersection(set_2)
print (a)

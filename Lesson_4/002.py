""" Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит
из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь 
непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки. """

N=int(input("Введите количество кустов: "))
array = []
count = []
for i in range (N):
    print ("Номер куста", i)
    x=int(input("Введите количество ягод на кусте"))
    array.append(x)
for i in range (N-1):
    count.append(array[i-1]+array[i]+array[i+1])
count.append(array[i-2]+array[i-1]+array[0])
print(max(count))



'''2. В массиве действительных чисел все нулевые элементы заменить на среднее
арифметическое всех элементов массива.'''

print('Введите количество элементов массива ')
n=int(input()) #кол-во элементов массива
sum=0 #сумма элементов массива
sr=0 #среднее арифметическое элементов массива
x=[] #сам массив
print('Введите ', n, ' элементов массива')
for i in range(n):
    x.append(int(input())) #заполняем массив
print('Массив ',x)
for i in range(n):
    sum=sum+x[i] #находим сумму элементов массива
print('Cумма элементов масива ', sum)
sr=sum/n #находим среднее арифметическое эелементов массива
print('среднее арифметическое эелементов массива',sr)
for i in range(n):
    if x[i]==0:
        x[i]=sr #заменяем все 0 на среднее арифметическое эелементов массива
print('Изменённый массив', x) #выводим изменённый массив
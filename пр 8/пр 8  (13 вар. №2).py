'''2. Найти наибольший и наименьший элементы прямоугольной матрицы
и поменять их местами.'''

import math
print('2. Найти наибольший и наименьший элементы прямоугольной матрицы и поменять их местами.')
print('Давайте введём двумерный массив')
print('Введиет количество столбцов')
n=int(input())
print('Введиет количество строк')
m=int(input())
print('Введите сам двумерный массив')
a=[]
for i in range(n):
    b=[]
    for j in range(m):
        b.append((int(input())))
    a.append(b)
print('Ваш массив')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
minn=float('inf')
maxx=float('-inf')
for i in range(n):
    for j in range(m):
        if a[i][j]>maxx:
            maxx=a[i][j]
    for k in range(m):
        if a[i][k] < minn:
            minn = a[i][k]
for i in range(n):
    for j in range(m):
        if a[i][j]==maxx:
            a[i][j]=minn
        elif a[i][j]==minn:
            a[i][j]=maxx
print('Новый массив')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

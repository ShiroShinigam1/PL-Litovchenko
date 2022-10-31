'''1. Определить наименьший элемент каждой четной строки матрицы
А[М, N].'''

print('1. Определить наименьший элемент каждой четной строки матрицы  А[М, N].')
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
for i in range(n):
    for j in range(m):
        if i%2==0:
           print('Наименьший элемент строки',i,min(a[i]))
        break
'''1. Найти максимальный среди всех элементов тех строк заданной
матрицы, которые упорядочены (либо по возрастанию, либо по
убыванию).'''

print('1. Найти максимальный среди всех элементов тех строк заданной матрицы, которые упорядочены (либо по возрастанию, либо по убыванию).')
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
maxx=[] #отдельный списко для максимальных
for i in range(n):
        if a[i]==sorted(a[i]) or a[i]==sorted(a[i], reverse=True):
            maxx.append(max(a[i]))
print('Список максимальных чисел в упорядоченных строках ')
print(maxx)
'''2. Дана матрица B[N, М]. Найти в каждой строке матрицы
максимальный и минимальный элементы и поменять их с первым и
последним элементами строки соответственно.'''

print('2. Дана матрица B[N, М]. Найти в каждой строке матрицы максимальный и минимальный элементы и поменять их с первым и последним элементами строки соответственно.')
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
        minn=min(a[i])
        x=a[i].index(min(a[i]))
    tmin=a[i][0]
    a[i][0]=a[i][x]
    a[i][x]=tmin
for i in range(n):
    for j in range(m):
        maxx=max(a[i])
        y=a[i].index(max(a[i]))
    tmax=a[i][m-1]
    a[i][m-1]=a[i][y]
    a[i][y]=tmax
print('Новый массив')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
print('2. Найти наибольший и наименьший элементы прямоугольной матрицы и поменять их местами.')
with open('Литовченко_А.Р._УБ-23_vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print('Матрица')
    print(matrix)
n=len(matrix)
m=len(matrix[0])
a=matrix
for i in range(n):
    for j in range(m):
        a[i][j]=int(a[i][j])
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
with open('Литовченко_А.Р._УБ-23_vivod 13 вар. №2.txt', 'w', encoding='utf-8-sig') as f:
        f.write(str(a))

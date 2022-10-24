'''2. Даны 3 различных массива целых чисел (размер каждого не превышает 15). В
каждом массиве найти сумму элементов и среднеарифметическое значение.'''

print('Введите размер перваого массива (<16)')
x=int(input())
mx=[]
print('Введите размер второго массива (<16)')
y=int(input())
my=[]
print('Введите размер третьего массива (<16)')
z=int(input())
mz=[]
while x>15:
    print('Вы ввели неверный размер первого массива, попробуйте ещё раз')
    x = int(input())
while y>15:
    print('Вы ввели неверный размер второго массива, попробуйте ещё раз')
    y = int(input())
while z>15:
    print('Вы ввели неверный размер третьего массива, попробуйте ещё раз')
    z = int(input())
print('Размер массива х',x)
print('Размер массива y',y)
print('Размер массива z',z)
print('Завполните первый массив')
for j in range(x):
    mx.append(int(input()))
print('Массива х',mx)
print('Завполните второй массив')
for u in range(y):
    my.append(int(input()))
print('Массива y',my)
print('Завполните третий массив')
for e in range(x):
    mz.append(int(input()))
print('Массива z',mz)
def  sr(n):
    sum=0
    for i in range(n):
       sum=mx[i]+sum
    print('Сумма элементов массива равна',sum)
    s=sum/n
    print('Средне арифметическое значений первого массива', s)
    return s
def  sr(n):
    sum=0
    for i in range(n):
       sum=my[i]+sum
    print('Сумма элементов массива равна',sum)
    s=sum/n
    print('Средне арифметическое значений второго массива', s)
    return s
def  sr(n):
    sum=0
    for i in range(n):
       sum=mz[i]+sum
    print('Сумма элементов массива равна',sum)
    s=sum/n
    print('Средне арифметическое значений третьего массива', s)
    return s
sr(x)
sr(z)
sr(y)
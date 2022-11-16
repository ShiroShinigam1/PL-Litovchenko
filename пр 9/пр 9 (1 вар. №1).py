with open('Литовченко_А.Р._УБ-23_vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print('Матрица')
    print(matrix)
n=len(matrix)
m=len(matrix[0])
a=matrix
sum=0
kp=0
for i in range(n):
    for j in range(n):
        if j>i:
            sum+=int(a[i][j])
            if int(a[i][j])>0:
                kp=kp+1
print('Сумма элементов двумернрого массива находящихся над главной диагонялью ', sum)
print('Количество элементов двумернрого массива находящихся над главной диагонялью ', kp)
with open('Литовченко_А.Р._УБ-23_vivod 1 вар. №1.txt', 'a+', encoding='utf-8-sig') as f:
    f.write('Сумма элементов двумернрого массива находящихся над главной диагонялью ')
    f.write(str(sum))
    f.write('\n')
    f.write('Количество элементов двумернрого массива находящихся над главной диагонялью ')
    f.write(str(kp))
    f.write('\n')
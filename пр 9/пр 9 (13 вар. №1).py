with open('Литовченко_А.Р._УБ-23_vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print('Матрица')
    print(matrix)
n=len(matrix)
m=len(matrix[0])
a=matrix
for i in range(n):
    if i%2==0:
        mmin = min(a[i])
        with open('Литовченко_А.Р._УБ-23_vivod 13 вар. №1.txt', 'a+', encoding='utf-8-sig') as f:
            f.write('min элемент чётной cроки ')
            f.write(str(i))
            f.write('равен ')
            f.write(str(mmin))
            f.write('\n')
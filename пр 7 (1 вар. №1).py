#1. Составить программу для вычисления площади разных геометрических фигур.

import math
print('Если хотите найти площадь прямоугольника, нажмите 1')
print('Если хотите найти площадь треугольника, нажмите 2')
print('Если хотите найти площадь круга, нажмите 3')
print('Введите число ')
k=int(input())
'''while k!=1 or k!=2 or k!=3: #проверка на дурака почему то не работает
    print('Число введено не верно, попробуйте ещё раз ')
    k=int(input())'''
def pl(x,y):
    if k==1:
        s=x*y
        print('Площадь прямоугольника s=',s)
    if k==2:
        s=0.5*x*y
        print('Площадь треугольника s=',s)
    if k==3:
        s=x*x*math.pi
        print('Площадь круга s=',s)
    return s
if k==1:
    print('Введите стороны прямоугольника')
    a=int(input())
    print('a=', a)
    b=int(input())
    print('b=', b)
    pl(a,b)
elif k==2:
    print('Введите сторону треуголька')
    a=int(input())
    print('a=', a)
    print('Введите высоту треуголька проведённую к заданной стороне')
    h=int(input())
    print('h=', h)
    pl(a, h)
elif k==3:
    print('Введите радиуc круга')
    r= int(input())
    print('r=', r)
    pl(r, 1)
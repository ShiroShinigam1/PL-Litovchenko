'''1. На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из
цифр а, b, с.'''

from random import randint
print('На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из цифр а, b, с.')
N = int(input('Введите число 210 < N < 231 '))
while N < 210 or N > 231:
    print('Вы ввели неверное значение, попробуйте ещё раз')
    N = int(input())
def p(n):
    k = 0
    a = [i for i in range(0, 10)]
    for i in a:
        for j in a:
            for g in a:
                if g != j and j != i and g != i:
                    x = g * 100 + k * 10 + i
                    if x >= 100 and x < N:
                        k += 1
    return k
print(p(n))
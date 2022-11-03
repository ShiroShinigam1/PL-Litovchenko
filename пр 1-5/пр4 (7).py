n=int(input('Ввежите число n '))
fac=1
sum=0
for i in range(1,n):
    fac=fac*i
    sum=sum+fac
fac=fac*n
sum=sum+fac
print('Сумма  n факториалов равна ',sum)
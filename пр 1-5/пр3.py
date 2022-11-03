k=int(input('Введите число k '))
с=int(input('Введите число с '))
if k<5 and с>4:
       print('x=',k+с**2)
elif k>с and k>3:
    print('x=',с**2+2)
else:
    print('x=',с-1)
print('='*30)
print('BANCO 24H')
print('='*30)
valor = int(input('Qual valor você deseja sacar? '))
total = valor
ced = 50 #cedula
tce = 0 #total de cédula
while True:
    if total >= ced:
        total -= ced
        tce += 1
    else:
        if tce > 0:
            print('Total de {} cédulas de R${}'.format(tce, ced))
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            tce = 0
            if total == 0:
                break




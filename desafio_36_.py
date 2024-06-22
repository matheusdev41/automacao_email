vc=float(input('Qual o valor da casa: '))
s=float(input('Qual o salário do comprador: '))
p=int(input('Em quantos anos será o pagamento: '))
pm=(vc/p)/12
if pm > (0.3*s):
    print('Infelizmente seu empréstimo foi recusado')
elif pm < (0.3*s):
    print('O empréstimo foi aprovado, sua parcela será de R${:.2f} por mês'.format(pm))

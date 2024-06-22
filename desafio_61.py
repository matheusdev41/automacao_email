print ('GERADOR DE PA')
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = pt #irá começar com o primeiro termo
count = 1 #irá começar com 1 para mostrar os 10 primeiros termos
while count <= 10:
   print('{}'.format(termo), end=' ')
   termo += r
   count += 1

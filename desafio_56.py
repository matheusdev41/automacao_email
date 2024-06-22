somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1,5):
     print('{}ª PESSOA'.format(p))
     nome = str(input('NOME: ')).strip()
     idade = int(input ('IDADE: '))
     sexo = str(input('SEXO [M/F]: ')).strip()
     somaidade += idade
     if p == 1 and sexo in 'mM':
         maioridadehomem = idade
         nomevelho = nome
     if sexo in 'mM' and idade > maioridadehomem:
         maioridadehomem = idade
         nomevelho = nome
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O nome do homem mais velho é {}'.format(nomevelho))




















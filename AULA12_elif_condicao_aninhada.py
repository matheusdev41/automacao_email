nome=str(input('Qual é o seu nome: ')).strip()
if nome == 'Matheus':
    print('Que nome bonito, {}!'.format(nome))
elif nome == 'Cláudia' or nome == 'José':
    print('Que nome engraçado, {}!.'.format(nome))
elif nome in 'Ana Jéssica':
    #in neste caso para determinar se existe a palavra ana ou jessica na string nome
    print('Seu nome é bem brasileiro,{}!'.format(nome))
else:
    print('Seu nome é bem normal, {}'.format(nome))
print('Tenha um bom dia, {}'.format(nome))




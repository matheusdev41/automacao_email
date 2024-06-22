num=int(input('Digite um número: '))
esc=str(input('Digite 1 para binário \nDigite 2 para octal \nDigite 3 para hexagonal: '))
if esc == '1':
    print('O número {} convertido para binário é {}'.format(num,bin(num)[2:]))
elif esc == '2':
    print('O número {} convertido em octal é {}'.format(num,oct(num)[2:]))
elif esc == '3':
    print('O número {} convertido em hexagonal é {}'.format(num,hex(num)[2:]))
print('FIM')



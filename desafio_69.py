print('='*20)
print('CADASTRO DE PESSOAS')
mai = 0
hom = 0
m20 = 0
ida = int(input('IDADE: '))
sex = str(input('SEXO [F/M]: ')).upper().strip()
print('='*20)
esc = str(input('QUER CONTINUAR? [S/N]? ')).upper().strip()
print('='*20)
if ida >= 18:
    mai += 1
if 'M' in sex:
    hom += 1
if 'F'.upper() in sex and ida >= 20:
    m20 += 1
while esc == 'S':
    if esc == 'N':
        break
    print('CADASTRO DE PESSOAS')
    ida = int(input('IDADE: '))
    sex = str(input('SEXO [F/M]: ')).upper()
    esc = str(input('QUER CONTINUAR? [S/N] ')).upper()
    print('='*20)
    if ida >= 18:
        mai += 1
    if 'M' in sex:
        hom += 1
    if 'F' in sex and ida <= 20:
        m20 += 1
print('======= FIM DO PROGRAMA ======= ')
print('Total de pessoas com mais de 18 anos: {}\n'
      'Ao todo temos {} homens cadastrados\n'
      'E temos {} mulheres com menos de 20 anos'.format(mai, hom, m20 ))


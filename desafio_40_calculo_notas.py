import math
n1=float(input('Nota 1 do aluno: '))
n2=float(input('Nota 2 do aluno: '))
m=(n1+n2)/2
if m < 5:
    print('MÉDIA FINAL: {:.2f}\nSITUAÇÃO: REPROVADO\nESTUDE MAIS'.format(m))
elif 5 <= m <= 6.9:
    print('MÉDIA FINAL: {:.2f}\nSITUAÇÃO: RECUPERAÇÃO\nQUASE LÁ'.format(m))
elif m >= 7:
    print('MÉDIA FINAL: {:.2f}\nSITUAÇÃO: APROVADO\nBOAS FÉRIAS'.format(m))


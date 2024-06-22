a=float(input('Seguimento 1: '))
b=float(input('Seguimento 2: '))
c=float(input('Seguimento 3: '))
if a < c+b and b < a+c  and c < a+b:
    #cada seguimento tem que ser menor que a soma de cada um deles para ser um triângulo
    print('Os seguimentos formam um triângulo')
elif a == b == c:
    print('TRIÂNGULO EQUILÁTERO')
elif a == b and a != c:
    print('TRIÂNGULO ISÓSCELES')
elif a != b != c:
    print('TRIÂNGULO ESCALENO')
elif
    print('Os seguimentos não formam um triângulo')









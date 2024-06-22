import datetime
ano=int(input('Ano do nascimento do atleta: '))
#ano atual
ant=datetime.date.today().year
id=ant-ano
if id <= 9:
    print('A categoria do atleta é MIRIM\npor ter até {} anos'.format(id))
elif id <= 14:
    print('A categoria do atleta é INFANTIL\npor ter até {} anos'.format(id))
elif id <= 19:
    print('A categoria do atleta é JUNIOR\npor ter até {} anos'.format(id))
elif id <= 20:
    print('A categoria do atleta é Sênior\npor ter até {} anos'.format(id))
else:
    print('A categodia do atleta é MASTER\npor ter acima de 20 anos')


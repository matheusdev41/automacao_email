import datetime
nas=int(input('Qual o ano do seu nascimento: '))
ano=datetime.date.today().year
ida= ano-nas
if ida < 18:
    print('Você tem {} anos\n e por isso ainda vai se alistar no exército!'.format(ida))
elif ida == 18:
    print('Você tem {} anos\n e por isso está na hora de se alistar no exército'.format(ida))
elif ida > 18:
    print('Você tem {} anos\n e por isso já passou do tempo de alistamento'.format(ida))

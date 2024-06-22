import time
num=int(input('Digite um número: '))
print('A tabua da do número {} é:'.format(num))
time.sleep(1.5)
for c in range(1,10):
    print(c, 'x', num,'=', num*c)
    time.sleep(2)








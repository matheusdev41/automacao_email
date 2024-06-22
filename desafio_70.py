print('======= RECIBO DE VENDA =======')
pro = str(input('PRODUTO: ')).upper()
pre = float(input('PREÇO: '))
esc = str(input('ADICIONAR MAIS PRODUTOS?[S/N] ')).strip().upper()
tot = pre
pdb = 0   #preço do produto barato
npb = ''  #nome do produto barato
pcm = 0   #produtos que valem mais de 1000
count = 0
while esc == 'S':
    if esc == 'N':
        break
    pro = str(input('PRODUTO: ')).upper()
    pre = float(input('PREÇO: '))
    esc = str(input('ADICIONAR MAIS PRODUTOS?[S/N] ')).strip().upper()
    tot = tot + pre
    if pre >= 1000:
        pcm = pcm + 1
    count += 1
    if count == 1:
        pdb = pre
        npb = pro
    if pre < pdb:
        pdb = pre
        npb = pro
print('='*20)
print('TOTAL DA COMPRA = R${}0'.format(tot))
print('QUANTIDADE DE PRODUTOS QUE CUSTAM MAIS QUE R$1000,00: {}'.format(pcm))
print('O PRODUTO COM O MENOR PREÇO É {} CUSTANDO R${}0'.format(npb, pdb))



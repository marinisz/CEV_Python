resp = ''
soma = 0
mil = 0
barato = 9999999
produtobarato = ''
produto = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = int(input('Digite o valor: '))
    print('\033[31m---BIP---\033[m')
    resp = str(input('Deseja passar outro produto? [S/N]')).upper().strip()
    soma = soma + valor
    if valor < 1000:
        mil +=1
    if valor < barato:
        barato = valor
        produtobarato = produto
    if resp == 'N':
        break
print(f'\033[34mTotal da compra = {soma}')
print(f'O produto mais barato é {produtobarato}')
print(f'{mil} produtos custam menos que R$1.000,00')
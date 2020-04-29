galera = list()
pessoa = dict()
contpessoa = 0
medidade = 0
while True:
    pessoa.clear()
    pessoa['NOME'] = str(input('Digite seu nome: '))
    while True:
        pessoa['SEXO'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['SEXO'] in 'MF':
            break
        print('Erro! Digite somente M ou F')
    pessoa['IDADE']= int(input('Digite sua idade: '))
    medidade = pessoa['IDADE'] + medidade
    galera.append(pessoa.copy())
    contpessoa += 1
    while True:
        resp = str(input('Deseja adicionar mais alguém [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        if resp not in 'SN':
            print('Erro! Digite somente S ou N')
    if resp == 'N':
        break
print(galera)
print(f'{contpessoa} pessoas cadastradas!')
print(f'{round(medidade/contpessoa)} é a média das idades')
print('Mulheres na lista: ', end='')
for p in galera:
    if p['SEXO'] == 'F':
        print(f' {p["NOME"]}, ', end='')
media = medidade/contpessoa
print()
for p in galera:
    if p['IDADE'] > media:
        print(f'PESSOAS ACIMA DA MÉDIA: {p["NOME"]} ', end='')
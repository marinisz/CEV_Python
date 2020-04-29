nomes = []
tudo = []
resp = ''
pesao = 0
pesinho = 0
while True:
    nomes.append(str(input('NOME: ')).upper())
    nomes.append(int(input('PESO: ')))
    if len(tudo)==0:
        pesinho=pesado=nomes[1]
    else:
        if nomes[1] > pesao:
            pesao = nomes[1]
        if nomes[1] < pesinho:
            pesinho = nomes[1]
    tudo.append(nomes[:])
    nomes.clear()
    resp = str(input('CONTINUAR [S/N] >>>>>>>')).upper().strip()
    if resp == 'N':
        break
for p in tudo:
    if p[1] == pesao:
        print(f'{p[0]} é o pesadão')
    if p[1] == pesinho:
        print(f'{p[0]} é o levinho')
print(tudo)

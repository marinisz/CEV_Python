maior = 0
h = 0
menor = 0
resp = ''
while True:
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()
    resp = str(input('Deseja adicionar mais uma pessoa? [S/N]: ')).upper().strip()
    if idade > 18:
        maior +=1
    if sexo == 'M':
        h +=1
    if sexo =='F' and idade <20:
        menor +=1
    if resp == 'N':
        break
print('a)Mostre quantos são maiores de 18')
print('b)Quantos homens foram cadastrados?')
print('c)Quantas mulheres com menos de 20 anos foram cadastradas?')
print(f'a){maior}. b){h}. c){menor}')
from random import randint
lista = list()
jogos = list()
quant = int(input('Digite o número de palpites que deseja: '))
tot = 0
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
for c in range(1,quant+1):
    print(f'O {c}º jogo é: {jogos[c]}\n', end='')
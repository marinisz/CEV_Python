import time
def contador(inicio, fim, passo):
    print(f'Contando de {inicio} até {fim} de {passo} à {passo}')

    if inicio <= fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            time.sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            time.sleep(0.5)
            cont -= passo
contador(1,10,1)
print()
contador(10,0,2)
print()
a = int(input('Digite o início da contagem: '))
b = int(input('Digite o fim da contagem: '))
c = int(input('Digite o passo da contagem: '))
contador(a, b, c)

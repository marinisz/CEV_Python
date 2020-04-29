lista = []
menor = 0
maior = 0
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos +=1
print(lista)

# n = int(input('Digite um valor: '))
        # lista.append(n)
        # if n == lista[0]:
        #     n = menor = maior
        # else:
        #     if n < menor:
        #         n = menor
        #     if n > maior:
        #         n = maior
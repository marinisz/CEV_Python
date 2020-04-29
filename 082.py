num = list()
pares = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('[S/N]')).upper()
    if resp == 'N':
        break
z = len(num)
for c, v in enumerate(num):
    if v%2 != 0:
        impar.append(v)
    elif v%2 == 0:
        pares.append(v)
print(num)
print(impar)
print(pares)

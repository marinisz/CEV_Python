x = str(input('Digite uma frase qualquer: ')).strip().upper()
y = x.split()
z = ''.join(y)
inverso = ''
for letra in range(len(z) -1, -1, -1):
    inverso += z[letra]
print(inverso)
if inverso == z:
    print('É um palindromo!')
else:
    print('Não é')



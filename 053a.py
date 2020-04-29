x = str(input('Digite uma frase qualquer: ')).strip().upper()
y = x.split()
z = ''.join(y)
inverso = z[::-1]
print(inverso)
if inverso == z:
    print('É um palindromo!')
else:
    print('Não é')
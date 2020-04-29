frase = str(input('Digite qualquer frase: ')).strip().upper().split()
frase1 = ''.join(frase)
inverso = frase1[::-1]
if frase1 == inverso:
    print('É um palindromo!')
else:
    print('Não é')
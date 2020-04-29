a = float(input('Digite sua primeira nota: '))
b = float(input('Digite sua segunda nota: '))
media = (a+b)/2
print('A sua média é: {}!'.format(media))
print('-=-'*9)
if media < 5.0:
    print('\033[31mVOCÊ FOI REPROVADO!')
elif 5.0 <= media < 6.9:
    print('\033[35mVOCÊ ESTÁ DE RECUPERAÇÃO!')
else:
    print('\033[34mVOCÊ FOI APROVADO!')
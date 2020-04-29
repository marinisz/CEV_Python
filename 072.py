num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
resp = ''
while resp != 'N':
    n = int(input('Digite um número de 1 à 20: '))
    if n > 20:
        break
    print(f'O número digitado é o {num[n]}')
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()
print('\033[31m------FIM DO PROGRAMA------\033[m')
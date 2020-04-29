valor = int(input('Digite o valor à ser sacado: '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'O total de cédulas de R${céd},00 é {totcéd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd =1
        totcéd = 0
        if total == 0:
            break


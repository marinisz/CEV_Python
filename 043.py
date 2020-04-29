peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura em cm?'))
imc = peso/((altura*altura)/10000)
print(round(imc))
if imc <= 18.5:
    print('\033[33mVocê está abaixo do peso!\033[m')
elif 18.5 < imc <= 25:
    print('\033[34mVocê está no peso ideal!\033[m')
elif 25 < imc < 40:
    print('\033[31mVocê está acima do peso (OBESIDADE)!\033[m')
else:
    print(print('\033[31mVocê está muito acima do peso (OBESIDADE MÓRBIDA)!\033[m'))
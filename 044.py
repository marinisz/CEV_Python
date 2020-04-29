import playsound
valor = float(input('Digite o valor do produto: '))
print('O valor à vista no dinheiro ou débito, com 10% de desconto é: \033[31m{}\033[m'.format(valor-(valor*0.1)))
print('O valor no cartão de crédito, com 5% de desconto é: \033[31m{}\033[m'.format(valor-(valor*0.05)))
print('O valor em até 2x no cartão é: \033[31m{}\033[m'.format(valor))
print('O valor 3x ou mais no cartão, com 20% de juros é: \033[31m{}\033[m'.format(valor+(valor*0.2)))
playsound.playsound('jovem.mp3')


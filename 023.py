n= str(input('Digite um número de até 04 algarismos: ')).strip()
print('Seu número é {}'.format(n))
unidade = n[3]
dezena = n[2]
centena = n[1]
milhar = n[0]

print('Na casa das unidades temos {}.'.format(unidade))
print('Na casa das dezenas temos {}.'.format(dezena))
print('Na casa das centenas temos {}.'.format(centena))
print('Na casa das unidades de milhar temos {}.'.format(milhar))

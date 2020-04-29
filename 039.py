ano = int(input('\033[34mDigite o ano de seu nascimento jovem: \033[m'))
x = 2019
if ano > 2001:
    print('\033[36mVocê deve se alistar em {}.'.format(x+(18-(x-ano))))
elif ano < 2001:
    print('\033[31mVocê deveria ter se alistado em {}.'.format(ano+18))
else:
    print('\033[34mVocê deve se alistar esse ano!')

print('\033[34mBem-vindo ao sistema de crédito!\033[m')
print('-=-'*11)
salario = int(input('\033[34mQual o eu salário? \033[m'))
print('-=-'*11)
casa = int(input('\033[34mQual o valor da casa que pretende comprar (meses)? \033[m'))
print('-=-'*11)
tempo = int(input('\033[34mEm quanto tempo você pretende pagar a casa? \033[m'))
presta = casa/tempo
x = presta*0.3
if salario <= x:
    print('\033[31mInfelizmente não podemos aprovar o seu crédito!\033[m')
else:
    print('\033[36mSeu crédito foi aprovado, favor se dirigir ao próximo guichê\033[m')


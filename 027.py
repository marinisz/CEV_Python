n= str(input('Digite seu nome completo: '))
print('Seu nome é {}'.format(n.title()))
x = n.split()
print('Seu primeiro nome é {}'.format(x[0].title()))
print('Seu ultimo nome é {}'.format(x[len(x)-1].title()))
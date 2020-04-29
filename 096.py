def lin():
    print('*='*15)
def area(larg, comp):
    a = larg * comp
    print(f'A área de {larg} * {comp} é = {a}m²!')

lin()
l = float(input('Digite a largura do terreno: '))
lin()
c = float(input('Digite o comprimento: '))
lin()
area(l,c)

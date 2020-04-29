velo = int(input('Qual a velocidade dessa nave: '))
if velo >= 80:
    print('Troxa, vai pagar {} de multa!'.format((velo-80)*7))
else:
    print('ta mec')
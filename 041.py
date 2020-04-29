idade = int(input('Digite sua idade atleta: '))
if idade <= 9:
    print('Você é um alteta da categoria MIRIM.')
elif 9 < idade <= 14:
    print('Você é um alteta da categoria INFANTIL')
elif 14 < idade <= 19:
    print('Você é um alteta da categoria JÚNIOR')
elif 19 < idade <= 20:
    print('Você é um alteta da categoria SÊNIOR')
else:
    print('Você é um alteta da categoria MASTER')
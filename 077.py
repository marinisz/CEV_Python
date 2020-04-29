a = ('abacate', 'amor', 'cachorro', 'feijao', 'neymar')
for palavra in a:
  print(f'\nNa palavra {palavra.upper()} temos ', end='')
  for vogal in palavra:
      if vogal.lower() in 'aeiou':
          print(vogal, end='')


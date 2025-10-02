nascimento = int(input('Qual ano o atleta nasceu?: '))
idade= 2025-nascimento
if (idade<=9):
  print(f'Mirim')
elif (9<idade<=14):
  print(f'Infantil')
elif (14<idade<=19):
  print(f'Junior')
elif (19<idade<=20):
  print(f'Sênior')
else:
  print(f'Master')
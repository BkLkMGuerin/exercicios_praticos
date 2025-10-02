num = int(input('Qual número você quer converter?:'))
print('''Escolha qual opção para conversão:
      [ 1 ] Binário
      [ 2 ] Octal
      [ 3 ] Hexadecimal''')
opt = int(input('Qual opção: \n'))
if opt == 1:
  num = bin(num)
  print(num)
elif opt == 2:
  num = oct(num)
  print(num)
elif opt == 3:
  num = hex(num)
  print(num)
else:
  print('Opção inválida')
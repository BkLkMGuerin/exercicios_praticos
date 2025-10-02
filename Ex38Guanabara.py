num1 = int(input('Qual o primeiro número será comparado?: '))
num2 = int(input('Qual o segundo número a ser comparado?: '))
if (num1>num2):
  print(f'O número {num1} é maior')
elif (num2>num1):
  print(f'O número {num2} é maior')
elif (num1==num2):
  print(f'Os dois números são iguais')
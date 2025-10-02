valor = int(input('Qual o valor da casa:\n'))
salario = int(input('Qual o seu salário:\n'))
parcelas = int(input('Quantas parcelas serão feitas?:\n'))
valor_parcelas = valor/parcelas
limite_salario = salario*0.3
if (valor_parcelas<limite_salario):
  print(f'Parabéns! Seu empréstimo foi aprovado no valor de {valor_parcelas}')
else:
  print(f'Infelizmente seu empréstimo no valor de {valor_parcelas} foi negado pois o limite disponivel seria de {limite_salario} ')

preco = float(input('Qual o preço do produto: '))
print('''Escolha a forma de pagamento:
      [ 1 ] Dinheiro/Cheque
      [ 2 ] Cartão(Á vista)
      [ 3 ] 2x Cartão 
      [ 4 ] 3x ou + Cartão''')
fpagamento = int(input('Qual opção: \n'))
if fpagamento == 1:
  print(f'O valor do pagamento será R${preco-0.1*preco}')
elif fpagamento == 2:
  print(f'O valor do pagamento será R${preco-0.05*preco}')
elif fpagamento == 3:
  print(f'O valor fo pagamento será R${preco}')
elif fpagamento == 4:
  print(f'O valor do pagamento será R${preco+preco*0.2} com parcelas de no mínimo R${(preco+preco*0.2)/3}')
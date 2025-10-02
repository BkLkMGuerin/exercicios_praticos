import random
print(''' Bem-Vindo ao JOKENPÔ! 
      Escolha a opção para jogar:
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura''')
lista=['Pedra','Papel','Tesoura']
comp = random.choice(lista)
player = int(input('Qual a sua escolha: '))
escolha_player = lista[player]
if comp==lista[0]: #PEDRA
  if escolha_player==lista[0]:
    print('Empate!')
  elif escolha_player==lista[1]:
    print('Jogador ganhou!')
  elif escolha_player==lista[2]:
    print('Jogador perdeu!')
  else:
    print('Jogada Invâlida')
elif comp==lista[1]: #PAPEL
  if escolha_player==lista[0]:
    print('Jogador perdeu!')
  elif escolha_player==lista[1]:
    print('Empate!')
  elif escolha_player==lista[2]:
    print('Jogador ganhou!')
  else:
    print('Jogada Invâlida')
elif comp==lista[2]: #TESOURA
  if escolha_player==lista[0]:
    print('Jogador ganhou!')
  elif escolha_player==lista[1]:
    print('Jogador perdeu!')
  elif escolha_player==lista[2]:
    print('Empate!')
  else:
    print('Jogada Invâlida')
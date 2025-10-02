print('-===--=-'*3)
print('OS 10 TERMOS DE UMA PA')
print('-===--=-'*3)
pt = int(input('Qual será o primeiro termo: '))
razao = int(input('Qual será a razão: '))
decimo = pt + (10-1) * razao
for i in range(pt,decimo,razao):
  print(f'[{i}]', end='==>')
  

num = int(input('Qual número você quer a tabuada?: '))
mult=0
for i in range(1,10+1):
  print(f'{i} x {num} = {num*i}')
  i+=1
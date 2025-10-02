num = int(input('Qual número quer saber se é primo: '))
tot= 0
for i in range(1,num+1):
  if num%i==0:
    tot+=1
print(f' o numero {num} foi divisivel {tot} vezes')
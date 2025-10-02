soma= 0 
for i in range(0,6):
  nums= int(input('Qual número: '))
  if nums%2==0:
    soma += nums
print(f' A soma dos pares foi de {soma}')
menor= 0
maior= 0
for i in range(1,7+1):
  idade = int(input('Qual ano você nasceu?: '))
  if 2025-idade>=18:
    maior+=1
  else:
    menor+=1
print(f'Temos {maior} pessoas maior de idade, e {menor} pessoas menor de idade')
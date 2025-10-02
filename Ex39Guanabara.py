ano = int(input('Que ano você nasceu?: '))
idade = 2025-ano
if (idade<18):
  print(f'Você ainda tem mais {18-idade} anos para se alistar')
elif(idade==18):
  print(f'Está na hora de se alistar!')
else:
  print(f'Você está atrasado em {idade-18} anos para seu alistamento')
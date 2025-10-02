r1 = float(input('Digite o primeiro segmento: \n'))
r2 = float(input('Digite o segundo segmento: \n'))
r3 = float(input('Digite o terceiro segmento: \n'))
if (r1<r2+r3 and r2<r1+r3 and r3<r1+r2):
  print('É possivel criar um triângulo')
  if (r1==r2==r3):
    print('É um triângulo Equilatero')
  elif(r1==r2 or r2==r3 or r1==r3):
    print('É um triângulo Isósceles')
  elif (r1!=r2!=r3):
    print('É um triângulo Escaleno')
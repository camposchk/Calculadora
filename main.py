import Murilo

print("Você deseja fazer uma Soma ou Subtração?")
print("\n1 - Somar \n2 - Subtrair\n")

resp = int(input("Digite qual vc deseja: "))

if resp == 1:
  print("Soma")
  a = int(input("Digite o 1° valor: "))
  b = int(input("Digite o 2° valor: "))

  soma = Murilo.soma(a, b)
  print(soma)

elif resp == 2:
  print("Subtração")
  a = int(input("Digite o 1° valor: "))
  b = int(input("Digite o 2° valor: "))

  sub = Murilo.sub(a, b)
  print(sub)
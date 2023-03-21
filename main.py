import Murilo

print("Você deseja fazer uma Soma ou Subtração?")
print("\n1 - Somar \n2 - Subtrair\n")
while True:
  try:
      resp = int(input("Digite qual vc deseja: "))
      if resp < 3 and resp > 0:
        break
  except ValueError:
    print("Valor Invalido!")
    print()


if resp == 1:
  print("Soma")
  while True:
    try:
      a = int(input("Digite o 1° valor: "))
      b = int(input("Digite o 2° valor: "))
      break
    except ValueError:
      print("Valor Invalido")

  soma = Murilo.soma(a, b)
  print(soma)

elif resp == 2:
  print("Subtração")
  while True:
    try:
        a = int(input("Digite o 1° valor: "))
        b = int(input("Digite o 2° valor: "))
        break
    except ValueError:
      print("Valor Invalido")
  sub = Murilo.sub(a, b)
  print(sub)
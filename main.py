import Juan

while True:
  try:
    a = int(input('Número 1: '))
    b = int(input('Número 2: '))
    break
  except ValueError:
    print('Valor inválido')
    print()

while True:
  try:
    print("1 Multiplicação | 2 Divisão")
    ops = int(input())
    if ops == 1:
      print(Juan.mult(a, b))
      break
    elif ops == 2:
      print(Juan.div(a, b))
      break
    else:
      raise ValueError()
  except ValueError:
    print('Valor inválido')
    print()
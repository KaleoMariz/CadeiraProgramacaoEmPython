def soma_de_dois_numeros (a, b): 
  return a + b

def subtracao_de_dois_numeros (a, b): 
  return a - b

def multiplicacao_de_dois_numeros (a, b): 
  return a * b

def divisao_de_dois_numeros (a, b): 
  return round(a / b, 2)

def potencia_de_dois_numeros (a, b): 
  return a ** b

def raiz_de_dois_numeros (a, b): 
  return round(a ** (1 / b), 5)

type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))
while type_character == 1:
  
  print ("Digite 1 para somar dois numeros")
  print ("Digite 2 para subtrair dois numeros")
  print ("Digite 3 para multiplicar dois numeros")
  print ("Digite 4 para dividir dois numeros")
  print ("Digite 5 para elever um número a outro")
  print ("Digite 6 para calcular a raiz de um número \n \n")

  opcao = int(input("Digite a opção desejada: \n "))

  if opcao == 1:
    print ("Soma \n")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: \n"))
    print ("O resultado da soma é: ", soma_de_dois_numeros(a, b))
    type_character = int(input("Digite 1 se quiser continuar a utilizar a calculadora: \n"))
    if type_character != 1: 
      print ("Obrigado! Volte sempre!")
      type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))

  elif opcao == 2:
    print ("Subtração \n")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: \n"))
    print ("O resultado da subtração é: ", subtracao_de_dois_numeros(a, b))
    type_character = int(input("Digite 1 se quiser continuar a utilizar a calculadora: \n"))
    if type_character != 1: 
      print ("Obrigado! Volte sempre!")
      type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))

  elif opcao == 3:
    print ("Multiplicação \n")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: \n"))
    print ("O resultado da multiplicação é: ", multiplicacao_de_dois_numeros(a, b))
    type_character = int(input("Digite 1 se quiser continuar a utilizar a calculadora: \n"))
    if type_character != 1: 
      print ("Obrigado! Volte sempre!")
      type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))

  elif opcao == 4:
    print ("Divisão \n")
    a = float(input("Digite o número a dividir: "))
    b = float(input("Digite por quando você quer dividi-lo: \n"))
    print ("O resultado da divisão é:", divisao_de_dois_numeros(a, b))
    type_character = int(input("Digite 1 se quiser continuar a utilizar a calculadora: \n"))
    if type_character != 1: 
      print ("Obrigado! Volte sempre!")
      type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))

  elif opcao == 5:
    print ("Potenciação \n")
    a = float(input("Digite a base da potência: "))
    b = float(input("Digite o expoente da potência: \n"))
    print ("O resultado da potência é: ", potencia_de_dois_numeros(a, b)) 
    type_character = int(input("Digite 1 se quiser continuar a utilizar a calculadora: \n"))
    if type_character != 1: 
      print ("Obrigado! Volte sempre!")
      type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))

  elif opcao == 6:
    print ("Raiz quadrada, cúbica, ou qualqur grau \n")
    a = float(input("Digite o 'radicando' da raiz: "))
    b = float(input("Digite o índice da raíz: \n"))
    print ("O resultado da raiz é: ", raiz_de_dois_numeros(a, b))
    type_character = int(input("Digite 1 se quiser continuar a utilizar a calculadora: \n"))
    if type_character != 1: 
      print ("Obrigado! Volte sempre!")
      type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))

  else:
    print ("Não corresponde a nenhuma operação")
    type_character = int(input("Digite 1 se quiser continuar a utilizar a calculadora: \n"))
    if type_character != 1: 
      print ("Obrigado! Volte sempre!")
      type_character = int(input("Digite 1 se quiser utilizar a calculadora: \n"))
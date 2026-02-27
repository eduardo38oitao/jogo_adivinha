import random as rd

print ("*************************")
print ("Bem vindo ao adivinhe.py")
print ("*************************")

chute=int(input("Digite seu número:"))


numero_secreto = rd.randrange(1, 100) 
numero_tentativa = 0
rodada = 1
pontos = 1000


print("niveis de dificuldade")
print("\n(1) facil (2) medio (3) dificil (4)aleatorio\n")

nivel = int(input("escolha o nivel: "))

if(nivel == 1):
  numero_tentativa = 12
elif(nivel == 2): 
  numero_tentativa = 8
elif(nivel == 3):
    numero_tentativa = 4
else:
  numero_tentativa = rd.randrange(1,50)


#criando um lupin para tudo que tiver em baixo se repita
for numero_tentativa in range(1,numero_tentativa + 1) :
  print(f"tentativa {rodada} de {numero_tentativa}")
  entrada = int(input("digite um numero entre 1 a 100: "))
  acertou = entrada == numero_secreto
  chute_maior = entrada > numero_secreto
  chute_menor = entrada < numero_secreto

  if(entrada > 100 or entrada < 1):
    print("o valor digitado não é permitido")
  print(f"Você digitou {entrada}")

  #verificação de acerto/erro
  if(acertou):
    print("Você Acertou!")
    print(f"parabens (ou não)! voce fez {pontos} pontos.")
    break
  else:
   if(chute_maior):
      print("Você Errou! Seu número foi maior que o número secreto")
   if(chute_menor):
      print("Você Errou! Seu número foi menor que o número secreto")
  
  pontos_perdidos = abs(numero_secreto - entrada) #(80 - 40 = 40)
  pontos = pontos - pontos_perdidos
  rodada = rodada + 1

print("***********")
print("Fim de Jogo")
print("***********")
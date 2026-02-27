print ("*************************")
print ("Bem vindo ao loop")
print ("*************************")

chute = int(input("digite sua senha:"))
#variaveis
senha_correta = 1
senha_errada = 2

for senha in range(1,chute + 1) :

    if(chute > senha_correta or chute < senha_correta):

        print("SENHA ERRADA")
        print(f"tentativa de {chute}")
    
    acertou = senha_correta + chute
    if(acertou):
        print("|||||||| SENHA CERTA |||||||||| ")
        print("||||||||||||| VOCE ACERTOU |||||||||")
        break
    else:
        if(senha_errada):{
            
        }
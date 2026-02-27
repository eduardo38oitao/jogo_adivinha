senha_correta = 1
tentativas = 0


print("  SISTEMA DE ACESSO  ")


while True:
    # aumenta o contador de tentativa
    tentativas += 1
    
    # palpite do usuario
    chute = chute = int(input("digite sua senha:"))

    # verificação
    if chute == senha_correta:
        print(" SENHA CORRETA!")
        print(f"Acesso garantido após {tentativas} tentativa(s).")
        break # reseta o while
    else:
        print(" SENHA ERRADA!")
        print("Tente novamente...")

print("  FIM DO PROGRAMA")




#while deixa o loop infinito
while True : 
    comando = input("Digite a palavra sair ! ")

    if comando.lower() == 'sair':
        print("fim do programa")
        break
    
    if len(comando)<2 : 
        print("String muito pequena ")
        print("Tente digitar 'sair' para encerrar o programa")
        continue

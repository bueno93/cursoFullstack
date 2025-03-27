while True : 

    print("A lampada estava plugada? ")
    opcao = input("Responda com sim ou nao :  ")

    if opcao.lower() == "nao": 
        print ("plugar a lampada")
        break
        
    elif opcao.lower() == "sim":
        
        bulbo = input("O bulbo queimou ? " )
        if bulbo == "sim":
            print("Troque o bulbo")
            break
        else:
            print(" Compre uma lampada nova.")   
            break





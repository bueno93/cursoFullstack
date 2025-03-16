#Maior entre dois numeros

"""numero_1 = float(input("Digite um valor númerico : "))
numero_2 = float(input("Digite um valor númerico : "))

if numero_1 > numero_2 :
    print(str(numero_1) + " é maior que é " + str(numero_2))
elif numero_1 < numero_2 :
    print (str(numero_2) + " é maior que o " + str(numero_1))
else :
    print (str(numero_1) +  " e " + str(numero_2) + " são iguais. ")
    
    """

# verificação de genero
"""
genero = input("DIGITE SEU SEXO : M - MASCULINO | F - FEMININO : ")

if genero == "M" or genero == "m" : 
    print("Sexo masculino")

elif genero == "F" or genero == "f": 
    print("Sexo feminino")
else : 
    print("Sexo não identificado")
"""

# verficar idade para votação 

"""idade = int(input("Digite sua idade : "))

if idade >= 16 and idade <= 60:
    print("Pode votar.")
elif idade >= 60:
    print("voto opcional.")
else :
    print("Não pode votar.")
   """         



#verificação de login
"""def menu ():
    print(("Bem vindo"))
    opcao  = input("Escolha uma opcão : 1- login | 2 - sair : ")
menu()

def login ():
    usuario = "admin"
    senha = 1993

usuario = input("Digite seu usuario:  ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "1993" :
    print("Acesso Permitido ")
else : 
    print("Usuario nao encontrado. Digite corretamente seus dados.")
    opcao = menu()
    if opcao == "1" :
       login()
    else :
       print("Saindo do programa. ")
       """
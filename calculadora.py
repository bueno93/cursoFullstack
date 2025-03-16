 

print ("Bem vindo a calculadora digital")
print ("1- SOMAR")
print ("2 - SUBTRAIR")
print ("3 - MULTIPLICAR")
print ("4 - DIVIDIR")
menu = (input ("Digite sua opção : "))
num1  = int(input("Digite seu primeiro valor :  "))
num2 = int(input ("Digite seu segundo valor : " ))

if menu == "1" : 
 resultado = num1 + num2
 print("SOMA IGUAL A : ", resultado)

elif menu == "2" : 
 resultado = num1 - num2
 print ("SUBTRAÇÃO IGUAL A : ", resultado)
 
elif menu == "3" : 
 resultado = num1 * num2
 print ("MULTIPLICAÇÃO  IGUAL A : ", resultado)

elif menu == "4" : 
 resultado = num1 / num2
 print ("DIVISÃO IGUAL A : ", resultado)

else : 
 print ("Digite uma opção válida")

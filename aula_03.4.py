print ("Bem vindo a calculadora digital")
print (" +  SOMAR")
print (" - SUBTRAIR")
print (" *  MULTIPLICAR")
print (" /  DIVIDIR")
num1  = float(input("Digite seu primeiro valor :  "))
operacao = (input ("Digite sua opção : "))
num2 = float(input ("Digite seu segundo valor : " ))
resultado = 0

if operacao == "+" : 
 resultado = num1 + num2
 print("SOMA IGUAL A : ", str(resultado))

elif operacao == "-" : 
 resultado = num1 - num2
 print ("SUBTRAÇÃO IGUAL A : ", str(resultado))
 
elif operacao == "*" : 
 resultado = num1 * num2
 print ("MULTIPLICAÇÃO  IGUAL A : ", str(resultado))

elif operacao == "/" : 
 resultado = num1 / num2
 print ("DIVISÃO IGUAL A : ", str(resultado))

else : 
 print ("operação inválida : ")
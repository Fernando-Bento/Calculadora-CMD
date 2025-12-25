from funcoes import operacoes
from registro import registrar


print("--------------------- CALCULADORA ---------------------")
print("")
while True:

    try:
        n1 = float(input("Primeiro numero: "))
        n2 = float(input("Segundo numero: "))
        break
    except:
        print("Numero Inválido, favor digite outro!")

while True:

    try:
        operacao = int(input("Operacoes:\n\nEscolha qual operacao será realizada:\n1 - soma \n2 - subtracao\n3 - multiplicacao\n4 - divisao\n5 - exponenciacao\n\nQual operacao será realizada: "))
        if operacao > 5:
            print("Numero inválido! Digite outro.")
            continue
        break
    except:
        print("Numero inválido!")

resultado = operacoes(n1,n2,operacao)

print(f"Resultado:\n {resultado}")

registrar(n1,n2,operacao,resultado)
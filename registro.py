from datetime import datetime

def registrar(n1,n2,operacao,resultado):
    agora = datetime.now()

    operadores = {
    1: "+",
    2: "-",
    3: "*",
    4: "/",
    5: "^"
    }

    with open("historico.txt",'a', encoding="utf-8") as arquivo:
        arquivo.write(f"({agora.hour}:{agora.minute}:{agora.second}) - {n1} {operadores[operacao]} {n2} = {resultado}\n")

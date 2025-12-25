def operacoes(n1,n2,operacao):
    match operacao:
        case 1:
            return n1 + n2
        case 2:
            return n1 - n2
        case 3:
            return n1 * n2
        case 4:
            if n2 == 0:
                return "Divisão por zero"
            return n1 / n2
        case 5:
            return n1 ** n2
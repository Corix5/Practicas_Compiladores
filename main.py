
def tipo(token):
    if token == '+' or token == '-':
        t_token = "Operador"
    elif token.isdigit():
        t_token = "Numero Entero"
    else:
        t_token = "Identificador"
    return t_token

def analizar(op):
    tokens = [None] * len(op)
    for i in range(len(op)):
        tokens[i] = [None] * 2
    # Tokens = [token], [tipo de Token]
    str(tokens)
    i = 0

    # Elimina los espacios
    op.strip()
    tam = 0
    while i < len(op):
        j = i

        while j < len(op):
            if op[j] == '+'or op[j] == '-':
                break
            j += 1

        if i == j:
            tok = op[i]
            i += 1
        else:
            tok = op[i:j]
            i = j

        encontrado = False

        # Creo que se puede mejorar
        if tam != 0:
            for index in range(tam):
                if tokens[index][0] == tok:
                    encontrado = True
                    break
        else:
            tokens[tam][0] = tok
            tokens[tam][1] = tipo(tok)
            tam += 1
            encontrado = True

        if not encontrado:
            tokens[tam][0] = tok
            tokens[tam][1] = tipo(tok)
            tam += 1

    for i in range(tam):
        print(str(tokens[i][0]) + "\t\t\t" + str(tokens[i][1]))
    return tokens


op = input("Ingrese la operacion: \n")
tokens = analizar(op)
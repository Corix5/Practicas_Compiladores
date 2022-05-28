
termSymbols = ["id", "+", "*", "(", ")", "$"]
nonTermSymbols = ["E", "E'", "T", "T'", "F"]

queuSymbols = []

# Tabla de LL(1)
# Nota: La letra 'e' representa a epsilon
tableLL1 = [["TE'", "", "", "TE'", "", ""],
            ["", "+TE'", "", "", "e", "e"],
            ["FT'", "", "", "FT'", "", ""],
            ["", "e", "*FT'", "", "e", "e"],
            ["id", "", "", "(E)", "", ""]]

mainChar = str(input("\n Ingrese la cadena: "))

charInput = []
i = 0
j = 0

# Se ingresa la cadena de entrada a una pila
while i < len(mainChar):
    j = i
    # Se ejecuta el ciclo while por los simbolos terminales de 2 o mas letras
    while not (mainChar[j:i] in termSymbols):
        i += 1
    charInput.append(mainChar[j:i])

# Se agrega $ a la cadena de entrada
charInput.append("$")

# Se agrega $E a la pila de simbolos
queuSymbols.append("$")
queuSymbols.append(nonTermSymbols[0])

# ============ Algoritmo analisis sintactico LL(1) ==============
i = 0
while queuSymbols:

    x = queuSymbols[-1]
    a = charInput[i]

    if x in termSymbols:
        if x == a:
            queuSymbols.pop()
            i += 1
            print(x)
        else:
            print("La cadena ingresada no fue aceptada...")
            exit()
    else:
        # prod Es lo que se produce en la tabla
        prod = tableLL1[nonTermSymbols.index(x)][termSymbols.index(a)]
        chAux = ""
        if prod:
            queuSymbols.pop()
            k = -1
            # El ciclo while analiza lo que produce la tabla y lo ingresa
            # a la pila de derecha a izquierda
            while (-k) != (len(prod)+1):
                if prod[k] == "'" or prod[k] == "d":
                    # Si encuentra un ' o una 'd' quiere decir
                    # que e el simbolo es de dos letras, se añaden a la pila juntas
                    chAux = prod[k-1] + prod[k]
                    k -= 2
                    queuSymbols.append(chAux)
                elif prod[k] == "e":
                    # Si produce epsilon no agregamos nada
                    k -= 1
                else:
                    # Si el simbolo es de una sola letra solo se añade dicha letra
                    chAux = prod[k]
                    k -= 1
                    queuSymbols.append(chAux)

        else:
            print("\n La cadena ingresada no fue aceptada...")
            exit()
        print(x + "->" + prod)

print("\n ****** La cadena " + mainChar + " fue aceptada!! ******")

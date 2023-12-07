## num
numero = int(input("Numero desejado: "))

ultimo_numero = 1
penultimo_numero = 0
aux = 0
resultado = 0

if numero == 0: 
    resultado = 1

while ultimo_numero <= numero:
    aux = ultimo_numero + penultimo_numero
    penultimo_numero = ultimo_numero
    ultimo_numero = aux

    if ultimo_numero == numero:
        resultado = 1

if resultado == 1:
    print("O numero pertence a sequencia")
else:
    print("O numero não pertence a sequencia")


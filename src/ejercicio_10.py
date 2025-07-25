sumar_palabras= 0
palabra=""
while palabra.lower() != "fin":
    palabra = input("Ingresa una palabra: ")
    if palabra.lower() != "fin":
        sumar_palabras += 1

print(f"la suma de las palabras es: {sumar_palabras} ")
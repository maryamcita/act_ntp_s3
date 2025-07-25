numeroUsuario = int(input("Ingrese el numero para calcular factorial: "))
factorial=1
contador=1
while contador<=numeroUsuario:
    factorial*=contador
    contador+=1
    print(f"El factorial de {numeroUsuario} es: {factorial}")
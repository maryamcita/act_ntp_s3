suma_total = 0
print("Ingresa números para sumarlos. Escribe 0 para terminar.")
while True:
    numero= int(input("Ingresa un número: "))
    if numero == 0:
        break 
    suma_total += numero 
print(f"La suma total de los números ingresados es: {suma_total}")
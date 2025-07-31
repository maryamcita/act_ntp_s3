frase = "programacion es divertida"
vocales = "aeiou"
contador = 0

for letra in frase:
  if letra.lower() in vocales:
    contador += 1

print(f"La cantidad de vocales de la frase es: {contador}")
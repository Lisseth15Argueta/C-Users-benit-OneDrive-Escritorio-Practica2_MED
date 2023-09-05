serie_numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]

pares = []
impares = []

for numero in serie_numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Serie:", serie_numeros)
print("Números pares:", pares)
print("Números impares:", impares)

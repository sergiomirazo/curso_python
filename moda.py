from collections import Counter
resp = True
lista = []

while resp:
    elemento = input("Ingresa el elemento: ")
    if elemento=='parar':
        resp = False
    else:
        lista.append(elemento)

def moda(array):
    contador = Counter(array)
    elemento, repeticiones = contador.most_common(1)[0]
    return elemento

elemento_repetido = moda(lista)
print("El elemento más repetido es: ", elemento_repetido)

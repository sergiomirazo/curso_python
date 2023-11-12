resp = True
#El siguiente ciclo es un while, ejecuta codigo mientras una variable
#sea verdadera
lista = []
suma = 0
while resp:
    respuesta = input("Quieres ingresar un número?: ")
    if respuesta=='si':
        numero = float(input("Ingresa un número: "))
        lista.append(numero)
    else:
        resp=False

#Calcular el promedio de los elementos dentro de una lista
for i in range(len(lista)):
    suma += lista[i]

promedio = round(suma/len(lista), 2)
print(f"El promedio es: {promedio}")

promedio = sum(lista)/len(lista)
print(promedio)


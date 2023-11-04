import matplotlib.pyplot as plt

# Leer los datos del archivo
with open('data1.txt', 'r') as file:
    data = file.readlines()

# Extraer las coordenadas x e y de los datos
x = []
y = []
for line in data:
    x_value, y_value = line.strip().split(',')
    x.append(float(x_value))
    y.append(float(y_value))

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los datos
ax.plot(x, y)

# Agregar título y etiquetas de los ejes
ax.set_title('Respuesta del campo eléctrico de un cristal de cuarzo respecto a la frecuencia')
ax.set_ylabel('E [V/m]')
ax.set_xlabel('f [Hz]')

# Ajustar los límites de los ejes
ax.set_xlim(4E14, 4E15)
ax.set_ylim(0, 0.1)

# Mostrar el gráfico
plt.show()

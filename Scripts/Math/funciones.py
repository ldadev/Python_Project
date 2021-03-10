from matplotlib import pyplot

entrada = input('Ingrese la función>>')

# Valores del eje X que toma el gráfico.
x = range(-1000, 1000)
# Graficar la funciones.
pyplot.plot(x,list(map(lambda x:eval(entrada),x)))

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-100, 100)
pyplot.ylim(-100, 100)
# Guardar gráfico como imágen PNG.
pyplot.savefig("función.png")
# Mostrarlo.
pyplot.show()


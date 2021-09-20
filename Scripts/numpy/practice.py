import matplotlib.pyplot as plt
import numpy as  np

x = np.arange(1,11)
y = [-7.4,-2.3,3,7.6,12,17.9,22.5,27.6,32.1,37.4]
plt.plot(x,y,'histograma')
plt.xlabel('Voltaje')
plt.ylabel('Corriente')
plt.title('Resultados Graficados')
plt.show()


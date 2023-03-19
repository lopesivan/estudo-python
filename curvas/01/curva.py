import numpy as np
import matplotlib.pyplot as plt

# Definindo as funções paramétricas
t = np.linspace(0, 2*np.pi, 200)
x = np.sin(3*t)
y = np.cos(2*t)

# Plotando a curva
plt.plot(x, y)

# Configurando o gráfico
plt.axis('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curva de Lissajous')

# Exibindo o gráfico
plt.show()

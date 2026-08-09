import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

x = np.linspace(-5, 5, 25)
y = np.linspace(-8, 8, 25)

X, Y = np.meshgrid(x, y)

M = f(X, Y)

U = np.ones_like(M)
V = M

L = np.sqrt(U**2 + V**2)
U = U / L
V = V / L

plt.figure(figsize=(14, 8))

plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1.5)

xx = np.linspace(-5, 5, 500)

# Solución particular: y = e^(x+2) - x - 1
yy = np.exp(xx + 2) - xx - 1

plt.plot(xx, yy, linewidth=2.5, label='Solución y(-2)=2')

plt.scatter(-2, 2, color='red', s=60, zorder=5)
plt.text(-1.8, 2.3, '(-2,2)', fontsize=12)

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlim(-5, 5)
plt.ylim(-8, 8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Campo de pendientes: y' = x + y")
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (6*x - 3*x*y) / (x**2 + 1)

x = np.linspace(-5, 5, 25)
y = np.linspace(-3, 7, 25)

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

# Solución particular: y = 2 - 1/(x²+1)^(3/2)
yy = 2 - 1 / (xx**2 + 1)**(3/2)

plt.plot(xx, yy, linewidth=2.5, label='Solución y(0)=1')

plt.scatter(0, 1, color='red', s=60, zorder=5)
plt.text(0.2, 1.2, '(0,1)', fontsize=12)

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlim(-5, 5)
plt.ylim(-3, 7)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Campo de pendientes: (x²+1)y' + 3xy = 6x")
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()

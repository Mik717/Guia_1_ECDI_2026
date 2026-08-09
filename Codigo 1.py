import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return -y - np.sin(x)

x = np.linspace(-5, 15, 25)
y = np.linspace(-6, 8, 20)

X, Y = np.meshgrid(x, y)

M = f(X, Y)

U = np.ones_like(M)
V = M

L = np.sqrt(U**2 + V**2)
U = U / L
V = V / L

plt.figure(figsize=(14, 8))

plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1.5)

xx = np.linspace(-5, 15, 500)

yy = (
    0.5 * np.exp(-xx)
    + 0.5 * np.cos(xx)
    - 0.5 * np.sin(xx)
)

plt.plot(xx, yy, linewidth=2.5, label='Solución y(0)=1')

plt.scatter(0, 1, color='red', s=60, zorder=5)
plt.text(0.2, 1.2, '(0,1)', fontsize=12)

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlim(-5, 15)
plt.ylim(-6, 8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Campo de pendientes: y' = -y - sin(x)")
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()

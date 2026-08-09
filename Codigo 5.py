import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * np.exp(y)

x = np.linspace(-3, 3, 25)
y = np.linspace(-4, 3, 25)

X, Y = np.meshgrid(x, y)

M = f(X, Y)

U = np.ones_like(M)
V = M

L = np.sqrt(U**2 + V**2)
U = U / L
V = V / L

plt.figure(figsize=(14, 8))

plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1.5)

xx = np.linspace(-1.35, 1.35, 500)

# Solución particular: y = -ln(1 - x²/2)
yy = -np.log(1 - xx**2 / 2)

plt.plot(xx, yy, linewidth=2.5, label='Solución y(0)=0')

plt.scatter(0, 0, color='red', s=60, zorder=5)
plt.text(0.1, 0.2, '(0,0)', fontsize=12)

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlim(-3, 3)
plt.ylim(-4, 3)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Campo de pendientes: y' = xeʸ")
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()

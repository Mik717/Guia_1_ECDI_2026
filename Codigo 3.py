import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(x, y):
    return -x**2 + np.sin(y)

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

# Condición escogida: y(0)=1
sol = solve_ivp(f, [-5, 5], [1], dense_output=True, max_step=0.02)

xx = np.linspace(-5, 5, 500)
yy = sol.sol(xx)[0]

plt.plot(xx, yy, linewidth=2.5, label='Solución y(0)=1')

plt.scatter(0, 1, color='red', s=60, zorder=5)
plt.text(0.2, 1.2, '(0,1)', fontsize=12)

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlim(-5, 5)
plt.ylim(-8, 8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Campo de pendientes: y' = -x² + sin(y)")
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()

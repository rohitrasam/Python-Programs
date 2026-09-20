import matplotlib.animation  as anim
import matplotlib.pyplot as plt
import numpy as np


deg_3 = lambda x: x**3
deg_13 = lambda x: np.exp(x)
# deg_2 = lambda x: 3*x**2
# deg_1 = lambda x: deg_3(x) / deg_2(x)
# f = lambda x: x**3 - 8*x**2 + 17*x +4
# df = lambda x: 3*x**2 - 16*x + 17 
# ddf = lambda x: 6*x - 16
circ = lambda x, y: x**2 + y**2 - 2

a = np.linspace(-2, 2, 1000)

fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(1, 1, 1)
fig.set_facecolor("black")
ax.set_facecolor("black")
ax.grid(color="white", alpha=0.4)
lin_3, = ax.plot(deg_3(a), label="3 deg")
lin_13, = ax.plot(deg_13(a), label="1/3 deg")
# cos, = ax.plot(np.cos(np.pi*a/180), "--", label="cos",)
# sin, = ax.plot(np.sin(a*np.pi/180), label='sin')
# c,  = ax.plot(circ(a, a))
ax.set_xlim(-10, 10) # plt.xlim
ax.set_ylim(-15, 15)
ax.set_xlabel("Deg")
ax.legend()

def animate(frames):
    print(frames)
    mask = a <= frames
    lin_3.set_data(a[mask], deg_3(a[mask]))
    lin_13.set_data(a[mask], deg_13(a[mask]))
    # cos.set_data((a[mask], np.cos(a[mask]*np.pi/180)))
    # sin.set_data((a[mask], np.sin(a[mask]*np.pi/180)))
    # c.set_data(a[mask], circ(a[mask], a[mask]))

lin_anim = anim.FuncAnimation(fig, animate, a[::10], interval=20)
lin_anim.save("2_deg.mp4")
plt.close()

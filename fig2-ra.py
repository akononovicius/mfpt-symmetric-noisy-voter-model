import matplotlib.pyplot as plt
import numpy as np

from theory.ra import *

show_grid = True

low_reflecting = 0.03
high_absorbing = 0.63
x_0_ticks = np.linspace(low_reflecting, high_absorbing, 4)
fixed_x0 = 0.23

fig = plt.figure(figsize=(6, 2.67))

for idx, epsi in enumerate([0, 0.5, 1, 1.5, 2, 2.5]):
    data = np.loadtxt(f"data/ra-epsi{10 * epsi:.0f}.csv", delimiter=",", dtype=float)
    if data[-1, 0] > 1:
        data[-1, 0] = data[-1, 0] / 1e3
    theory_x = np.linspace(low_reflecting, high_absorbing)
    theory_y = globals()[f"theory_epsi{10 * epsi:.0f}"](
        theory_x, low_reflecting, high_absorbing
    )

    plt.subplot(231 + idx)
    plt.grid(show_grid)
    plt.title(rf"$\varepsilon={epsi:.1f}$", fontsize=8)
    plt.xticks(x_0_ticks)
    if idx < 3:
        plt.xlabel("")
        plt.gca().set_xticklabels([])
    else:
        plt.xlabel(r"$x_0$")
    plt.ylim([-0.075, 1.75])
    plt.yticks([0, 0.5, 1.0, 1.5])
    if idx % 3 == 0:
        plt.ylabel(r"$\overline{T}$")
    else:
        plt.ylabel("")
        plt.gca().set_yticklabels([])
    plt.text(
        0.97,
        0.9,
        f"({chr(ord('a') + idx)})",
        horizontalalignment="right",
        verticalalignment="center",
        transform=plt.gca().transAxes,
    )
    plt.plot(theory_x, theory_y, "k")
    plt.plot(data[:, 0], data[:, 1], "rs")

plt.tight_layout()
plt.savefig("figs/fig2-ra.pdf", format="pdf")
plt.close()

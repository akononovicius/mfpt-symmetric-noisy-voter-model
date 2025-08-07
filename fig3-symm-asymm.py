import re

import matplotlib.pyplot as plt
import numpy as np

show_grid = False
show_legend = False
show_titles = False

epsis = [0, 0.8, 1.6, 2.4, 3.2, 4.0]

y_lims = [-0.03, 0.43]
y_step = 0.1
y_ticks = np.arange(0, y_lims[1], y_step)

fig = plt.figure(figsize=(6, 2))

# MFPT curves for the symmetric case
plt.subplot(121)
if show_titles:
    plt.title(r"$L=0.2$, $H=0.8$")
plt.grid(show_grid)
plt.ylim(y_lims)
plt.yticks(y_ticks)
plt.ylabel(r"$\overline{T}$")
plt.xlim([0.17, 0.83])
plt.xticks(np.arange(0.2, 0.83, 0.1))
plt.xlabel(r"$x_0$")

for epsi in epsis:
    data = np.loadtxt(f"data/x0-symm-epsi{epsi*10:.0f}.csv", delimiter=",")
    plt.plot(data[:, 0], data[:, 1], label=rf"$\varepsilon={epsi:.1f}$")

plt.text(
    0.97,
    0.92,
    "(a)",
    horizontalalignment="right",
    verticalalignment="center",
    transform=plt.gca().transAxes,
)

if show_legend:
    plt.legend(loc=0, ncols=2, fontsize="small").get_frame().set_linewidth(0.4)

# MFPT curves for the asymmetric case
plt.subplot(122)
if show_titles:
    plt.title(r"$L=0.1$, $H=0.7$")
plt.grid(show_grid)
plt.ylim(y_lims)
plt.yticks(y_ticks)
plt.ylabel("")
plt.gca().set_yticklabels([])
plt.xlim([0.07, 0.73])
plt.xticks(np.arange(0.1, 0.73, 0.1))
plt.xlabel(r"$x_0$")

for epsi in epsis:
    data = np.loadtxt(f"data/x0-asymm-epsi{epsi*10:.0f}.csv", delimiter=",")
    plt.plot(data[:, 0], data[:, 1], label=rf"$\varepsilon={epsi:.1f}$")

plt.text(
    0.97,
    0.92,
    "(b)",
    horizontalalignment="right",
    verticalalignment="center",
    transform=plt.gca().transAxes,
)

if show_legend:
    plt.legend(loc=0, ncols=2, fontsize="small").get_frame().set_linewidth(0.4)

plt.savefig("figs/fig3-sym-asym.pdf", format="pdf")
plt.close()

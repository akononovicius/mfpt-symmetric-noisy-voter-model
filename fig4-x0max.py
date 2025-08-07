import matplotlib.pyplot as plt
import numpy as np

show_grid = False
show_legend = False

epsis = [0, 1.6, 3.2]

fig = plt.figure(figsize=(3, 2))

# MFPT curves for the symmetric case
plt.grid(show_grid)
plt.ylabel(r"$x_{0,\text{max}}$")
plt.ylim([0.02, 1.03])
plt.yticks(np.arange(0.05, 1.1, 0.225))
plt.xlabel(r"$H$")
plt.xticks(np.arange(0.05, 1.1, 0.3))

for epsi in epsis:
    data = np.loadtxt(f"data/x0max-epsi{10*epsi:.0f}.csv", delimiter=",", dtype=float)
    plt.plot(data[:, 1], data[:, 2], label=rf"$\varepsilon={epsi:.1f}$")
plt.plot(data[:, 1], (data[:, 0] + data[:, 1]) / 2, "k--", label=r"$(H+L)/2$")

if show_legend:
    plt.legend(loc=0, ncols=2, fontsize="small").get_frame().set_linewidth(0.4)

plt.savefig("figs/fig4-x0max.pdf", format="pdf")
plt.close()

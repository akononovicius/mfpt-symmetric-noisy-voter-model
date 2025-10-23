import matplotlib.pyplot as plt
import numpy as np

show_grid = True
show_legend = False

epsis = [0, 1.6, 3.2]
markers = list("soD")

fig = plt.figure(figsize=(3, 2))

# MFPT curves for the symmetric case
plt.grid(show_grid)
plt.ylabel(r"$x_{0,\text{max}}$")
plt.ylim([0.02, 1.03])
plt.yticks(np.arange(0.05, 1.1, 0.225))
plt.xlabel(r"$H$")
plt.xticks(np.arange(0.05, 1.1, 0.3))

for idx, epsi in enumerate(epsis):
    data = np.loadtxt(f"data/x0max-epsi{10 * epsi:.0f}.csv", delimiter=",", dtype=float)
    odd_indices = np.arange(1, len(data), 2)
    extra_indices = np.array([len(data) - 2, len(data) - 1])
    indices_to_plot = np.unique(np.concatenate((odd_indices, extra_indices)))
    plt.plot(
        data[indices_to_plot, 1],
        data[indices_to_plot, 2],
        markers[idx],
        label=rf"$\varepsilon={epsi:.1f}$",
    )
plt.plot(data[:, 1], (data[:, 0] + data[:, 1]) / 2, "k--", label=r"$(H+L)/2$")

if show_legend:
    plt.legend(loc=0, ncols=2, fontsize="small").get_frame().set_linewidth(0.4)

plt.savefig("figs/fig4-x0max.pdf", format="pdf")
plt.close()

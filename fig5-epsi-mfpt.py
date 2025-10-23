import matplotlib.pyplot as plt
import numpy as np

from theory.ra import theory_general as theory_ra_general


def __create_linear_step_mask(
    data: np.ndarray, smallest_step: float, offset: int = 0
) -> np.ndarray:
    mask = np.zeros(len(data), dtype=bool)
    if smallest_step <= 0:
        mask[:] = True
        return mask

    last_shown = -np.inf
    for idx, val in enumerate(data[offset:, 0]):
        if val - last_shown >= smallest_step:
            mask[offset + idx] = True
            last_shown = val

    return mask


show_grid = True
main_plot_min_step = 5

low_absorbing = 0.03
low_reflecting = 0.03
high_absorbing = 0.63
x_0_ticks = np.linspace(low_reflecting, high_absorbing, 4)
fixed_x0 = 0.23

fig = plt.figure(figsize=(6, 2))

# Overal AA dependence
plt.subplot(121)
plt.grid(show_grid)
plt.ylim([1.1e-1, 3e4])
plt.yticks([1e0, 1e1, 1e2, 1e3, 1e4])
plt.ylabel(r"$\overline{T}$")
plt.xlabel(r"$\varepsilon$")

data_aa = np.loadtxt("data/epsi-mfpt-aa.csv", delimiter=",", dtype=float)
data_aa = data_aa[np.argsort(data_aa[:, 0])]
theory_aa = np.loadtxt("theory/epsi-mfpt-aa.csv", delimiter=",", dtype=float)

approx_aa_mask = data_aa[:, 0] > theory_aa[-1, 0]
approx_aa_mask[np.argmax(approx_aa_mask) - 1] = True

approx_aa_factor_k = (data_aa[-2, 0] - data_aa[-1, 0]) / np.log(
    data_aa[-2, 1] / data_aa[-1, 1]
)
last_aa_theory_epsi = theory_aa[-1, 0]
last_aa_theory_mfpt = theory_aa[-1, 1]
approx_aa_factor_c = (
    np.log(last_aa_theory_mfpt) - last_aa_theory_epsi / approx_aa_factor_k
)
theory_aa_2 = np.exp(
    data_aa[approx_aa_mask, 0] / approx_aa_factor_k + approx_aa_factor_c
)

main_aa_plot_mask = __create_linear_step_mask(data_aa, main_plot_min_step)

plt.semilogy()
plt.minorticks_off()
plt.text(
    0.97,
    0.92,
    "(a)",
    horizontalalignment="right",
    verticalalignment="center",
    transform=plt.gca().transAxes,
)
plt.plot(theory_aa[:, 0], theory_aa[:, 1], "k")
plt.plot(data_aa[approx_aa_mask, 0], theory_aa_2, color="#999999")
plt.plot(data_aa[main_aa_plot_mask, 0], data_aa[main_aa_plot_mask, 1], "rs")

# Overal RA dependence
plt.subplot(122)
plt.grid(show_grid)
plt.xlabel(r"$\varepsilon$")
# plt.ylabel(r"$\overline{T}$")
plt.ylabel("")
plt.ylim([1.1e-1, 3e4])
plt.yticks([1e0, 1e1, 1e2, 1e3, 1e4])

data_ra = np.loadtxt("data/epsi-mfpt-ra.csv", delimiter=",", dtype=float)
data_ra = data_ra[np.argsort(data_ra[:, 0])]
theory_ra = np.loadtxt("theory/epsi-mfpt-ra.csv", delimiter=",", dtype=float)

main_ra_plot_mask = __create_linear_step_mask(data_ra, main_plot_min_step)

approx_ra_mask = data_ra[:, 0] > theory_ra[-1, 0]
approx_ra_mask[np.argmax(approx_ra_mask) - 1] = True
theory_ra_2 = theory_ra_general(
    data_ra[approx_ra_mask, 0], fixed_x0, low_reflecting, high_absorbing
)

plt.semilogy()
plt.minorticks_off()
plt.gca().set_yticklabels([])
plt.text(
    0.97,
    0.92,
    "(b)",
    horizontalalignment="right",
    verticalalignment="center",
    transform=plt.gca().transAxes,
)
plt.plot(theory_ra[:, 0], theory_ra[:, 1], "k")
plt.plot(data_ra[approx_ra_mask, 0], theory_ra_2, color="#999999")
plt.plot(data_ra[main_ra_plot_mask, 0], data_ra[main_ra_plot_mask, 1], "rs")

# inset for AA dependence zoom in
inset_aa_ax = fig.add_axes((0.14, 0.62, 0.2, 0.3))
inset_aa_theory_mask = theory_aa[:, 0] < 51
inset_aa_data_mask = data_aa[:, 0] < 51
inset_aa_ax.set_ylim((0.15, 0.45))
inset_aa_ax.tick_params(labelsize=6.5)
inset_aa_ax.grid(show_grid)
inset_aa_ax.plot(
    theory_aa[inset_aa_theory_mask, 0], theory_aa[inset_aa_theory_mask, 1], "k"
)
inset_aa_ax.plot(data_aa[inset_aa_data_mask, 0], data_aa[inset_aa_data_mask, 1], "rs")

# inset for RA dependence zoom in
inset_ra_ax = fig.add_axes((0.61, 0.62, 0.2, 0.3))
inset_ra_theory_mask = theory_ra[:, 0] < 51
inset_ra_data_mask = data_ra[:, 0] < 51
inset_ra_ax.set_ylim((0.15, 0.45))
inset_ra_ax.tick_params(labelsize=6.5)
inset_ra_ax.grid(show_grid)
inset_ra_ax.plot(
    theory_ra[inset_ra_theory_mask, 0], theory_ra[inset_ra_theory_mask, 1], "k"
)
inset_ra_ax.plot(data_ra[inset_ra_data_mask, 0], data_ra[inset_ra_data_mask, 1], "rs")

plt.tight_layout()
plt.savefig("figs/fig5-epsi-mfpt.pdf", format="pdf")
plt.close()

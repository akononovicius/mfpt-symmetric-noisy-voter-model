import numpy as np
import typer

from nvm_fpt import get_passage_times


def main(
    out_filename: str,
    *,
    n_samples: int = 10000,
    rate: float = 0.5,
    n_x_0: int = 15,
    to_left: float = 1e-3,
    to_right: float = 0.999,
    to_shift: float = -1,
    max_time: float = 1e6,
    sde_time_step: float = 1e-5,
    seed: int = -1,
) -> None:
    if seed < 0:
        rng = np.random.default_rng()
        seed = int(rng.integers(0, int(2**20)))

    if to_shift < 0:
        interval = to_right - to_left
        step = interval / (n_x_0 - 1)
        to_shift = step / 10

    x_0_list = np.linspace(to_left + to_shift, to_right - to_shift, num=n_x_0)
    data = np.array(
        [
            np.mean(
                get_passage_times(
                    x_0,
                    x_a=[to_right],
                    x_r=[to_left],
                    n_samples=n_samples,
                    max_time=max_time,
                    birth_rate=rate,
                    death_rate=rate,
                    dt=sde_time_step,
                    seed=seed + idx,
                )
            )
            for idx, x_0 in enumerate(x_0_list)
        ]
    )
    result = np.vstack((x_0_list, data)).T

    np.savetxt(out_filename, result, fmt="%.8f", delimiter=",")


if __name__ == "__main__":
    typer.run(main)

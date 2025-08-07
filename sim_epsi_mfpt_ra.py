import numpy as np
import typer

from nvm_fpt import get_passage_times


def main(
    *,
    n_samples: int = 10000,
    rate: float = 0.5,
    x_0: float = 0.5,
    to_left: float = 1e-3,
    to_right: float = 0.999,
    max_time: float = 1e6,
    sde_time_step: float = 1e-5,
    seed: int = -1,
) -> None:
    if seed < 0:
        rng = np.random.default_rng()
        seed = int(rng.integers(0, int(2**20)))

    data = get_passage_times(
        x_0,
        x_a=[to_right],
        x_r=[to_left],
        n_samples=n_samples,
        max_time=max_time,
        birth_rate=rate,
        death_rate=rate,
        dt=sde_time_step,
        seed=seed,
    )

    print(f"{rate:.2f},{np.mean(data):.4f}")


if __name__ == "__main__":
    typer.run(main)

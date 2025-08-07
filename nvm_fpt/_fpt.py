import os
from ctypes import CDLL, POINTER, c_double, c_int, c_long
from gc import collect as collect_garbage
from typing import Optional

import numpy as np

___ctypes_local_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
___lib_c = CDLL(___ctypes_local_dir + "libfpt.so")
___lib_c.get_passage_times.argtypes = [
    c_long,  # n_samples
    c_double,  # max_time
    c_double,  # x_0
    POINTER(c_double),  # x_f
    c_int,  # n_final
    POINTER(c_double),  # x_r
    c_int,  # n_reflected
    c_double,  # epsi_b
    c_double,  # epsi_d
    c_double,  # dt
    c_int,  # rng_seed
    POINTER(c_double),  # output
]
___lib_c.get_passage_times.restype = None


def get_passage_times(
    x_0: float,
    *,
    x_a: list[float] = [],
    x_r: list[float] = [],
    n_samples: int = 10000,
    max_time: float = 1e6,
    birth_rate: float = 0.5,
    death_rate: float = 0.5,
    dt: float = 1e-5,
    seed: int = -1
) -> np.ndarray:
    """Obtain FPTs from the noisy voter model.

    Input:
        x_0:
            Initial condition. Must be between boundary conditions.
        x_a: (default: [])
            Absorbing boundary conditions. You must specify at least one.
            Note that you should specify exactly two boundary conditions
            in total.
        x_r: (default: [])
            Reflective boundary conditions. May be specified, but this is
            not neccesary. Note that natural reflective boundary conditions
            will be added automatically, if you specify less than two
            boundary conditions.
        n_samples: (default: 10000)
            How many samples to take.
        max_time: (default: 1e6)
            Longest FPT to consider. If FPT becomes greater than `max_time`,
            sampling is stopped, and `max_time` is recorded.
        birth_rate: (default: 0.5)
            Parameter of the noisy voter model.
        death_rate: (default: 0.5)
            Parameter of the noisy voter model.
        dt: (default: 1e-5)
            Noisy voter model is simulated by numerically solving SDE
            using Euler-Maruyama method. This `dt` sets the time step
            of the method. Lower values will result in better samples,
            but longer run times.
        seed: (default: -1)
            Seed to use for RNG. If seed is negative, then seed will
            be generated automatically.

    Output:
        Numpy array containing `n_samples` FPT samples.
    """
    # if initial condition is on the absorbing boundary, then FPT = 0
    if x_0 in x_a:
        return np.zeros(n_samples)

    # the code doesn't hand well this particular case
    if x_0 in x_r:
        raise ValueError("Initial condition (x_0) can't be on reflective boundary.")

    # FPT is measured to an absorbing boundary
    n_absorbing = len(x_a)
    if n_absorbing == 0:
        raise ValueError("No absorbing boundary specified.")

    n_reflected = len(x_r)

    # for one-dimensional process more than two boundaries make no sense
    if (n_absorbing + n_reflected) > 2:
        raise ValueError("There are more than two boundary conditions.")
    # there should be exactly two boundaries specified, otherwise append
    # relevant natural boundary
    if (n_absorbing + n_reflected) < 2:
        if x_a[0] < x_0:
            x_r = [1.0]
        else:
            x_r = [0.0]

    # initial condition must be between boundary conditions
    if n_absorbing == 2:
        x_a = sorted(x_a)
        if x_0 < x_a[0] or x_a[1] < x_0:
            raise ValueError(
                "Initial condition must be between two boundary conditions"
            )
    else:
        if (x_0 < x_a[0] and x_0 < x_r[0]) or (x_a[0] < x_0 and x_r[0] < x_0):
            raise ValueError(
                "Initial condition must be between two boundary conditions"
            )

    # auto-generate seed
    if seed < 0:
        rng = np.random.default_rng()
        seed = int(rng.integers(0, int(2**20)))

    data = (c_double * n_samples)()
    c_x_a = (c_double * n_absorbing)(*x_a)
    c_x_r = (c_double * n_reflected)(*x_r)

    ___lib_c.get_passage_times(
        n_samples,
        max_time,
        x_0,
        c_x_a,
        n_absorbing,
        c_x_r,
        n_reflected,
        birth_rate,
        death_rate,
        dt,
        seed,
        data,
    )
    ret = np.array(list(data))
    del data
    collect_garbage()

    return ret

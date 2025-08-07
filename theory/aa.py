import numpy as np


def theory_epsi0(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        return -z * np.log(z) - (1 - z) * np.log(1 - z)

    denominator = high - low
    term_1 = (low * _f(high) - high * _f(low)) / denominator
    term_2 = (_f(low) - _f(high)) / denominator

    return np.asarray(term_1 + term_2 * x_0 + _f(x_0))


def theory_epsi5(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    term_0 = np.arcsin(1 - 2 * x_0)
    term_low = np.arcsin(1 - 2 * low)
    term_high = np.arcsin(1 - 2 * high)

    return np.asarray(0.5 * (term_0 - term_low) * (term_high - term_0))


def theory_epsi10(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        return np.log(1 - z)

    def _g(z: np.ndarray | float) -> np.ndarray | float:
        return np.log(z) - np.log(1 - z)

    term_frac = (_f(high) - _f(low)) / (_g(low) - _g(high))

    return np.asarray(_f(x_0) - _f(high) + term_frac * (_g(x_0) - _g(high)))


def theory_epsi15(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        return -0.5 * (1 + 0.5 * _g(z) * np.arccos(np.sqrt(z)))

    def _g(z: np.ndarray | float) -> np.ndarray | float:
        return 2 * (1 - 2 * z) / np.sqrt((1 - z) * z)

    denominator = _g(high) - _g(low)

    term_1 = (_f(high) * _g(low) - _f(low) * _g(high)) / denominator
    term_2 = (_f(low) - _f(high)) / denominator

    return np.asarray(term_1 + term_2 * _g(x_0) + _f(x_0))


def theory_epsi20(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        return (1 / 6) * (1 / (z - 1) + 2 * np.log(1 - z))

    def _g(z: np.ndarray | float) -> np.ndarray | float:
        return (1 - 2 * z) / ((z - 1) * z) + 2 * (np.log(z) - np.log(1 - z))

    term_1 = _f(x_0) - _f(high)
    frac_term = (_f(high) - _f(low)) / (_g(low) - _g(high))

    return np.asarray(term_1 + frac_term * (_g(x_0) - _g(high)))


def theory_epsi25(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        poly_z = z * (1 - z)
        poly_32_z = poly_z ** (3 / 2)
        poly_strange_z = np.polyval([16, -24, 6, 1], z)
        return 2 * poly_strange_z / (3 * poly_32_z)

    def _g(z: np.ndarray | float) -> np.ndarray | float:
        poly_z = z * (1 - z)
        poly_32_z = poly_z ** (3 / 2)
        poly_strange_z = np.polyval([16, -24, 6, 1], z)
        arccos_z = np.arccos(np.sqrt(z))

        return (
            -5 / 24 - 1 / (32 * poly_z) - poly_strange_z * arccos_z / (32 * poly_32_z)
        )

    tp_high = _g(high)
    tp_x_0 = _g(x_0)
    tp_low = _g(low)

    beta_high = _f(high)
    beta_low = _f(low)
    beta_x_0 = _f(x_0)

    num_1 = tp_high * beta_low - tp_low * beta_high
    denom_1 = beta_high - beta_low
    term_1 = num_1 / denom_1

    num_2 = (tp_low - tp_high) * beta_x_0
    term_2 = num_2 / denom_1

    term_3 = tp_x_0

    return np.asarray(term_1 + term_2 + term_3)

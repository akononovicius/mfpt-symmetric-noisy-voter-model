import numpy as np


def theory_epsi0(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        return (z - 1) * np.log(1 - z) - z * np.log(z)

    def _g(z: np.ndarray | float) -> np.ndarray | float:
        return np.log(1 - z) - np.log(z)

    term_1 = (high - x_0) * _g(low)
    term_2 = _f(x_0) - _f(high)

    return np.asarray(term_1 + term_2)


def theory_epsi5(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    term_0 = np.arcsin(2 * x_0 - 1)
    term_low = np.arcsin(2 * low - 1)
    term_high = np.arcsin(2 * high - 1)

    return np.asarray(0.5 * (term_high - term_0) * (term_high - 2 * term_low + term_0))


def theory_epsi10(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    term_1 = low * np.log(x_0 / (1 - x_0))
    term_2 = low * np.log((1 - high) / high)
    term_3 = np.log((1 - x_0) / (1 - high))

    return np.asarray(term_1 + term_2 + term_3)


def theory_epsi15(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        return -0.5 * (1 + 0.5 * _g(z) * np.arccos(np.sqrt(z)))

    def _g(z: np.ndarray | float) -> np.ndarray | float:
        return 2 * (1 - 2 * z) / np.sqrt((1 - z) * z)

    term_1 = (1 - low) * low * _g(low) + 2 * np.arccos(np.sqrt(low))
    term_2 = _g(x_0) - _g(high)
    term_3 = _f(x_0) - _f(high)

    return np.asarray(0.125 * term_1 * term_2 + term_3)


def theory_epsi20(x_0: np.ndarray, low: float, high: float) -> np.ndarray:
    def _f(z: np.ndarray | float) -> np.ndarray | float:
        term_1 = z / (z - 1)
        term_2 = 2 * np.log(1 - z)
        return (term_1 + term_2) / 6

    def _g(z: np.ndarray | float) -> np.ndarray | float:
        term_1 = 2 * z - 1
        term_2 = z * (1 - z)
        term_3 = 2 * (np.log(z) - np.log(1 - z))
        return term_1 / term_2 + term_3

    term_1 = (3 - 2 * low) * (low**2) / 6
    term_2 = _g(x_0) - _g(high)
    term_3 = _f(x_0) - _f(high)

    return np.asarray(term_1 * term_2 + term_3)


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

    def _h(z: np.ndarray | float) -> np.ndarray | float:
        poly_z = z * (1 - z)
        poly_strange_z = np.polyval([16, -24, 2, 3], z)
        arccos_z = np.arccos(np.sqrt(z))

        return (np.sqrt(poly_z) * poly_strange_z + 3 * arccos_z) / 64

    term_1 = _h(low) * (_f(x_0) - _f(high))
    term_2 = _g(x_0) - _g(high)

    return np.asarray(term_1 + term_2)


def theory_general(epsi: np.ndarray, x_0: float, low: float, high: float) -> np.ndarray:
    term_1 = 2 * np.pi * high / (epsi ** (3 / 2))
    term_2 = -epsi * np.log(4 * high * (1 - high))

    return np.asarray(term_1 * np.exp(term_2))

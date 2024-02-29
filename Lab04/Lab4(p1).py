from matplotlib import pyplot as plt
import numpy as np

def func(x: list[float], N: int) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    a0 = 0.62
    a1 = 0.48
    a2 = 0.38
    N = 11
    return [a0 - a1 * np.abs(t - (N-1)/2) - a2 * np.cos(2 * np.pi * t / N) for t in x]


def tabulate(N: int, a: float, b: float, n: int) -> tuple[list[float], list[float]]:
    x = [ a + x*(b - a)/n for x in range(n) ]
    y = func(x, N)
    return (x, y)

def main():
    N = 11
    res = tabulate(N, 0, 50, 1000)

    plt.plot(res[0], res[1])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
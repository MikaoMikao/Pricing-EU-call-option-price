import numpy as np
from scipy.stats import norm

# parameters configuration
K = 110  # strike price
r = 0.015  # risk-free rate
T = 1  # expiration time in years
sigma = 0.3  # volitility in BS model
S0 = 100  # initial asset price
S_max = 150  # max asset price
N = 1000  # number of time steps
M = 100  # number of price steps


def Theoretical_price_call(K, r, S0, T, sigma):
    a = (np.log(S0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    b = a - sigma * np.sqrt(T)
    return S0 * norm.cdf(a) - K * np.exp(-r * T) * norm.cdf(b)


C_theoretical = Theoretical_price_call(K, r, S0, T, sigma)
print(f"欧式看涨期权价格: {C_theoretical:.2f}")

# define finite difference method
def finite_difference_european_call(S0, K, T, r, sigma, S_max, M, N):

    dt = T / N

    # initialise grid
    grid = np.zeros((M + 1, N + 1))
    S = np.linspace(0, S_max, M + 1)

    # terminal conditions
    grid[:, -1] = np.maximum(S - K, 0)

    # boundary conditions
    grid[0, :] = 0  # S=0
    grid[-1, :] = S_max - K * np.exp(-r * (T - np.linspace(0, T, N + 1)))  # S -> S_max

    # define coefficient
    alpha = 0.5 * dt * (sigma ** 2 * np.arange(M) ** 2 - r * np.arange(M))
    beta = 1 - dt * (sigma ** 2 * np.arange(M) ** 2 + r)
    gamma = 0.5 * dt * (sigma ** 2 * np.arange(M) ** 2 + r * np.arange(M))

    # backward iteration
    for n in reversed(range(N)):
        for i in range(1, M):
            grid[i, n] = alpha[i] * grid[i - 1, n + 1] + beta[i] * grid[i, n + 1] + gamma[i] * grid[i + 1, n + 1]

    # option prices with S0
    price = np.interp(S0, S, grid[:, 0])
    return price


# pricing EU call option price
option_price = finite_difference_european_call(S0, K, T, r, sigma, S_max, M, N)
print(f"EU call option price(finite difference): {option_price:.2f}")
print(f"EU call option price(theoretical): {C_theoretical:.2f}")
print(f"EU call option error:{abs(option_price-C_theoretical):.2f}")

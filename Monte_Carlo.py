import numpy as np
from scipy.stats import norm

# parameters configuration
K = 110  # strike price
r = 0.015  # risk-free rate
T = 1  # expiration time in years
sigma = 0.3  # volitility in BS model
S0 = 100  # initial asset price
N = 2000  # number of time steps in simulation
M = 10000  # Monte Carlo samples


# theoretical EU call option price
def Theoretical_price_call(K, r, S0, T, sigma):
    a = (np.log(S0 / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    b = a - sigma * np.sqrt(T)
    return S0 * norm.cdf(a) - K * np.exp(-r * T) * norm.cdf(b)


C_theoretical = Theoretical_price_call(K, r, S0, T, sigma)


# MC simulated EU call option prices
def simulate_price(r, K, sigma, S0, N, M, T):
    dt = T / N
    s = np.zeros((M, N))
    s[:, 0] = S0
    normal_sample = norm.rvs(size=(M, N))

    for i in range(1, N):
        s[:, i] = s[:, i - 1] * np.exp((r - sigma ** 2 / 2) * dt + sigma * np.sqrt(dt) * normal_sample[:, i])
    sT = s[:, -1]

    price = (np.maximum(0, sT - K)) * (np.exp(-r * T))
    mean = np.sum(price) / M  # an approximate option price
    return mean


C_simulated= simulate_price(r, K, sigma, S0, N, M, T)
error = abs(C_simulated - C_theoretical)
print(f"EU call option price(theoretical): {C_theoretical:.2f}")
print(f"EU call option price(Monte Carlo):{C_simulated:.2f}")
print(f"EU call option price error: {error:.2f}")

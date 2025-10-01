import numpy as np
from scipy.stats import norm

def call_price(S, K, T, r, sigma):
    """
    Black-Scholes equation for European call option price
    """
    d1 = (np.log((S/K)) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return norm.cdf(d1) * S - norm.cdf(d2) * K * np.exp(-r * T)

def put_price(S, K, T, r, sigma):
    """
    Black-Scholes equation for European put option price
    """
    d1 = (np.log((S/K)) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
import numpy as np
from src.black_scholes import call_price, put_price


def test_call_put_parity():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    call = call_price(S, K, T, r, sigma)
    put = put_price(S, K, T, r, sigma)

    # Put-Call Parity: C - P = S - Ke^(-rT)
    lhs = call - put
    rhs = S - K * np.exp(-r * T)
    assert abs(lhs - rhs) < 1e-6

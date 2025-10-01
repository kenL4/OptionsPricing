from black_scholes import call_implied_volatility
from market_pricing import get_options_dates, get_call_options
from datetime import datetime
import yfinance as yf

dates = get_options_dates("AAPL")
options = get_call_options("AAPL", dates[0])

S = yf.Ticker("AAPL").history(period="1d")["Close"].iloc[-1]

expiry_dt = datetime.strptime(dates[0], "%Y-%m-%d")
today = datetime.today()
T = max((expiry_dt - today).days / 365, 1e-6)

for i, option in options.iterrows():
    if option["bid"] <= 0 or option["ask"] <= 0:
        continue
    market_price = (option["bid"] + option["ask"]) / 2
    K = option["strike"]

    r = 0.05

    print(S, K, T, r, market_price)
    bs_iv = call_implied_volatility(S, K, T, r, market_price)
    print(f'Yfinance: {option["impliedVolatility"]} Computed: {bs_iv}')

import yfinance as yf


def get_options_dates(symbol):
    """
    Returns a tuple of options expiry dates
    """
    ticker = yf.Ticker(symbol)
    options_dates = ticker.options
    return options_dates


def get_call_options(symbol, expiry_date):
    """
    Returns a tuple of call options with a given expiry date
    """
    ticker = yf.Ticker(symbol)
    opt = ticker.option_chain(expiry_date)
    calls = opt.calls
    return calls


def get_put_options(symbol, expiry_date):
    """
    Returns a tuple of put options with a given expiry date
    """
    ticker = yf.Ticker(symbol)
    opt = ticker.option_chain(expiry_date)
    puts = opt.puts
    return puts

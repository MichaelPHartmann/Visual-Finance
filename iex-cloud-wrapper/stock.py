from ._common import *

#   Financials
def financials(symbol, token, period=None, sandbox_state=False, vprint=False):
    IEX_FINANCIALS_URL = prepend_iex_url('stock', sandbox_state=sandbox_state) + '{symbol}/financials?'
    """:return: Brief overview of a company's financial statements.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param period: The time interval of financial statements returned.
    :type period: accepted values are ['annual', 'quarterly'], optional
    """
    url = replace_url_var(IEX_FINANCIALS_URL, symbol=symbol)
    url += f'period={period}' if period else ''
    if vprint: print(url)
    return get_iex_json_request(url, token)

#   Key Stats
def key_stats(symbol, token, stat=False, sandbox_state=False, vprint=False):
    IEX_STATS_URL = prepend_iex_url('stock', sandbox_state=sandbox_state) + '{symbol}/stats'
    """:return: Important and key statistics for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param stat: The specific stat which you would like to return.
    :type stat: string, optional
    """
    url = replace_url_var(IEX_STATS_URL, symbol=symbol)
    url += str(stat) if stat else '?'
    if vprint: print(url)
    return get_iex_json_request(url, token)

#   News
def news(symbol, token, last=None, sandbox_state=False, vprint=False):
    IEX_NEWS_URL = prepend_iex_url('stock', sandbox_state=sandbox_state) + '{symbol}/news'
    """:return: News item summaries for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param last: The number of news items to return.
    :type last: integer, optional
    """
    url = replace_url_var(IEX_NEWS_URL, symbol=symbol)
    url += f'/last/{last}?' if last else '?'
    if vprint: print(url)
    return get_iex_json_request(url, token)

#   Price
def price(symbol, token, external=False, sandbox_state=False, vprint=False):
    IEX_PRICE_URL = prepend_iex_url('stock', sandbox_state=sandbox_state) + '{symbol}/price?'
    """:return: Single float value of the requested ticker's price.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_PRICE_URL, symbol=symbol)
    if vprint: print(url)
    return get_iex_json_request(url, token)

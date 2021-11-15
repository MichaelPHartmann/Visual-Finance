import requests

def prepend_iex_url(section, sandbox_state=False):
    if sandbox_state is True:
        url = f'https://sandbox.iexapis.com/stable/{section}/'
    else:
        url = f'https://cloud.iexapis.com/stable/{section}/'
    return url

def append_iex_token(url, token):
        return f"{url}&token={token}"

def get_iex_json_request(url, token, vprint=False):
    url = append_iex_token(url, token)
    if vprint: print(f"Making request: {url}")
    result = requests.get(url)
    if vprint: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

def replace_url_var(url, **kwargs):
    for key, value in kwargs.items():
        url = url.replace('{' + key + '}', value)
    return url

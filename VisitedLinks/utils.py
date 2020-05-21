import requests


def get_server_type(link):
    try:
        r = requests.head(link, timeout=5)
        return r.headers['Server']
    except Exception:
        return 'Unknown'

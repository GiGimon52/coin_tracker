# import requests
#
#
# def get_price_from_coinpaprika():
#     print("→ Coinpaprika")
#     url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"
#     r = requests.get(url, timeout=10)
#     r.raise_for_status()
#     return r.json()["quotes"]["USD"]["price"]

# import requests
#
# def get_price_from_coinpaprika(ticker_id: str):
#     print(f"→ Coinpaprika ({ticker_id})")
#     url = f"https://api.coinpaprika.com/v1/tickers/{ticker_id}"
#     r = requests.get(url, timeout=10)
#     r.raise_for_status()
#     return r.json()["quotes"]["USD"]["price"]

import requests

def get_price_from_coinpaprika(ticker_id: str) -> float:
    print(f"→ Coinpaprika ({ticker_id})")
    url = f"https://api.coinpaprika.com/v1/tickers/{ticker_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["quotes"]["USD"]["price"]
    except (KeyError, requests.RequestException) as e:
        print(f"[!] Ошибка Coinpaprika: {e}")
        raise

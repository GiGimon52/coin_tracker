# import requests
#
#
# def get_price_from_coingecko():
#     print("→ CoinGecko")
#     url = "https://api.coingecko.com/api/v3/simple/price"
#     params = {"ids": "bitcoin", "vs_currencies": "usd"}
#     r = requests.get(url, params=params, timeout=10)
#     r.raise_for_status()
#     return r.json()["bitcoin"]["usd"]

# import requests
#
# def get_price_from_coingecko(coin_id: str):
#     print(f"→ CoinGecko ({coin_id})")
#     url = "https://api.coingecko.com/api/v3/simple/price"
#     params = {"ids": coin_id, "vs_currencies": "usd"}
#     r = requests.get(url, params=params, timeout=10)
#     r.raise_for_status()
#     return r.json()[coin_id]["usd"]

import requests

def get_price_from_coingecko(coin_id: str) -> float:
    print(f"→ CoinGecko ({coin_id})")
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[coin_id]["usd"]
    except (KeyError, requests.RequestException) as e:
        print(f"[!] Ошибка CoinGecko: {e}")
        raise

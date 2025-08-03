# import requests
# from sources.coingecko import get_price_from_coingecko
# from sources.coinpaprika import get_price_from_coinpaprika
#
# class BitcoinPriceFetcher:
#     def __init__(self):
#         self.sources = [
#             get_price_from_coingecko,
#             get_price_from_coinpaprika
#         ]
#
#     def get_price(self):
#         for source in self.sources:
#             try:
#                 price = source()
#                 print("[✓] Цена получена")
#                 return price
#             except requests.exceptions.RequestException as e:
#                 print(f"[!] Источник не сработал: {e}")
#             except Exception as e:
#                 print(f"[x] Внутренняя ошибка: {e}")
#         return None


# import requests
# from sources.coingecko import get_price_from_coingecko
# from sources.coinpaprika import get_price_from_coinpaprika
#
# class CryptoPriceFetcher:
#     def __init__(self, coin_id="bitcoin", ticker_id="btc-bitcoin"):
#         self.coin_id = coin_id
#         self.ticker_id = ticker_id
#         self.sources = [
#             self._coingecko_source,
#             self._coinpaprika_source
#         ]
#
#     def _coingecko_source(self):
#         return get_price_from_coingecko(self.coin_id)
#
#     def _coinpaprika_source(self):
#         return get_price_from_coinpaprika(self.ticker_id)
#
#     def get_price(self):
#         for source in self.sources:
#             try:
#                 price = source()
#                 print("[✓] Цена получена")
#                 return price
#             except requests.exceptions.RequestException as e:
#                 print(f"[!] Источник не сработал: {e}")
#             except Exception as e:
#                 print(f"[x] Внутренняя ошибка: {e}")
#         return None

import requests
from sources.coingecko import get_price_from_coingecko
from sources.coinpaprika import get_price_from_coinpaprika

class CryptoPriceFetcher:
    def __init__(self, coin_id="bitcoin", ticker_id="btc-bitcoin"):
        self.coin_id = coin_id
        self.ticker_id = ticker_id
        self.sources = [
            self._coingecko_source,
            self._coinpaprika_source
        ]

    def _coingecko_source(self):
        print(f"→ CoinGecko: {self.coin_id}")
        return get_price_from_coingecko(self.coin_id)

    def _coinpaprika_source(self):
        print(f"→ Coinpaprika: {self.ticker_id}")
        return get_price_from_coinpaprika(self.ticker_id)

    def get_price(self):
        for source in self.sources:
            try:
                price = source()
                if price is not None:
                    print("[✓] Цена получена")
                    return price
            except requests.exceptions.RequestException as e:
                print(f"[!] Источник не сработал: {e}")
            except Exception as e:
                print(f"[x] Внутренняя ошибка: {e}")
        return None

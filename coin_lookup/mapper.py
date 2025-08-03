# import requests
#
# class CoinMapper:
#     def __init__(self):
#         self.coins = []
#         self._load_common_coins()
#
#     def _load_common_coins(self):
#         try:
#             cg_list = requests.get("https://api.coingecko.com/api/v3/coins/list", timeout=10).json()
#             cp_list = requests.get("https://api.coinpaprika.com/v1/tickers", timeout=10).json()
#
#             cg_map = {
#                 (c["name"].lower(), c["symbol"].lower()): {
#                     "name": c["name"],
#                     "symbol": c["symbol"],
#                     "coingecko_id": c["id"]
#                 }
#                 for c in cg_list
#             }
#
#             cp_map = {
#                 (c["name"].lower(), c["symbol"].lower()): {
#                     "name": c["name"],
#                     "symbol": c["symbol"],
#                     "coinpaprika_id": c["id"]
#                 }
#                 for c in cp_list
#             }
#
#             common_keys = set(cg_map.keys()) & set(cp_map.keys())
#
#             self.coins = [
#                 {
#                     "name": cg_map[k]["name"],
#                     "symbol": cg_map[k]["symbol"].lower(),
#                     "coingecko_id": cg_map[k]["coingecko_id"],
#                     "coinpaprika_id": cp_map[k]["coinpaprika_id"]
#                 }
#                 for k in common_keys
#             ]
#
#             self.coins.sort(key=lambda x: x["name"])
#
#         except Exception as e:
#             print(f"❌ Ошибка при загрузке монет: {e}")
#
#     def search(self, query: str):
#         query = query.strip().lower()
#         return [
#             coin for coin in self.coins
#             if query in coin["name"].lower() or query == coin["symbol"].lower()
#         ]
#
#     def get_ids_by_symbol(self, symbol: str):
#         matches = self.search(symbol)
#         if matches:
#             return matches[0]["coingecko_id"], matches[0]["coinpaprika_id"]
#         return None, None


import requests

class CoinMapper:
    def __init__(self):
        self.coins = []
        self._load_common_coins()

    def _load_common_coins(self):
        try:
            # Получаем списки монет с CoinGecko и Coinpaprika
            cg_response = requests.get("https://api.coingecko.com/api/v3/coins/list", timeout=10)
            cp_response = requests.get("https://api.coinpaprika.com/v1/tickers", timeout=10)

            cg_list = cg_response.json()
            cp_list = cp_response.json()

            # Формируем словари для быстрого доступа по (name, symbol)
            cg_map = {
                (c["name"].lower(), c["symbol"].lower()): {
                    "name": c["name"],
                    "symbol": c["symbol"],
                    "coingecko_id": c["id"]
                }
                for c in cg_list
            }

            cp_map = {
                (c["name"].lower(), c["symbol"].lower()): {
                    "name": c["name"],
                    "symbol": c["symbol"],
                    "coinpaprika_id": c["id"]
                }
                for c in cp_list
            }

            # Ищем пересечения по (name, symbol)
            common_keys = set(cg_map) & set(cp_map)

            self.coins = [
                {
                    "name": cg_map[k]["name"],
                    "symbol": cg_map[k]["symbol"].lower(),
                    "coingecko_id": cg_map[k]["coingecko_id"],
                    "coinpaprika_id": cp_map[k]["coinpaprika_id"]
                }
                for k in common_keys
            ]

            # Сортировка по имени
            self.coins.sort(key=lambda x: x["name"])

        except Exception as e:
            print(f"❌ Ошибка при загрузке монет: {e}")

    def search(self, query: str):
        """Поиск монеты по названию или тикеру."""
        query = query.strip().lower()
        return [
            coin for coin in self.coins
            if query in coin["name"].lower() or query == coin["symbol"].lower()
        ]

    def get_ids_by_symbol(self, symbol: str):
        """Возвращает (coingecko_id, coinpaprika_id) по символу или названию монеты."""
        matches = self.search(symbol)
        if matches:
            return matches[0]["coingecko_id"], matches[0]["coinpaprika_id"]
        return None, None

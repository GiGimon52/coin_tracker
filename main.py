# from datetime import datetime
# from fetcher import BitcoinPriceFetcher
#
#
#
# # ===== Запуск =====
# def main():
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     fetcher = BitcoinPriceFetcher()
#     price = fetcher.get_price()
#
#     if price:
#         print(f"[{now}] BTC: {price:.2f} USD")
#     else:
#         print(f"[{now}] ❌ Не удалось получить цену.")
#
# if __name__ == "__main__":
#     main()



# from datetime import datetime
# from fetcher import BitcoinPriceFetcher
#
# def main():
#     # Выбери любую монету, которую поддерживают обе API
#     coin_id = "ethereum"
#     ticker_id = "eth-ethereum"
#
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     fetcher = BitcoinPriceFetcher(coin_id=coin_id, ticker_id=ticker_id)
#     price = fetcher.get_price()
#
#     if price:
#         print(f"[{now}] {coin_id.upper()}: {price:.2f} USD")
#     else:
#         print(f"[{now}] ❌ Не удалось получить цену для {coin_id.upper()}.")
#
# if __name__ == "__main__":
#     main()


# from datetime import datetime
# from fetcher import BitcoinPriceFetcher
# from utils.coin_mapper import get_coin_ids
#
# def get_crypto_price(coin_name: str):
#     ids = get_coin_ids(coin_name)
#
#     if not ids:
#         print(f"❌ Не удалось найти ID монеты: {coin_name}")
#         return
#
#     coin_id, ticker_id = ids
#     fetcher = BitcoinPriceFetcher(coin_id=coin_id, ticker_id=ticker_id)
#     price = fetcher.get_price()
#
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     if price:
#         print(f"[{now}] {coin_name.upper()}: {price:.2f} USD")
#     else:
#         print(f"[{now}] ❌ Не удалось получить цену для {coin_name.upper()}.")
#
# if __name__ == "__main__":
#     get_crypto_price("bittensor")  # 👈 Просто имя монеты

# from coin_lookup.mapper import CoinMapper
# from fetcher import CryptoPriceFetcher  # если ты не переименовывал
#
# if __name__ == "__main__":
#     mapper = CoinMapper()
#
#     user_input = input("Введите тикер или название монеты: ").strip()
#
#     coin_id, ticker_id = mapper.get_ids_by_symbol(user_input)
#
#     if not coin_id or not ticker_id:
#         print("❌ Не удалось определить ID монеты.")
#     else:
#         fetcher = CryptoPriceFetcher(coin_id=coin_id, ticker_id=ticker_id)
#         price = fetcher.get_price()
#
#         if price:
#             print(f"💰 {user_input.upper()} = {price:.2f} USD")
#         else:
#             print("❌ Не удалось получить цену.")

from coin_lookup.mapper import CoinMapper
from fetcher import CryptoPriceFetcher
from datetime import datetime

if __name__ == "__main__":
    mapper = CoinMapper()

    user_input = input("Введите тикер или название монеты: ").strip()

    if not user_input:
        print("⚠️ Вы ничего не ввели.")
        exit()

    coin_id, ticker_id = mapper.get_ids_by_symbol(user_input)

    if not coin_id or not ticker_id:
        print("❌ Не удалось определить ID монеты.")
    else:
        fetcher = CryptoPriceFetcher(coin_id=coin_id, ticker_id=ticker_id)
        price = fetcher.get_price()

        if price:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] 💰 {user_input.upper()} = {price:.2f} USD")
        else:
            print("❌ Не удалось получить цену.")
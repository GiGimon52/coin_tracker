# from mapper import CoinMapper
#
# if __name__ == "__main__":
#     mapper = CoinMapper()
#
#     user_input = input("🔍 Введите тикер или название монеты: ").strip()
#
#     results = sorted(mapper.search(user_input), key=lambda x: x["name"])
#
#     if results:
#         print(f"\nНайдено {len(results)} совпадений:\n")
#         for coin in results:
#             print(f"• {coin['name']} ({coin['symbol'].upper()})")
#             print(f"  CoinGecko ID:    {coin['coingecko_id']}")
#             print(f"  Coinpaprika ID:  {coin['coinpaprika_id']}\n")
#     else:
#         print("❌ Ничего не найдено.")

from mapper import CoinMapper

def main():
    mapper = CoinMapper()

    user_input = input("🔍 Введите тикер или название монеты: ").strip()

    if not user_input:
        print("⚠️ Пустой ввод. Попробуйте снова.")
        return

    results = mapper.search(user_input)

    if results:
        print(f"\nНайдено {len(results)} совпадений:\n")
        for coin in sorted(results, key=lambda x: x["name"]):
            print(f"• {coin['name']} ({coin['symbol'].upper()})")
            print(f"  CoinGecko ID:    {coin['coingecko_id']}")
            print(f"  Coinpaprika ID:  {coin['coinpaprika_id']}\n")
    else:
        print("❌ Ничего не найдено.")

if __name__ == "__main__":
    main()

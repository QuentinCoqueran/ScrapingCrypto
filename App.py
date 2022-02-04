# coding: utf-8

from input import menu, search_input


class App:

    def __init__(self, request_manager):
        self.requestManager = request_manager;

    def start(self):
        choice = menu()
        while choice != 0:
            if choice == 1:
                self.search()
                pass
            elif choice == 2:
                break
            else:
                print("\n choix incorrect")
                choice = menu()

    def search(self):
        query = search_input()
        coins = self.request_manager.search_currencies(query)
        for coin in coins:
            print(coin.name, coin.symbol, coin.market_cap_rank)
        return coins

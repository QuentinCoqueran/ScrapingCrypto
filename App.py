# coding: utf-8

from Input import Input


class App:

    def __init__(self, request_manager):
        self.request_manager = request_manager

    def start(self):
        choice = Input.menu()
        while choice != 0:
            if choice == 1:
                self.search()
                pass
            elif choice == 2:
                break
            else:
                print("\n choix incorrect")
                choice = Input.menu()

    def search(self):
        query = Input.search_input()
        coins = self.request_manager.search_currencies(query)
        for coin in coins:
            print(coin)
        return coins

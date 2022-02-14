# coding: utf-8

from app.Input import Input


class App:

    def __init__(self, request_manager):
        self.request_manager = request_manager

    def start(self):
        choice = Input.menu()
        while choice != 0:
            if choice == 1:
                self.search()
                if Input.back():
                    choice = 10
                pass
            elif choice == 2:
                choice = self.report()
            else:
                print("\n choix incorrect")
                choice = Input.menu()

    def report(self):
        choice = Input.report_menu()
        while choice != 3:
            if choice == 1:
                break
            elif choice == 2:
                # TODO : Creer un fichier rapport Json
                break
            elif choice == 3:
                break
            else:
                print("\n choix incorrect")
                choice = Input.report_menu()
        return 10

    def search(self):
        query = Input.search_input()
        coins = self.request_manager.search_currencies(query)
        for coin in coins:
            print(coin)
        return coins

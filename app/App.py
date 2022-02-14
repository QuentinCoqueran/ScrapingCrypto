# coding: utf-8

from sys import displayhook
from app.Input import Input
from app.model.Report import Report


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
                self.generate_report()
                # TODO : Creer un fichier rapport Json
                break
            elif choice == 3:
                break
            else:
                print("\n choix incorrect")
                choice = Input.report_menu()
        return 10

    def search_coins(self):
        query = Input.search_input()
        coins = self.request_manager.search_coins(query)
        return coins

    def search_currencies(self):
        query = Input.search_input()
        currencies = self.request_manager.get_currencies(query)
        return currencies


    def generate_report(self):
        coins = []
        currencies = []
        name = ""
        # TODO : choose coins
        # TODO : choose currencies
        self.display_currency()
        report = Report(name, coins, currencies)
        print(report)


    def display_currency(self) :
        list_currencies = self.search_currencies()
        for key, value in enumerate(list_currencies) : 
            print(key,value)
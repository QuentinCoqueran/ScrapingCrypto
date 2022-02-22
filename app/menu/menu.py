from app.api.request_manager import request_manager


class CoinMenu:

    @staticmethod
    def search_coins():
        query = input("\nQuelle cryptomonnaie cherchez-vous ? : ")
        while query is None:
            print("\nErreur")
            query = input("\nQuelle cryptomonnaie cherchez-vous ? : ")
        coins = request_manager.search_coins(query)
        return coins

    @staticmethod
    def display_coins(coins):
        for idx, coin in enumerate(coins):
            print(f'{idx}. {coin.name}')


class CurrencyMenu:

    @staticmethod
    def choose_currency(self, currencies):
        self.display_currencies(currencies)
        query = input("\nQuel ID de devise voulez vous choisir ? : ")
        while query is None:
            print("\nErreur")
            query = input("\nQuel ID de devise voulez vous choisir ? : ")
        return query

    @staticmethod
    def display_currencies(currencies):
        for index, currency in enumerate(currencies):
            print(f'{index}. {currency.short_name}')


class ReportMenu:

    def start(self):
        menu_text = "\n1.Tous mes rapports\n2.Nouveau rapport\n3.Retour\nVotre choix : "
        choice = int(input(menu_text))
        if choice == 1:
            self.my_reports()
            self.start()
        elif choice == 2:
            self.new_report()
            self.start()
            # TODO : Créer un fichier rapport Json
        elif choice == 3:
            return
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.start()

    @staticmethod
    def my_reports():
        print("\nTous mes rapports")

    @staticmethod
    def new_report():
        print("-- Création d'un rapport --")


def back():
    text = "\nRevenir au menu precedent ? O/n (Oui) : "
    return input(text) != "n"

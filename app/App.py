# coding: utf-8

from app.Io import Input, Output
from app.menu.menu import ReportMenu, CoinMenu, back


class App:

    def __init__(self):
        self.coin_menu = CoinMenu()
        self.report_menu = ReportMenu()

    def start(self):
        menu_text = "\n1.Rechercher une cryptomonnaie\n2.Mes rapports\n3.Quitter\nVotre choix : "
        choice = int(input(menu_text))
        if choice == 1:
            self.coin_menu.display_coins(self.coin_menu.search_coins())
            if back():
                self.start()
        elif choice == 2:
            self.report_menu.start()
            self.start()
        elif choice == 3:
            print("Execution terminée, Merci beaucoup.")
            exit(0)
        else:
            print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.start()


    # def currency_choice(self):
    #     # appelle la fonction qui affiche les currencies et qui retourne un int, e
    #     pass

    # def search_currencies(self):
    #     currencies = self.request_manager.get_currencies()
    #     return currencies

    # def generate_report(self):
    #     coins = []
    #     currencies = []
    #     name = ""
    #     # TODO : créer une class ReportMenu.py dans lequel on a le menu de creation des report et les menu ci dessous
    #     # TODO : appeller un menu qui va permettre de retourner une liste de coins
    #     # TODO : appeller un menu qui va permettre de retourner une liste de currency
    #     Output.display_currencies(currencies)
    #     report = Report(name, coins, currencies)
    #     print(report)
    #
    # def choose_currency(self):
    #     """
    #     TODO : Decomposition de la feature ajout de currency dans le report :
    #     - récuperer les currencies
    #     - passer les currencies en paramètre a une fonction qui va les afficher correctement en liste, avec index et retourne l'index
    #     - depuis l'index, retourne la currencie choisie
    #     """
    #     list_currencies = self.search_currencies()
    #     for key, value in enumerate(list_currencies):
    #         print(key, value.short_name)
    #     choice = list_currencies[int(Input.search_currency())]
    #     print(choice)
    #
    # def choose_coin(self):
    #     """
    #     TODO : Decomposition de la feature ajout de coin dans le report :
    #     - rechercher une coin
    #     - passer les coin resultat en paramètre a une fonction qui va les afficher correctement en liste, avec index et retourne l'index
    #     - depuis l'index, retourne la coin choisie
    #     """
    #     pass

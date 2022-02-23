# coding: utf-8
from app.menu.menu import CoinMenu, back, clearscreen
from app.menu.report_menu import ReportMenu


class App:

    def __init__(self):
        self.coin_menu = CoinMenu()
        self.report_menu = ReportMenu()

    def start(self):
        clearscreen()
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
            # print("\nVotre choix est incorrect, Veuillez réessayer.")
            self.start()
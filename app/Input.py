# coding: utf-8


class Input:

    @staticmethod
    def menu():
        menu_text = "\n1.Rechercher une cryptomonnaie\n2.Mes rapports\n3.Quitter\nVotre choix : "
        return int(input(menu_text))

    @staticmethod
    def search_input():
        query = input("\nQuelle cryptomonnaie cherchez-vous ? : ")
        while query is None:
            print("\nErreur")
            query = input("\nQuelle cryptomonnaie cherchez-vous ? : ")
        return query

    @staticmethod
    def back():
        text = "\nRevenir au menu precedent ? O/n(n : Non, autre: Oui) : "
        if input(text) == "n":
            return False
        return True

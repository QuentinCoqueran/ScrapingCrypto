import json
import os

import config
from app.api.request_manager import request_manager


class CoinMenu:

    @staticmethod
    def search_coins():
        clearscreen()
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
        clearscreen()
        self.display_currencies(currencies)
        choose_menu("Monnaie", len(currencies))

    @staticmethod
    def display_currencies(currencies):
        for index, currency in enumerate(currencies):
            print(f'{index}. {currency.short_name}')


def back():
    text = "\nRevenir au menu precedent ? O/n (Oui) : "
    return input(text) != "n"


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_menu(source, size):
    try:
        query = int(input(f'\n{source} -> votre choix : '))
        while query is None or query < 0 or query > size:
            print("\nVotre choix est invalide.")
            query = int(input(f'\n{source} -> votre choix : '))
        return query
    except Exception:
        print("\nUne erreur est survenue, veuillez réessayer")
        choose_menu(source, size)


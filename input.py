# coding: utf-8

from api.RequestManager import RequestManager


def menu() :
    menu = """
    1.Rechercher une cryptomonnaie
    2.Configuration
    3.Quitter

    Votre choix : 
    """
    return int(input(menu))

def search_input():
    query = input("\n Quelle cryptomonnaie cherchez-vous ? : ")
    while(query == None):
        print("\n Erreur")
        query = input("\n Quelle cryptomonnaie cherchez-vous ? : ")
    return query


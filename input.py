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


def menu_action():
    choice = menu()
    while(choice != 0) :
        if(choice == 1):
            search()
            pass
        elif(choice == 2):
        
            break
        
        else :
            print("\n choix incorrect")
            choice = menu()

def search_input():
    query = input("\n Quelle cryptomonnaie cherchez-vous ? : ")
    while(query == None):
        print("\n Erreur")
        query = input("\n Quelle cryptomonnaie cherchez-vous ? : ")
    return query

def search():
    # TODO : Refactor appel reccurent vers RequestManager
    query = search_input()
    r = RequestManager("https://api.coingecko.com/api/v3/")
    r.search_currencies(query)
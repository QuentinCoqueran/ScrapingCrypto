# coding: utf-8

from input import menu, search_input

class App:

    requestManager = None

    def __init__(self, _requestManager):
        self.requestManager = _requestManager;

    def start(self): 
        choice = menu()
        while(choice != 0) :
            if(choice == 1):
                self.search()
                pass
            elif(choice == 2):
                break
            else :
                print("\n choix incorrect")
                choice = menu()
    
    def search(self):
        query = search_input()
        coins = self.requestManager.search_currencies(query)
        for coin in coins : 
            print(coin.name)
        return coins


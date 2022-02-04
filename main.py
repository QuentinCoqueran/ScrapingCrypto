# coding: utf-8

from api.RequestManager import RequestManager
from App import App

def main():
    requestManager = RequestManager("https://api.coingecko.com/api/v3/")
    app = App(requestManager)
    app.start()
    
if __name__ == '__main__':
    main()
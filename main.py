# coding: utf-8

from api.RequestManager import RequestManager
from App import App


def main():
    request_manager: RequestManager = RequestManager("https://api.coingecko.com/api/v3/")
    app = App(request_manager)
    app.start()


if __name__ == '__main__':
    main()

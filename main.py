# coding: utf-8

from api.RequestManager import RequestManager

def main():

    api_url = "https://api.coingecko.com/api/v3/"
    api = RequestManager(api_url)
    print(api.get_vs_currencies())
    
if __name__ == '__main__':
    main()
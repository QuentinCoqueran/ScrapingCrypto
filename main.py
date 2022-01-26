# coding: utf-8

from api.call import ApiCalls

def main():

    api_url = "https://api.coingecko.com/api/v3/"
    api = ApiCalls(api_url)
    print(api.get_vs_currencies())
    

if __name__ == '__main__':
    main()
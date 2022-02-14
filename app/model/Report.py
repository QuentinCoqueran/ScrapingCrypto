class Report:

    def __init__(self, name, coins, currencies):
        self.name = name
        self.coins = coins
        self.currencies = currencies

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, coins):
        self._coins = coins

    @property
    def currencies(self):
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        self._currencies = currencies

    def add_coin(self, coin):
        self.coins.append(coin)

    def add_currency(self, currency):
        self.currencies.append(currency)

    def __str__(self):
        string = "{{\"coins\" : [{}], \"currencies\": [{}]}}".format((', '.join([str(x) for x in self.coins])),
                                                                     (', '.join([str(x) for x in self.currencies])))
        return string

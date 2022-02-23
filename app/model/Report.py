class Report:

    def __init__(self, name, coins, currencies):
        self.name = name
        self.coins = coins
        self.currencies = currencies

    def add_coin(self, coin):
        self.coins.append(coin)

    def add_currency(self, currency):
        self.currencies.append(currency)

    def __str__(self):
        string = "{{ \"name\": \"{}\", \"coins\" : [{}], \"currencies\": [{}]}}" \
            .format(
            self.name,
            (', '.join([str(x) for x in self.coins])),
            (', '.join([str(x) for x in self.currencies])))
        return string

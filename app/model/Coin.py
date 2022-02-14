# coding: utf-8

class Coin:

    def __init__(self, id, name, symbol, market_cap_rank):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.market_cap_rank = market_cap_rank

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @property
    def market_cap_rank(self):
        return self._market_cap_rank

    @market_cap_rank.setter
    def market_cap_rank(self, market_cap_rank):
        self._market_cap_rank = market_cap_rank

    def __str__(self):
        return "{{\"id\": \"{}\",\"name\": \"{}\", \"symbol\": \"{}\", \"market_cap_rank\": \"{}\" }}"\
            .format(self.id, self.name, self.symbol, self.market_cap_rank)

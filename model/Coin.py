# coding: utf-8

class Coin:

    def __init__(self, id, name, symbol, market_cap_rank):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.market_cap_rank = market_cap_rank

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, _id):
        self.id = _id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, _name):
        self.name = _name

    @property
    def symbol(self):
        return self.symbol

    @symbol.setter
    def symbol(self, _symbol):
        self.symbol = _symbol

    @property
    def market_cap_rank(self):
        return self.id

    @market_cap_rank.setter
    def market_cap_rank(self, _market_cap_rank):
        self.market_cap_rank = _market_cap_rank

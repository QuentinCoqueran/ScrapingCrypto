# coding: utf-8

class Coin:

    id = ""
    name = ""
    symbol = ""
    market_cap_rank = ""

    def __init__(self, _id, _name, _symbol, _market_cap_rank):
        self.id = _id
        self.name = _name
        self.symbol = _symbol
        self.market_cap_rank = _market_cap_rank

    # def _get_id(self):
    #     return self.id

    # def _set_id(self, _id):
    #     self.id = _id

    # def _get_name(self):
    #     return self.name

    # def _set_name(self, _name):
    #     self.name = _name

    # def _get_symbol(self):
    #     return self.symbol

    # def _set_symbol(self, _symbol):
    #     self.symbol = _symbol

    # def _get_market_cap_rank(self):
    #     return self.id

    # def _set_market_cap_rank(self, _market_cap_rank):
    #     self.market_cap_rank = _market_cap_rank

    # name = property(_get_name, _set_name)

# coding: utf-8

class Coin:

    def __init__(self, id, name, symbol, market_cap_rank):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.market_cap_rank = market_cap_rank

    def __str__(self):
        return "{{\"id\": \"{}\",\"name\": \"{}\", \"symbol\": \"{}\", \"market_cap_rank\": \"{}\" }}" \
            .format(self.id, self.name, self.symbol, self.market_cap_rank)

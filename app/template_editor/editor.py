from jinja2 import Environment, FileSystemLoader
from app.api.request_manager import request_manager


def generate_template(report):
    data = prepare_data(report)
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.jinja')
    string = template.render(coins=data[0], images=data[1], currencies=data[2], curr_datas=data[3])
    return string


def prepare_data(report):
    curr_datas = request_manager.get_coin_price_by_currencies(report)
    coins = [coin for coin in report.coins]
    currencies = [currency for currency in report.currencies]
    images = {coin.id: request_manager.get_coin_thumb_by_coin_id(coin.id) for coin in coins}
    return [coins, images, currencies, curr_datas]

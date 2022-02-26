from jinja2 import Environment, FileSystemLoader
from app.utils.json_report_util import get_report_by_idx
from app.api.request_manager import request_manager


def generate_template(report):
    data = prepare_data(report)
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')
    string = template.render(coins=data[0], images=data[1], currencies=data[2], prices=data[3])
    return string


def prepare_data(report):
    prices = request_manager.get_coin_price_by_curr(report)
    coins = [coin for coin in report.coins]
    currencies = [currency for currency in report.currencies]
    images = {coin.id: request_manager.get_coin_thumb_by_coin_id(coin.id) for coin in coins}
    return [coins, images, currencies, prices]

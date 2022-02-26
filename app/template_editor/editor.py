from jinja2 import Environment, FileSystemLoader
from app.utils.json_report_util import get_report_by_idx
from app.api.request_manager import request_manager


def generate_template(report):
    prices = request_manager.get_coin_price_by_curr(report)
    coins = [coin for coin in report.coins]
    currencies = [currency for currency in report.currencies]
    env = Environment(loader=FileSystemLoader('templates'))

    template = env.get_template('template.html')
    string = template.render(coins=coins, currencies=currencies, prices=prices)
    with open("templates/template-edited.html", 'w') as template:
        template.write(string)
    return string

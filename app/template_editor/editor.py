from jinja2 import Environment, FileSystemLoader
from app.utils.json_report_util import get_report_by_idx

def generate_template():
    report = get_report_by_idx(1)
    coins = [coin for coin in report.coins]
    currencies = [currency for currency in report.currencies]
    env = Environment(loader=FileSystemLoader('templates'))

    template = env.get_template('template.html')
    string = template.render(title = 'TITRE', coins = coins, currencies = currencies)
    print(string)
    # return string
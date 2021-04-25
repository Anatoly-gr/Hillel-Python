import argparse
from datetime import timedelta
from datetime import datetime
import json
import urllib.request
import requests

currency_from = str(input('Введите тип валюты from: '))
currency_to = str(input('Введите тип валюты для конвертации to: '))
amount = float(input('введите сумму для конвертации: '))
start_date = str(input('Введите дату в формате YYYY-mm-dd: '))
today = datetime.today()

try:
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if start_date > datetime.today():
        start_date = today
except:
    ValueError(print('You entered is incorrected date'))
    start_date = today

with open('symbols.json', 'r+') as file:
    cur_dict = (json.load(file))
    currency_to = currency_to.upper()
    currency_from = currency_from.upper()
    if currency_from in cur_dict['symbols'] and currency_to in cur_dict['symbols']:
        # start_date = datetime.strptime(start_date, '%Y-%m-%d')
        print(f"'date',   'from',   'to', 'amount',\t 'rate', \t'result'")
        while start_date <= today:
            url = "https://api.exchangerate.host/convert"
            payload = {'from': currency_from, 'to': currency_to, 'amount': amount, 'date': start_date}

            r = requests.get(url, params=payload)
            request = urllib.request.urlopen(r.url)
            data = json.load(request)
            # print(data)
            print(f"{start_date.strftime('%d-%m-%Y')}, {data['query']['from']}, '\t'{data['query']['to']}, "
                  f" {data['query']['amount']}, \t {data['info']['rate']}, {data['result']}")
            start_date += timedelta(days=1)
    else:
        print('Wrong type of currency')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Currency exchange')
    parser.add_argument('currency_from')
    parser.add_argument('currency_to')
    args = parser.parse_args()

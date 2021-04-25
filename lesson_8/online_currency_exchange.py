import argparse
from datetime import datetime
from datetime import timedelta
import json
import urllib.request

import requests


def main():
    currency_from = args.cur_f
    currency_to = args.cur_to
    amount = args.amnt
    start_day = args.start_day
    today = datetime.today()
    try:
        start_day = datetime.strptime(start_day, '%Y-%m-%d')
        if start_day > datetime.today():
            start_day = today
    except ValueError as err:
        print('You entered is incorrect date', err)
        start_day = today
    # print(currency_from, currency_to, amount, start_day)
    with open('symbols.json', 'r+') as file:
        cur_dict = json.load(file)
        currency_to = currency_to.upper()
        currency_from = currency_from.upper()
        if currency_from in cur_dict['symbols'] and currency_to in cur_dict['symbols']:
            print(f"'date',   'from', 'to', 'amount',\t'rate',\t\t'result'")
            while start_day <= today:
                url = "https://api.exchangerate.host/convert"
                payload = {'from': currency_from, 'to': currency_to, 'amount': amount, 'date': start_day}

                r = requests.get(url, params=payload)
                request = urllib.request.urlopen(r.url)
                data = json.load(request)
                # print(data)
                print(f"{start_day.strftime('%d-%m-%Y')}, {data['query']['from']},  {data['query']['to']}, "
                      f" {data['query']['amount']}, \t\t {data['info']['rate']}, \t{data['result']}")
                start_day += timedelta(days=1)
        else:
            print('Wrong type of currency')
    return

if __name__ == '__main__':
    t = datetime.today().strftime('%Y-%m-%d')
    parser = argparse.ArgumentParser(description='Currency exchange')
    parser.add_argument('cur_f')
    parser.add_argument('cur_to')
    parser.add_argument('amnt')
    parser.add_argument('--start_day', default=t, type=str)
    args = parser.parse_args()

main()

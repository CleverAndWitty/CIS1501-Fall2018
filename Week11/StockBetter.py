import requests
import os
import json
import datetime
import random

picks = [ 'AAPL', 'AMZN', 'MSFT', 'GOOGL', 'FB' ]

url = 'https://api.iextrading.com/1.0/stock/{}/chart/1y'
companies = {}
for symbol in picks:
    try:
        if not os.path.exists(symbol):
            response = requests.get(url.format(symbol))
            data = response.json()
            with open(symbol, 'w') as file:
                file.write(str(data))
        else:
            with open(symbol) as file:
                raw = file.read()
                data = json.loads(raw.replace("'", '"'))
        companies[symbol] = data
    except Exception as e:
        print(e)

#for company in companies:
#    print(company, ': ', companies[company])

apple = companies['AAPL']
print(apple)

trends = {}
for number in range(-9, 10):
    trends[number] = 0

gaining_days_in_a_row = 0
losing_days_in_a_row = 0
yesterdays_close = 0

six_months_ago = datetime.date.today() - datetime.timedelta(days=182)

for day in apple:
    day_string = str(day['date'])
    day_string_split = day_string.split('-')
    today = datetime.date(year=int(day_string_split[0]),
                          month=int(day_string_split[1]),
                          day=int(day_string_split[2]))
    if today < six_months_ago:
        #print('AAPL: ', day['label'], day['close'])
        if yesterdays_close == 0:
            yesterdays_close = float(day['close'])
        todays_close = float(day['close'])

        if todays_close < yesterdays_close:
            losing_days_in_a_row -= 1
            if gaining_days_in_a_row > 0:
                trends[gaining_days_in_a_row] += 1
            gaining_days_in_a_row = 0
        elif todays_close > yesterdays_close:
            gaining_days_in_a_row += 1
            if losing_days_in_a_row < 0:
                trends[losing_days_in_a_row] += 1
            losing_days_in_a_row = 0
        yesterdays_close = todays_close

for streak, count in trends.items():
    print("Streak:", streak, ":", count )


cash = 100000.0
stock = 0.0

monkey_cash = 100000.0
monkey_stock = 0.0

yesterdays_close = 0

for day in apple:
    day_string = str(day['date'])
    day_string_split = day_string.split('-')
    today = datetime.date(year=int(day_string_split[0]),
                          month=int(day_string_split[1]),
                          day=int(day_string_split[2]))
    if today > six_months_ago:
        #print('AAPL: ', day['label'], day['close'])
        if yesterdays_close == 0:
            yesterdays_close = float(day['close'])
        todays_close = float(day['close'])

        if todays_close < yesterdays_close:
            losing_days_in_a_row -= 1
            gaining_days_in_a_row = 0

        elif todays_close > yesterdays_close:
            gaining_days_in_a_row += 1
            losing_days_in_a_row = 0


        if losing_days_in_a_row == -3:
            stock += 10
            cash -= todays_close * 10
            print("bought 10 at", todays_close)

        if gaining_days_in_a_row == 1:
            if stock > 0:
                print("Sold", stock, "for", todays_close)
                cash += stock * todays_close
                stock = 0

        if random.randint(0, 1) == 0:
            monkey_stock += 10
            monkey_cash -= todays_close * 10
            #print("bought 10 at", todays_close)

        elif random.randint(0, 1) == 0:
            if stock > 0:
                #print("Sold", stock, "for", todays_close)
                monkey_cash += monkey_stock * todays_close
                monkey_stock = 0

        yesterdays_close = todays_close

if stock > 0:
    print("Sold", stock, "for", todays_close)
    cash += stock * todays_close
    stock = 0


if monkey_stock > 0:
    print("Sold", monkey_stock, "for", todays_close)
    monkey_cash += monkey_stock * todays_close
    monkey_stock = 0

print("cash at end:", cash)
print("monkey cash:", monkey_cash)
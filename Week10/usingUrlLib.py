import json
import urllib3
urllib3.disable_warnings()

url = 'https://api.iextrading.com/1.0/stock/aapl/chart'

http = urllib3.PoolManager()
response = http.request('GET', url)
data = json.loads(response.data.decode('utf-8'))


for date in data:
    print(date['date'], ":", date['close'])
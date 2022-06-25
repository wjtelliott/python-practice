import pprint
from urllib import response
import requests
from matplotlib import pyplot as plt
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)

API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'madison'
r = requests.get(API_URL + city)
response = r.json()
pp.pprint(response)

forecast_list = response['forecast']
today = datetime.now().strftime('%b-%d-%Y')

to_graph = dict()
count = 1

for day in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count += 1

    to_graph[this_day] = day['wind']
print('To Graph data => ', to_graph)

plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')

format_value = lambda item: __import__('re').sub(r' km/h$', '', item)

for i in to_graph.keys():
    new_value = format_value(to_graph[i])
    to_graph[i] = 0 if new_value == '' else int(new_value)

print('to_graph keys: ', to_graph.keys())
print('to_graph values: ', to_graph.values())


plt.scatter(to_graph.keys(), to_graph.values())
plt.show()
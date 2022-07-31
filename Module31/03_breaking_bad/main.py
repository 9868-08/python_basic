import requests
import json
from collections import Counter

my_req = requests.get('https://www.breakingbadapi.com/api/Deaths')  # парсинг сайта
data = json.loads(my_req.text)  # десериализация JSON

deaths_dict = dict()

for item in data:
    deaths_dict[item['season'] * 100 + item['episode']] = item["number_of_deaths"]

deaths_list = list(deaths_dict.items())
sorted_deaths_list = sorted(deaths_list, key=lambda sort: -sort[1])
decoded_sorted_deaths_list = list()

for item in sorted_deaths_list:
    print("season", item[0] // 100, "episode", item[0] % 100, "deaths:", item[1])
    decoded_sorted_deaths_list.append(["season", item[0] // 100, "episode", item[0] % 100, "deaths:", item[1]])

with open("03_breaking_bad.json", "w") as file:
    json.dump(decoded_sorted_deaths_list, file, indent=4)  # сериализация JSON
file.close()
